import math
import sys
import random

import pygame
from pygame.locals import *
from Engine import misc,characters
characters=characters.characters()
buttonCheck=0
pressed=[False,False,False,False]
# The Main Menu object. Accepts no parameters to its constructor
class Menu(object):
    def __init__(self):
        self.buttonXY=[]
        self.drawButtons=[]
        self.running = True
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.get_surface()
        self.resourceFilepath = "Resources/Interface/Start Menu/Background/"
        self.gobletLogo = pygame.image.load(self.resourceFilepath + "Goblet Logo.png")
 #       self.gobletLogo = pygame.transform.scale(self.gobletLogo, (self.screen.get_size()))
        self.backgroundImg1 = pygame.image.load(self.resourceFilepath + "Background-sky.png").convert()
        self.backgroundImg1 = pygame.transform.scale(self.backgroundImg1, (self.screen.get_size()))
        self.backgroundImg2 = pygame.image.load(self.resourceFilepath + "Wizard-Tower.png")
        self.backgroundImg2 = pygame.transform.scale(self.backgroundImg2,
                                                    (
                                                    int(self.screen.get_width()/8),
                                                    int(self.screen.get_height()/2)
                                                    )
                                                )
        
        self.midgroundImg = pygame.image.load(self.resourceFilepath + "Background-Trees+grass.png")
        self.midgroundImg = pygame.transform.scale(self.midgroundImg, (self.screen.get_size()))       

        self.foregroundImg = pygame.image.load(self.resourceFilepath + "Foreground-Clouds.png")
        self.foregroundImg = pygame.transform.scale(self.foregroundImg, (self.screen.get_size()))
        self.cloudx = 0
    def menu_create(self,img):
        global buttonCheck
        XY=[]
        surface=pygame.display.get_surface()
        buttons = pygame.image.load(img).convert_alpha()
        x= int(self.screen.get_width() / 2) - 100
        y = int(self.screen.get_height() / 3) + (75*(buttonCheck))
        width = buttons.get_width()
        height = buttons.get_height()
        surface.blit(buttons,(x,y))
        XY.append(x)
        XY.append(y)
        self.buttonXY.append(XY)
        buttonCheck+=1
        listO=0
        while len(self.buttonXY)>4:
            del self.buttonXY[listO]
            listO+=1
            
    def menuAnimation(self):
        global buttonCheck
        self.screen.blit(self.backgroundImg1, (0,0))
        self.screen.blit(self.gobletLogo, ((self.screen.get_width() * .5) - 200, self.screen.get_height() *.1))
        for x in range(2):
            self.screen.blit(self.foregroundImg, (self.cloudx+(self.foregroundImg.get_width()*x), 0))
        if self.cloudx<0-self.foregroundImg.get_width():
            self.cloudx=0
        self.cloudx -= self.foregroundImg.get_width()/600
        self.screen.blit(self.backgroundImg2,(self.screen.get_width() * .7, self.screen.get_height() * .15))
        self.screen.blit(self.midgroundImg, (0,0))
        if pressed[0]:
            self.menu_create("Resources/Interface/Start Menu/Buttons/Start-Button-Pressed.png")
        else:
            self.menu_create("Resources/Interface/Start Menu/Buttons/Start-Button.png")
        if pressed[1]:
            self.menu_create("Resources/Interface/Start Menu/Buttons/Load-Button-Pressed.png")
        else:
            self.menu_create("Resources/Interface/Start Menu/Buttons/Load-Button.png")
        if pressed[2]:
            self.menu_create("Resources/Interface/Start Menu/Buttons/Settings-Button-Pressed.png")
        else:
            self.menu_create("Resources/Interface/Start Menu/Buttons/Settings-Button.png")
        if pressed[3]:
            self.menu_create("Resources/Interface/Start Menu/Buttons/Exit-Button-Pressed.png")
        else:
            self.menu_create("Resources/Interface/Start Menu/Buttons/Exit-Button.png")
        buttonCheck=0

    def keyListener(self):
        global pressed
        P = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()

        # Player input is processed at the beginning
        events = pygame.event.get()
        for e in events:
            if e.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)
            if e.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if x >= self.buttonXY[0][0] and x <= self.buttonXY[0][0]+ 200 and y >= self.buttonXY[0][1] and y <= self.buttonXY[0][1]+50:
                    pressed[0]=True
                if x >= self.buttonXY[1][0] and x <= self.buttonXY[1][0] + 200 and y >= self.buttonXY[1][1] and y <= self.buttonXY[1][1] + 50:
                    pressed[1]=True
                    print(characters.load())
                if x >= self.buttonXY[2][0] and x <= self.buttonXY[2][0] + 200 and y >= self.buttonXY[2][1] and y <= self.buttonXY[2][1] + 50:
                    pressed[2]=True
                if x >= self.buttonXY[3][0] and x <= self.buttonXY[3][0] + 200 and y >= self.buttonXY[3][1]and y <= self.buttonXY[3][1] + 50:
                    pressed[3]=True
                    pygame.quit()
                    sys.exit(0)
            if e.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                if x >= self.buttonXY[0][0] and x <= self.buttonXY[0][0]+ 200 and y >= self.buttonXY[0][1] and y <= self.buttonXY[0][1]+50:
                    self.running = False
                    print("Start button pressed")
                if x >= self.buttonXY[1][0] and x <= self.buttonXY[1][0] + 200 and y >= self.buttonXY[1][1] and y <= self.buttonXY[1][1] + 50:
                    print(characters.load())
                if x >= self.buttonXY[2][0] and x <= self.buttonXY[2][0] + 200 and y >= self.buttonXY[2][1] and y <= self.buttonXY[2][1] + 50:
                    print("Settings button pressed")
                if x >= self.buttonXY[3][0] and x <= self.buttonXY[3][0] + 200 and y >= self.buttonXY[3][1]and y <= self.buttonXY[3][1] + 50:
                    print("Exit button pressed")
                    pygame.quit()
                    sys.exit(0)
                tempCount=0
                for boo in pressed:
                    pressed[tempCount]=False
                    tempCount+=1
                    
    # Main loop. Continues until it's time to move on
    def run(self):
        while self.running:
            case = None
            self.menuAnimation()

            self.keyListener()
            pygame.display.update()
            self.clock.tick(60)

    # Loop until the game ends
    def play(self):
        while self.running:
            self.run()
