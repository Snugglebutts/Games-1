import pygame
import random
import math

pygame.init()

display_width = 1200
display_height = 800
player_height = 32
player_width = 32
pet_width = 37
pet_height = 39

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Arcane Acrobat')
clock = pygame.time.Clock()

#value for player position
x = (display_width * 0.45)
y = (display_height * 0.8)
pet_x = (display_width * 0.45) + 16
pet_y = (display_height * 0.8) + 32
randx=0
randy=0

#value for speed/direction
x_change = 0
y_change = 0

lastDir = 3 # 0 = left, 1 = up, 2 = right, 3 = down
# Sprite animation step count once it reaches three set topCount to true and go down
stepCount = 0
petStepCount = 0
petAn = 0 
an = 0
proLen=160
temp_direction=0
treantIdle=0
treantCount=0
treantImg = pygame.image.load('Treent-front-1.png')
treant_rect = treantImg.get_rect()
playerImg = pygame.image.load('Wizard-front-2.png')
petImg = pygame.image.load('Duck-right-2.png')

pressed=False
doubleKey=False
attack=False
# Arrays containing sprite animations; 0 is up, 1 is Down, 2 is left, 3 is right
sprites=[['Wizard-back-1.png','Wizard-back-2.png','Wizard-back-3.png'],['Wizard-front-1.png','Wizard-front-2.png','Wizard-front-3.png'],
         ['Wizard-left-1.png','Wizard-left-2.png','Wizard-left-3.png'],['Wizard-right-1.png','Wizard-right-2.png','Wizard-right-3.png']]
petSprites=[['Duck-right-1.png','Duck-right-2.png','Duck-right-3.png'],['Duck-left-1.png','Duck-left-2.png','Duck-left-3.png']]
treantSprite=['Treent-front-1.png','Treent-front-2.png']

