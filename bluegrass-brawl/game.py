import sys
import time
import pygame
import health
from BBplatform import Platform
import CharacterFiles.character as char
from random import randint

BGCOLOR=(0,255,255)

SHOWFPS=False

def main():
    pygame.init()
    game = Game()
    game.runGame()



"""
Game class
"""
class Game:
    def __init__(self,player1,player2):
        self.width = 1000
        self.height = 700
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.BGIMAGE=pygame.transform.scale(pygame.image.load("background.jpg"),(self.width,self.height))
        self.screen.fill(BGCOLOR)
        self.player1=self.getPlayer(self.width/4,self.height-100,player1)
        self.player2=self.getPlayer(self.width*3/4,self.height-100,player2)
        self.player1Bar = health.HealthBar(self.screen,10, 10, self.player1)
        self.player2Bar=health.HealthBar(self.screen, self.width - 210, 10, self.player2)
        self.platforms=[Platform(self.screen,-80,self.height-10,self.width + 120)]
        self.font = pygame.font.Font("CountryGold.ttf", 30)
        self.p1 = self.font.render("Player 1", 1, pygame.Color("black"))
        self.p2 = self.font.render("Player 2", 1, pygame.Color("black"))
        for i in range(15):
            self.addPlatform()
    def getPlayer(self,x,y,player):
        if player==0:
            return char.BlueGrassBilly(self.screen,x,y)
        elif player==1:
            return char.CountryCarl(self.screen,x,y)
        elif player==2:
            return char.SinginSusan(self.screen,x,y)
        elif player==3:
            return char.BackwoodsBob(self.screen,x,y)
        elif player==4:
            return char.MetalMan(self.screen,x,y)
        elif player == 5:
            return char.SinisterStan(self.screen, x, y)
        elif player==6:
            return char.EvilEmily(self.screen,x,y)
        elif player==7:
            return char.MonstrousMike(self.screen,x,y)
        else:
            return char.MetalMan(self.screen,x,y)

    def addPlatform(self):
        for i in range(50):
            width=randint(200,600)
            rect=pygame.rect.Rect(randint(-100,self.screen.get_width()-100-width),randint(50,self.screen.get_height()-150),width+200,400)
            valid=True
            for p in self.platforms:
                if p.rect.colliderect(rect):
                    valid=False
                    break
            if valid:
                self.platforms.append(Platform(self.screen,rect.left+100,rect.top+150,width))
                break

    def runGame(self):
        pygame.key.set_repeat(500, 30)
        pygame.display.set_caption('Bluegrass Brawl')
        fpsTime=time.time()
        frames=0
        while 1:
            t=time.time()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.update()
            if self.player1.deathCounter<=0 or self.player2.deathCounter<=0:
                if self.player1.deathCounter<=0:
                    return "p2"
                else:
                    return "p1"

            self.render()
            self.screen.blit(self.p1, (220, 5))
            self.screen.blit(self.p2, (660, 5))
            pygame.display.update()
            time.sleep(max(0.017-(time.time()-t),0))
            if SHOWFPS:
                frames+=1
                now=time.time()
                if now-fpsTime>=1:
                    print(frames/(now-fpsTime))
                    frames=0
                    fpsTime=time.time()

    def update(self):
        keys=pygame.key.get_pressed()
        self.player2.update(keys[pygame.K_j],keys[pygame.K_l],keys[pygame.K_i],keys[pygame.K_k],keys[pygame.K_n],keys[pygame.K_SEMICOLON] or keys[pygame.K_b],self.platforms)
        self.player1.update(keys[pygame.K_a],keys[pygame.K_d],keys[pygame.K_w],keys[pygame.K_s],keys[pygame.K_z],keys[pygame.K_LSHIFT] or keys[pygame.K_f],self.platforms)
        collision=self.player1.checkHit(self.player2)
        self.addKnockback(collision)
        collision=self.player2.checkHit(self.player1)
        self.addKnockback(collision) 

    def addKnockback(self, collision):
        if not collision[0]:
            return
        if collision[3]==self.player1:
            self.player1Bar.damage(collision[1].damage)
            self.player1.d.set(collision[1].getKnockback(collision[2]))
            self.player1.red=True
        else:
            self.player2Bar.damage(collision[1].damage)
            self.player2.d.set(collision[1].getKnockback(collision[2]))
            self.player2.red=True

    def render(self):
        #self.screen.fill(BGCOLOR)
        self.screen.blit(self.BGIMAGE,(0,0))
        self.player1.render()
        self.player2.render()
        self.player1Bar.render()
        self.player2Bar.render()
        for p in self.platforms:
            p.render()

    def gamedebug(self):
        main()