import math
import sys
import random

import pygame
from pygame.locals import *
from Engine import misc

# The Main Menu object. Accepts no parameters to its constructor
class Menu(object):
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.get_surface()

        self.resourceFilepath = "Resources/Interface/Start Menu/Background/"
        self.backgroundImg1 = pygame.image.load(self.resourceFilepath + "Background-sky.png").convert()
        self.backgroundImg1 = pygame.transform.scale(self.backgroundImg1, (self.screen.get_size()))
        self.backgroundImg2 = pygame.image.load(self.resourceFilepath + "Wizard-Tower.png")
        self.backgroundImg2 = pygame.transform.scale(self.backgroundImg2,
                                                   (int(self.backgroundImg2.get_width() * .5),
                                                    int(self.backgroundImg2.get_height() * .5)))
        
        self.background = pygame.display.get_surface()
        
        self.midground = pygame.display.get_surface()
        self.midgroundImg = pygame.image.load(self.resourceFilepath + "Background-Trees+grass.png")
        self.midgroundImg = pygame.transform.scale(self.midgroundImg, (self.screen.get_size()))       

        self.foregroundImg = pygame.image.load(self.resourceFilepath + "Foreground-Clouds.png")
        self.foregroundImg = pygame.transform.scale(self.foregroundImg, (self.screen.get_size()))
        self.foregroundImg2 = self.foregroundImg
        self.foregroundImg3 = self.foregroundImg
        self.foreground = pygame.display.get_surface()
        self.cloudx = 0

        self.startButton = pygame.image.load("Resources/Interface/Start Menu/Buttons/Start-Button.png").convert_alpha()
        self.startButtonX = int(self.screen.get_width() / 2) - 100
        self.startButtonY = int(self.screen.get_height() / 3) - 25
        self.startButtonWidth = self.startButton.get_width()
        self.startButtonHeight = self.startButton.get_height()
        self.startButtonRect = pygame.Rect(self.startButtonX, self.startButtonY, self.startButtonWidth, self.startButtonHeight)

        self.loadButton = pygame.image.load("Resources/Interface/Start Menu/Buttons/Load-Button.png").convert_alpha()
        self.loadButtonX = int(self.screen.get_width() / 2) - 100
        self.loadButtonY = int(self.screen.get_height() / 3) + 50
        self.loadButtonWidth = self.loadButton.get_width()
        self.loadButtonHeight = self.startButton.get_height()
        self.loadButtonRect = pygame.Rect(self.loadButtonX, self.loadButtonY, self.loadButtonWidth, self.loadButtonHeight)

        self.settingsButton = pygame.image.load("Resources/Interface/Start Menu/Buttons/Settings-Button.png").convert_alpha()
        self.settingsButtonX = int(self.screen.get_width() / 2) - 100
        self.settingsButtonY = int(self.screen.get_height() / 3) + 125
        self.settingsButtonWidth = self.settingsButton.get_width()
        self.settingsButtonHeight = self.settingsButton.get_height()
        self.settingsButtonRect = pygame.Rect(self.settingsButtonX, self.settingsButtonY, self.settingsButtonWidth, self.settingsButtonHeight)

        self.exitButton = pygame.image.load("Resources/Interface/Start Menu/Buttons/Exit-Button.png").convert_alpha()
        self.exitButtonX = int(self.screen.get_width() / 2) - 100
        self.exitButtonY = int(self.screen.get_height() / 3) + 200
        self.exitButtonWidth = self.settingsButton.get_width()
        self.exitButtonHeight = self.exitButton.get_height()
        self.exitButtonRect = pygame.Rect(self.exitButtonX, self.exitButtonY, self.exitButtonWidth, self.exitButtonHeight)
        
        self.buttons = pygame.display.get_surface()
        self.buttons.blit(self.startButton, (self.startButtonX, self.startButtonY))
        self.buttons.blit(self.loadButton, (self.loadButtonX, self.loadButtonY))
        self.buttons.blit(self.settingsButton, (self.settingsButtonX, self.settingsButtonY))
        self.buttons.blit(self.exitButton, (self.exitButtonX, self.exitButtonY))
        #self.buttons.blit(self.startButton, (int(self.screen.get_width() / 2)-100, int(self.screen.get_height()/3)-25))
        #self.startButtonRect = self.startButton.get_rect()

    def menuAnimation(self):
        self.background.blit(self.backgroundImg1, (0,0))
        self.foreground.blit(self.foregroundImg.convert_alpha(), (self.cloudx, 0))
        self.foreground.blit(self.foregroundImg2.convert_alpha(), (self.cloudx + self.foregroundImg.get_width(), 0))
        self.background.blit(self.backgroundImg2,(self.screen.get_width() * .75, self.screen.get_height() * .20))
        self.midground.blit(self.midgroundImg, (0,0))
        self.buttons.blit(self.startButton, (self.startButtonRect.x, self.startButtonRect.y))
        self.buttons.blit(self.loadButton, (self.loadButtonX, self.loadButtonY))
        self.buttons.blit(self.settingsButton, (self.settingsButtonX, self.settingsButtonY))
        self.buttons.blit(self.exitButton, (self.exitButtonX, self.exitButtonY))
        #self.buttons.blit(self.startButton, (self.startButtonRect.x, self.startButtonRect.y))
        self.cloudx -= 0.5

        if self.cloudx < 0 - self.foregroundImg.get_width():
            self.cloudx = 0

    def keyListener(self):
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
                if x >= self.startButtonRect.x and x <= self.startButtonRect.x + 200 and y >= self.startButtonRect.y and y <= self.startButtonRect.y + 50:
                    print("Start button pressed")
                if x >= self.loadButtonRect.x and x <= self.loadButtonRect.x + 200 and y >= self.loadButtonRect.y and y <= self.loadButtonRect.y + 50:
                    print("Load button pressed")
                if x >= self.settingsButtonRect.x and x <= self.settingsButtonRect.x + 200 and y >= self.settingsButtonRect.y and y <= self.settingsButtonRect.y + 50:
                    print("Settings button pressed")
                if x >= self.exitButtonRect.x and x <= self.exitButtonRect.x + 200 and y >= self.exitButtonRect.y and y <= self.exitButtonRect.y + 50:
                    print("Exit button pressed")
                    pygame.quit()
                    sys.exit(0)
                    
                
                print("Pos: " + str(x) + "," + str(y))
                
                # RETURNS COORDINATES OF MOUSE PRESS
                # NEED TO CREATE A MENU FOR PLAYER TO CHOOSE
                # If P == [newGameButtonX, NewGameButtonY]:
                #       newGame = True
                
    # Main loop. Continues until it's time to move on
    def run(self):
        case = None
        self.keyListener()

        # Clears screen to show next step in animation
        self.screen.fill((0,0,0))

        #self.background.blit(self.backgroundImg1, (0,0))
        #self.background.blit(self.backgroundImg2,(self.screen.get_width() * .75, self.screen.get_height() * .20))
        #self.midground.blit(self.midgroundImg, (0,0))
        self.menuAnimation()
        #self.buttons.blit(self.startButton, (int(self.screen.get_width() / 2)-100, int(self.screen.get_height()/3)-25))
        pygame.display.update()
        self.clock.tick(60)

    # Loop until the game ends
    def play(self):
        while self.running:
            self.run()
