import pygame
import vector
import projectile


class Attack:
    def __init__(self,frames,mustLand=False):
        self.frames=frames
        self.frameID=[]
        self.mustLand=mustLand
        self.ready=True
        index=0
        for frame in self.frames:
            for i in range(frame.quantity):
                self.frameID.append(index)
            index+=1
        self.frameOn=0
        

    def start(self):
        """Initializes the attack for use."""
        self.frameOn=0

    def update(self,user):
        """Advances the attack by one frame. If the attack has ended, it returns True. Otherwise, it returns False."""
        if self.frameOn>=len(self.frameID):
            return True
        self.frames[self.frameID[self.frameOn]].updateUser(user)
        self.frameOn+=1
        return False

    def getCurrentFrame(self):
        if self.frameOn>=len(self.frameID):
            return self.frames[0]
        else:
            return self.frames[self.frameID[self.frameOn]]

class AttackFrame:
    def __init__(self, image, hitboxes=[], velocity=vector.Vector(0,0), quantity=1, projectile=None):
        self.image=image
        self.hitboxes=hitboxes
        self.velocity=velocity
        self.quantity=quantity
        self.projectile=projectile

    def updateUser(self, user):
        user.image=self.image
        if self.velocity.magSquared()!=0:
            if user.direction==1:
                user.d.set(self.velocity.flipX())
            else:
                user.d.set(self.velocity)

    def getProjectile(self, user, screen):
        if self.projectile==None:
            return None
        elif self.projectile=="Pitchfork":
            return projectile.Pitchfork(screen,user,user.direction)
        elif self.projectile=="HelmetShot":
            return projectile.HelmetShot(screen,user,user.direction)
        elif self.projectile=="Fireball":
            return projectile.Fireball(screen,user,user.direction)
        elif self.projectile=="Microphone":
            return projectile.Microphone(screen,user,user.direction)
        elif self.projectile=="Pig":
            return projectile.Pig(screen,user,user.direction)
        elif self.projectile=="Axe":
            return projectile.Axe(screen,user,user.direction)
        elif self.projectile=="Knife":
            return projectile.Knife(screen,user,user.direction)
        else:
            return None


        
        


class Hitbox:
    def __init__(self, rect, knockback, damage):
        self.rect=pygame.rect.Rect(rect[0],rect[1],rect[2],rect[3])
        self.knockback=knockback
        self.damage=damage

    def getRect(self, user):
        if user.direction==0:
            return (user.rect.centerx+self.rect.left,user.rect.bottom+self.rect.top,self.rect.width,self.rect.height)
        else:
            return (user.rect.centerx-self.rect.right,user.rect.bottom+self.rect.top,self.rect.width,self.rect.height)

    def getKnockback(self, user):
        if user.direction==1:
            return self.knockback.flipX()
        else:
            return self.knockback
