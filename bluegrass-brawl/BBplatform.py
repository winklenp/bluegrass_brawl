import pygame
from vector import Vector

class Platform:
    def __init__(self, screen, x, y, width):
        self.rect=pygame.rect.Rect(x,y,width,10)
        self.color=(0,0,0)
        self.screen=screen
        
    def intersects(self, fighter):
        return self.rect.colliderect(fighter.rect)

    def isOn(self, fighter):
        return self.rect.top==fighter.rect.bottom and self.rect.right>fighter.rect.left and self.rect.left<fighter.rect.right

    def getEjection(self, fighter):
        if not self.intersects(fighter):
            return Vector(0,0)
        overlap=[]
        overlap.append(fighter.rect.right-self.rect.left)
        overlap.append(self.rect.right-fighter.rect.left)
        overlap.append(fighter.rect.bottom-self.rect.top)
        overlap.append(self.rect.bottom-fighter.rect.top)
        direction=overlap.index(min(overlap))
        if direction==0:
            return Vector(-overlap[0],0)
        elif direction==1:
            return Vector(overlap[1],0)
        elif direction==2:
            return Vector(0,-overlap[2])
        else:
            return Vector(0,overlap[3])
    
    def render(self):
        pygame.draw.rect(self.screen,self.color,self.rect)