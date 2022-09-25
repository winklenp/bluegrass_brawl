import pygame
import vector
import attack

class Projectile:
    def __init__(self,screen,x,y,direction,image):
        self.direction=direction
        if direction==0:
                    self.image=pygame.transform.scale(image,(self.rect.width,self.rect.height))
        else:
                    self.image=pygame.transform.flip(pygame.transform.scale(image,(self.rect.width,self.rect.height)),True,False)
        self.d=vector.Vector(0,0)
        self.GRAVITYSTRENGTH=0.5
        self.screen=screen
        self.moving=True
        self.x=x
        self.y=y
        self.updateRect()

    def update(self):
        self.x+=self.d.x
        self.y+=self.d.y
        self.d.y+=self.GRAVITYSTRENGTH
        if self.y>self.screen.get_height() or self.x>self.screen.get_width()+self.rect.width or self.x<-self.rect.width:
            self.moving=False
        self.updateRect()

    def updateRect(self):
        self.rect.centerx=int(self.x)
        self.rect.y=int(self.y)

    def render(self):
        self.screen.blit(self.image,(self.x-self.rect.width/2,self.y))
    
    def hit(self,target):
        self.moving=False

class Pitchfork(Projectile):
    def __init__(self, screen, user, direction):
        self.rect=pygame.rect.Rect(0,0,120,30)
        Projectile.__init__(self,screen,user.rect.centerx,user.rect.centery,direction,pygame.image.load("CharacterFiles/CharacterModels/BlueGrassBilly/pitchfork.png"))
        self.d.x=20
        self.d.y=-3
        if direction==1:
            self.d.flipXIp()
        self.hitbox=attack.Hitbox((-self.rect.width/2,-self.rect.height,self.rect.width,self.rect.height),vector.Vector(7,-4),35)

class HelmetShot(Projectile):
    def __init__(self, screen, user, direction):
        self.rect=pygame.rect.Rect(0,0,80,60)
        Projectile.__init__(self,screen,user.rect.centerx,user.rect.top,direction,pygame.image.load("CharacterFiles/CharacterModels/MetalMan/helmetShot.png"))
        self.d.x=8
        self.d.y=0
        self.GRAVITYSTRENGTH=0
        if direction==1:
            self.d.flipXIp()
        self.hitbox=attack.Hitbox((-10,-60,40,60),vector.Vector(10,-8),110)

class Fireball(Projectile):
    def __init__(self, screen, user, direction):
        self.rect=pygame.rect.Rect(0,0,80,80)
        Projectile.__init__(self,screen,user.rect.centerx,user.rect.top,direction,pygame.image.load("CharacterFiles/CharacterModels/MonstrousMike/fireball.png"))
        self.d.x=8
        self.d.y=-0.2
        self.GRAVITYSTRENGTH=0.1
        if direction==1:
            self.d.flipXIp()
        self.hitbox=attack.Hitbox((-40,-70,80,60),vector.Vector(10,-8),35)

class Microphone(Projectile):
    def __init__(self,screen,user,direction):
        self.rect=pygame.rect.Rect(0,0,66,30)
        Projectile.__init__(self,screen,user.rect.centerx,user.rect.centery,direction,pygame.image.load("CharacterFiles/CharacterModels/SinginSusan/microphone.png"))
        self.d.x=13
        self.d.y=-8
        if direction==1:
            self.d.flipXIp()
        self.hitbox=attack.Hitbox((-33,-30,66,30),vector.Vector(10,-8),60)

class Pig(Projectile):
    def __init__(self,screen,user,direction):
        self.rect=pygame.rect.Rect(0,0,80,60)
        Projectile.__init__(self,screen,user.rect.centerx,user.rect.bottom-60,direction,pygame.image.load("CharacterFiles/CharacterModels/CountryCarl/pig.png"))
        self.d.x=15
        self.d.y=0
        self.GRAVITYSTRENGTH=0
        if direction==1:
            self.d.flipXIp()
        self.hitbox=attack.Hitbox((-40,-60,80,60),vector.Vector(10,-16),20)
    
    def hit(self,target):
        pass

class Axe(Projectile):
    def __init__(self,screen,user,direction):
        self.rect=pygame.rect.Rect(0,0,75,45)
        Projectile.__init__(self,screen,user.rect.centerx,user.rect.centery,direction,pygame.image.load("CharacterFiles/CharacterModels/BackwoodsBob/axe.png"))
        self.d.x=12
        self.d.y=-7
        if direction==1:
            self.d.flipXIp()
        self.hitbox=attack.Hitbox((-37,-45,75,45),vector.Vector(10,-8),20)

class Knife(Projectile):
    def __init__(self,screen,user,direction):
        self.rect=pygame.rect.Rect(0,0,66,30)
        Projectile.__init__(self,screen,user.rect.centerx,user.rect.centery,direction,pygame.image.load("CharacterFiles/CharacterModels/SinisterStan/projectile.png"))
        self.d.x=14
        self.d.y=-3
        self.GRAVITYSTRENGTH=0.3
        if direction==1:
            self.d.flipXIp()
        self.hitbox=attack.Hitbox((-33,-30,66,30),vector.Vector(2,0),100)