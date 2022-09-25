import pygame
import math
import time
import sys
import random

class HealthBar(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, player):
        self.screen = screen
        self.x=x
        self.y=y
        self.player = player
        self.color = (229, 22, 22)
        self.bgcolor = (60,60,60)
        self.bar = pygame.draw.rect(self.screen, (229, 22, 22), (x,y,200,25))
        self.fullBar=pygame.rect.Rect(x,y,200,25)
        self.currentHealth = self.player.health
        self.health = self.player.health
        self.sounds = ["sounds/punchSound.wav", "sounds/punchSound2.wav", "sounds/slapSound.wav", "sounds/kickSound.wav"]
        self.points = [[self.bar.topright[0], self.bar.topright[1]], [self.bar.topright[0]-25, self.bar.topright[1]], [self.bar.topright[0]-25, self.bar.topright[1]+25]]
    
    def render(self):
        pygame.draw.rect(self.screen,self.bgcolor,self.fullBar)
        self.pointList = [(self.points[0][0], self.points[0][1]), (self.points[1][0], self.points[1][1]), (self.points[2][0], self.points[2][1])]
        if self.currentHealth > 0:
            pygame.draw.polygon(self.screen, self.color, self.pointList, 0)
        if self.bar.width>0:
            pygame.draw.rect(self.screen,self.color,self.bar)
    
    def moveTriangle(self,dx):
        for point in self.points:
            point[0] += dx
    
    def damage(self, damage):
        sound = random.randint(0, len(self.sounds) -1)
        sound = pygame.mixer.Sound(self.sounds[sound])
        sound.set_volume(0.9)
        pygame.mixer.Sound.play(sound)
        self.currentHealth -= damage
        width = (self.currentHealth/self.health) * 200
        self.bar.width = width
        if self.points[-1][0] > self.bar.topright[0]:
           self.moveTriangle(self.bar.topright[0] - self.points[-1][0]) 
        self.player.health = self.currentHealth
        # tunes = pygame.mixer.music.load("sounds/bluegrassSong.mp3")
        # pygame.mixer.music.play(20)
        if self.currentHealth <= 0:
            self.bar.width = 0
            self.points[-1][0]= self.points[1][0]
            self.player.die()


