import pygame
import time
import math
import sys

class GameOver:
    def __init__(self, screen, winner):
        self.width = 1000
        self.height = 700
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background1 = Background("background.jpg", [0,0])
        self.screen.fill(pygame.Color("white"))
        self.newfont = pygame.font.Font("CountryGold.ttf", 100)
        self.newfont3 = pygame.font.Font("CountryGold.ttf",40)
        self.newfont1 = pygame.font.Font("CountryGold.ttf", 40)
        self.newfont2 = pygame.font.Font("CountryGold.ttf", 35)
        self.gameover1 = self.newfont.render("Game Over", 1, pygame.Color("black"))
        self.winner = winner
        if self.winner == "p1":
            self.gameover2 = self.newfont3.render("Player 1 Took It All The Way To The Top!", 1, pygame.Color("black"))
        if self.winner == "p2":
            self.gameover2 = self.newfont3.render("Player 2 Took It All The Way To The Top!", 1, pygame.Color("black"))




    def boxDraw(self, x, y, width, height, text, textx):
        button = pygame.rect.Rect(x, y, width, height)
        buttontext = self.newfont2.render(text, 1, pygame.Color("black"))
        pygame.draw.rect(self.screen, pygame.Color("black"),button,4)
        centerpoint=(textx,y+13)
        self.screen.blit(buttontext, centerpoint)
        posx, posy = pygame.mouse.get_pos()
        if posx > x and posx< x+width and posy > y and posy < y+height:
            highlight = pygame.rect.Rect(x-5, y-5, width+10, height+10)
            pygame.draw.rect(self.screen, pygame.Color("white"), highlight, 5)

    def runGameOver(self):
        pygame.key.set_repeat(500, 30)
        while 1:
            t=time.time()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.checkForQuit():
                        sys.exit()
                    if self.checkForPlayAgain():
                        return "PlayAgain"
                    if self.checkForCredits():
                        return "Credits"
                    if self.checkForMM():
                        return "MM"

            self.screen.blit(self.background1.image, (0,0))
            self.screen.blit(self.gameover1, (225, 30))
            self.screen.blit(self.gameover2, (120, 160))
            self.boxDraw(400, 240, 200, 60,"Play Again",417)
            self.boxDraw(400, 320, 200, 60, "Main Menu", 407)
            self.boxDraw(400, 400, 200, 60, "Credits", 447)
            self.boxDraw(400, 480, 200, 60, "Quit", 468)
            pygame.display.update()
            time.sleep(max(0.017-(time.time()-t),0))

    def checkForPlayAgain(self):
        p1x, p1y = pygame.mouse.get_pos()
        if p1x > 400 and p1x < 600 and p1y > 240 and p1y < 300:
            return True

    def checkForMM(self):
        p1x, p1y = pygame.mouse.get_pos()
        if p1x > 400 and p1x < 600 and p1y > 320 and p1y < 380:
            return True

    def checkForCredits(self):
        p1x, p1y = pygame.mouse.get_pos()
        if p1x > 400 and p1x < 600 and p1y > 400 and p1y < 460:
            return True

    def checkForQuit(self):
        p1x, p1y = pygame.mouse.get_pos()
        if p1x > 400 and p1x < 600 and p1y > 480 and p1y < 540:
            return True


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("background.jpg")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location