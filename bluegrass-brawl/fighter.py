import pygame
import vector

SHOW_HITBOXES=False

class Fighter(pygame.sprite.Sprite):

    def __init__(self,screen,x,y,health,directory):
        pygame.sprite.Sprite.__init__(self)
        self.x=x
        self.y=y
        self.d=vector.Vector(0,0)
        self.hitboxcolor=(255,0,123)
        self.screen=screen
        self.hitBoxWidth = 95
        self.hitBoxHeight = 120
        self.rect=pygame.rect.Rect(x,y,self.hitBoxWidth,self.hitBoxHeight)
        self.WALKSPEED=3
        self.JUMPSPEED=10
        self.WALKACCEL=0.5
        self.GRAVITYSTRENGTH=0.5
        self.upaccel=2
        self.health = health
        self.image=0
        self.direction=0
        self.IMG=[]
        self.IMG.append([])
        self.IMG[0].append(self.load(directory+"lookingRight.png"))
        self.IMG[0].append(self.load(directory+"attackingRight.png"))
        self.IMG[0].append(self.load(directory+"attackingRight2.png"))
        self.IMG[0].append(self.load(directory+"attackingRight3.png"))
        self.IMG[0].append(self.load(directory+"walkingRight.png"))
        self.IMG.append([])
        self.IMG[1].append(self.load(directory+"lookingRight.png",True))
        self.IMG[1].append(self.load(directory+"attackingRight.png",True))
        self.IMG[1].append(self.load(directory+"attackingRight2.png",True))
        self.IMG[1].append(self.load(directory+"attackingRight3.png",True))
        self.IMG[1].append(self.load(directory+"walkingRight.png",True))
        self.IMG.append([])
        self.IMG[2].append(self.load(directory+"dead.png"))
        self.REDIMG=[]
        for x in range(len(self.IMG)):
            self.REDIMG.append([])
            for y in range(len(self.IMG[x])):
                if self.IMG[x][y]!=None:
                    self.REDIMG[x].append(self.IMG[x][y].copy())
                    self.setRed(self.REDIMG[x][y])
                else:
                    self.REDIMG[x].append(None)
        self.grounded=True
        self.attack=None
        self.dead=False
        self.projectiles=[]
        self.deathCounter=90
        self.landReady=True
        self.walkCounter=0
        self.stepLength=12
        self.red=False

    def setRed(self, img):
        array=pygame.surfarray.pixels_red(img)
        for x in array:
            for y in range(len(x)):
                x[y]=255

    def load(self, file, flip=False):
        try:
            return pygame.transform.flip(pygame.transform.scale(pygame.image.load(file),(self.imageRect.width,self.imageRect.height)),flip,False)
        except:
            return None

    def update(self,left,right,up,down,platforms):
        self.red=False
        if self.dead:
            left=False
            right=False
            up=False
            down=False
            self.deathCounter-=1
            if self.deathCounter<=0:
                self.dead = True
        if self.attack!=None:
            self.walkCounter=0
            if self.grounded:
                self.d.frictionIp(self.WALKACCEL,0)
            if self.attack.update(self):
                self.attack=None
                self.image=0
            else:
                p=self.attack.getCurrentFrame().getProjectile(self,self.screen)
                if p!=None:
                    self.projectiles.append(p)
        elif left and self.d.x>-self.WALKSPEED:
            self.d.addIp(-self.WALKACCEL,0)
            self.direction=1
            if self.grounded:
                self.advanceWalk()
        elif right and self.d.x<self.WALKSPEED:
            self.d.addIp(self.WALKACCEL,0)
            self.direction=0
            if self.grounded:
                self.advanceWalk()
        elif self.grounded:
            self.d.frictionIp(self.WALKACCEL,0)
            if not left and not right:
                self.walkCounter=0

        if self.x+self.rect.width<0:
            #self.x=0
            self.x=self.screen.get_width()
            #self.d.x=0
        if self.x>self.screen.get_width():
            #self.x=self.screen.get_width()-self.rect.width
            self.x=1
            #self.d.x=0

        if self.attack==None and self.grounded and up:
            self.d.y=-self.JUMPSPEED
            self.grounded=False
        self.x+=self.d.x
        self.y+=self.d.y

        self.updateRect()
        self.grounded=False
        for p in platforms:
            v=p.getEjection(self)
            if v.magSquared()>0:
                self.x+=v.x
                self.y+=v.y
                self.rect.move_ip(v.x,v.y)
            if p.isOn(self):
                self.grounded=True
                if self.attack==None:
                    self.landReady=True
                self.d.y=0

        if not self.grounded:
            self.grav(self.GRAVITYSTRENGTH)
        
        for p in self.projectiles:
            p.update()
            if not p.moving:
                self.projectiles.remove(p)

    def advanceWalk(self):
        self.walkCounter+=1
        if self.walkCounter>=self.stepLength*2:
            self.walkCounter=0

    def updateRect(self):
        width=self.rect.width
        height=self.rect.height
        self.rect.left=int(self.x)
        self.rect.top=int(self.y)
        self.rect.right=self.rect.left+width
        self.rect.bottom=self.rect.top+height

    def render(self):
        imgArray=self.IMG
        if self.red:
            imgArray=self.REDIMG
        if self.image==0 and self.walkCounter>=self.stepLength and not self.dead:
            img=imgArray[self.direction][-1]
        else:
            img=imgArray[self.direction][self.image]
        self.screen.blit(img,(self.rect.centerx-img.get_width()/2,self.rect.bottom-img.get_height()))
        for p in self.projectiles:
            p.render()
        if SHOW_HITBOXES:#Debug feature, draws hitboxes
            self.fillTranslucent(self.rect)
            if self.attack!=None:
                for box in self.attack.getCurrentFrame().hitboxes:
                    pygame.draw.rect(self.screen,self.hitboxcolor,box.getRect(self))
            for p in self.projectiles:
                self.fillTranslucent(pygame.rect.Rect(p.hitbox.getRect(p)))

    def fillTranslucent(self,rect):
        s=pygame.Surface((rect.width,rect.height))
        s.set_alpha(128)
        s.fill(self.hitboxcolor)
        self.screen.blit(s,(rect.left,rect.top))

    def grav(self, gravaccel):
        self.d.addIp(0, gravaccel)
    
    def checkHit(self, opponent):
        if self.attack != None:
            result=None
            for box in self.attack.getCurrentFrame().hitboxes:
                if opponent.rect.colliderect(box.getRect(self)):
                    result=(True,box,self,opponent)
                for p in opponent.projectiles:
                    if p.rect.colliderect(box.getRect(self)):
                        opponent.projectiles.remove(p)
            if result!=None:
                return result
        for p in opponent.projectiles:
            if self.rect.colliderect(p.hitbox.getRect(p)):
                p.hit(self)
                return (True, p.hitbox, p,self)
        return (False,None,None)

    def die(self):
        if not self.dead:
            self.attack=None
            self.dead=True
            self.image=0
            self.direction=2
            
        return self.dead

    def checkAirAttack(self):
        if self.attack!=None and self.attack.mustLand:
            if self.landReady:
                self.landReady=False
            else:
                self.attack=None