class Enemy(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image = pygame.image.load(img).convert()
        self.rect = self.image.get_rect()
    def setimg(self,img):
        self.image = pygame.image.load(img).convert()
        self.rect = self.image.get_rect()

all_sprites_list = pygame.sprite.Group()
block_list = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()
projectile_list = pygame.sprite.Group()

treant1 = Enemy('treent-front-1.png')
treant1.rect.x = random.randrange(display_width)
treant1.rect.y = random.randrange(display_height)
block_list.add(treant1)
all_sprites_list.add(treant1)

treant2 = Enemy('treent-front-2.png')
treant2.rect.x = random.randrange(display_width)
treant2.rect.y = random.randrange(display_height)
block_list.add(treant2)
all_sprites_list.add(treant2)

def treant(img):
    global treant_rect, treantImg
    treantImg=pygame.image.load(img)
    gameDisplay.blit(treantImg,(400,350))
    treant_rect = treantImg.get_rect()
    treant_rect.x = 400
    treant_rect.y = 350

def projectile(img,x,y):
    #Input changes from projectile string (file/img) to already loaded image
    # using Pygame.surface
    #projectileImg = pygame.image.load(img)
    gameDisplay.blit(img,(x,y+5))
    
def player(img,x,y):
    playerImg = pygame.image.load(img)
    playerImg = pygame.transform.scale(playerImg,(64,64))
    gameDisplay.blit(playerImg,(x,y))

def pet(img,x,y):
    petImg = pygame.image.load(img)
    #petImg = pygame.transform.scale(petImg,(25,25))
    gameDisplay.blit(petImg,(x,y))

def movement():
    global lastDir, stepCount, an, treantIdle, treantCount, attack, pressed
    global x, y, x_change, y_change, sprites, pressed, doubleKey, petStepCount
    global pet_width, pet_height, pet_x, pet_y, petAn,randx,randy,proLen,temp_direction

    pet_x_change = x_change
    pet_y_change = y_change
    
    if lastDir==0:
        pet_x = x+(pet_width+10)
    elif lastDir==2:
        pet_x = x-(pet_width-16)
    elif lastDir == 1 or lastDir ==3:
        pet_x = x+(player_width/2)
            
    if lastDir==0 or lastDir==2:
        pet_y = y+25
    elif lastDir==1:
        pet_y = y+(pet_height+10)
    elif lastDir==3:
        pet_y = y-(pet_height-16)
    
    #Count for walk animation
    if pressed==True:
        stepCount+=1
        petStepCount+=1
        if stepCount==5:
            an=0
        if stepCount==10:
            an=1
        if stepCount==15:
            an=2
            stepCount=0

        if petStepCount==3:
            petAn=0
        if petStepCount==6:
            petAn=1
        if petStepCount==9:
            petAn=2
            petStepCount=0
            
    # Movement for the player
    if x + x_change >= 0 and x + x_change <= display_width - player_width:
        x += x_change
    if y + y_change >= 0 and y + y_change <= display_height - player_height:
        y += y_change

    if x + x_change >= 0 and x + x_change <= display_width - player_width:
        pet_x += pet_x_change
    if y + y_change >= 0 and y + y_change <= display_height - player_height:
        pet_y += pet_y_change

    #check for key change during animation as well as let go of key
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pressed=True
                lastDir=0
            if event.key == pygame.K_UP:
                pressed=True
                lastDir=1
            if event.key == pygame.K_RIGHT:
                pressed=True
                lastDir=2
            if event.key == pygame.K_DOWN:
                pressed=True
                lastDir = 3
            if event.key == pygame.K_SPACE and not attack:
                    if lastDir==1:
                        randx=x+30
                        randy = y - 25
                    if lastDir==3:
                        randx=x+5
                        randy=y + 25
                    if lastDir==0:
                        randx = x - 25
                        randy = y + 5
                    if lastDir==2:
                        randx=x+25
                        randy = y + 5
                    
                    proLen=0
                    temp_direction=lastDir
                    attack=True
        if event.type==pygame.KEYUP:
            if lastDir==0 and event.key == pygame.K_LEFT:
                pressed=False
            if lastDir==1 and event.key == pygame.K_UP:
                pressed=False
            if lastDir==2 and event.key == pygame.K_RIGHT:
                pressed=False
            if lastDir==3 and event.key == pygame.K_DOWN:
                pressed=False
    treantIdle+=1
    if treantIdle==30:
        treantCount=1
    if treantIdle==60:
        treantCount=0
        treantIdle=0
    draw()
def draw():
    global treant_rect, attack,randx,randy,proLen
    #background
    back = pygame.image.load('Sand-5.png').convert()
    for i in range(math.floor(display_width / 32) + 1):
        for z in range(math.floor(display_height / 32) + 1):
            gameDisplay.blit(back,(i*32,z*32))
    #Draws the sprites based on direction and change in x,y position  
    if y > treant_rect.y:
        treant(treantSprite[treantCount])
    if proLen<150:
        proj = pygame.image.load('Red Projectile Narrow.png')
        if temp_direction==0:
            randx -= 10
            proj = pygame.transform.rotate(proj, 180)
        elif temp_direction==1:
            randy-=10
            proj = pygame.transform.rotate(proj, 90)
        elif temp_direction==2:
            randx+=10
        elif temp_direction==3:
            randy+=10
            proj = pygame.transform.rotate(proj, 270)
        proLen+=5
        
        projectile(proj,randx,randy)
        print("Here")
    else:
        attack=False
        
    if lastDir == 0:
        player(sprites[2][an],x,y)
        pet(petSprites[1][petAn],pet_x,pet_y)
    elif lastDir == 1:
        player(sprites[0][an],x,y)
        pet(petSprites[1][petAn],pet_x,pet_y)
    elif lastDir == 2:
        player(sprites[3][an],x,y)
        pet(petSprites[0][petAn],pet_x,pet_y)

    elif lastDir == 3:
        pet(petSprites[0][petAn],pet_x,pet_y)
        player(sprites[1][an],x,y)

    if y <= treant_rect.y:
        treant(treantSprite[treantCount])
    all_sprites_list.draw(gameDisplay)
    pygame.display.update()
    clock.tick(30)
    
def game_loop():
    global lastDir, x_change, y_change, pressed,treantIdle,attack,treantCount,doubleKey,attack

    # Game close boolean
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            
        #Checks the button press and determines the direction, 0 left, 1 up, 2 right, 3 down
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameExit = True
                if event.key == pygame.K_LEFT:
                    pressed=True
                    lastDir=0
                if event.key == pygame.K_UP:
                    pressed=True
                    lastDir=1
                if event.key == pygame.K_RIGHT:
                    pressed=True
                    lastDir=2
                if event.key == pygame.K_DOWN:
                    pressed=True
                    lastDir = 3
        #use a loop for button pressses, needed for long presses
            while pressed==True:
                if lastDir == 0:
                    x_change = -5
                    movement()
                    x_change=0
                if lastDir == 1:
                    y_change = -5
                    movement()
                    y_change=0 
                if lastDir == 2:
                    x_change = 5
                    movement()
                    x_change=0 
                if lastDir == 3:
                    y_change = 5
                    movement()
                    y_change=0
                
        treantIdle+=1
        if treantIdle==30:
            treantCount=1
        if treantIdle==60:
            treantCount=0
            treantIdle=0
        draw()

game_loop()
pygame.quit()
quit()





'''
******************************************** NOTES ********************************************
Animation works now, except you cant hold down button and switch directions immediately 
'''
