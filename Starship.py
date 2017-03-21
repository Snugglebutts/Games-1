import pygame

pygame.init()

display_width = 1200
display_height = 800
player_height = 32
player_width = 32

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('StarShooter')
clock = pygame.time.Clock()

#value for player position
x = (display_width * 0.45)
y = (display_height * 0.8)

#value for speed/direction
x_change = 0
y_change = 0

lastDir = 3 # 0 = left, 1 = up, 2 = right, 3 = down
# Sprite animation steps, 3 per direction; Top is for 1,2,3,2,1 cycle; detect if 3 or 1
leftAn = 0
leftTop = False
rightAn = 0
rightTop = False
upAn = 0
upTop = False
downAn = 0
downTop = False

playerImg = pygame.image.load('Wizard-front-2.png')

pressed=False

# Arrays containing sprite animations; 0 is up, 1 is Down, 2 is left, 3 is right
sprites=[['Wizard-back-1.png','Wizard-back-2.png','Wizard-back-3.png'],['Wizard-front-1.png','Wizard-front-2.png','Wizard-front-3.png'],
         ['Wizard-left-1.png','Wizard-left-2.png','Wizard-left-3.png'],['Wizard-right-1.png','Wizard-right-2.png','Wizard-right-3.png']]

def player(img,x,y):
    playerImg = pygame.image.load(img)
    gameDisplay.blit(playerImg,(x,y))

def animation():
    global lastDir, downTop, upTop, rightTop, leftTop, downAn, upAn, rightAn, leftAn
    global x, y, x_change, y_change, sprites,pressed
    #Checks direction from keypressed and moves count for sprite animation
    if lastDir == 0:
        if leftTop:
            leftAn -= 1
        else:
            leftAn += 1

    if lastDir == 2:
        if rightTop:
            rightAn -= 1
        else:
            rightAn += 1
        
    if lastDir == 1:
        if upTop:
            upAn -= 1
        else:
            upAn += 1

    if lastDir == 3:
        if downTop:
            downAn -= 1
        else:
            downAn += 1
    if rightAn == 2:
        rightTop = True
    elif rightAn == 0:
        rightTop = False

    if leftAn == 2:
        leftTop = True
    elif leftAn == 0:
        leftTop = False

    if upAn == 2:
        upTop = True
    elif upAn == 0:
        upTop = False

    if downAn == 2:
        downTop = True
    elif downAn == 0:
        downTop = False
#### Took from line 237
    if x + x_change >= 0 and x + x_change <= display_width - player_width:
            x += x_change
    if y + y_change >= 0 and y + y_change <= display_height - player_height:
        y += y_change
    #check for key up during animation
    for event in pygame.event.get():
        if event.type==pygame.KEYUP:
            pressed=False
    #Draws the sprites based on direction and change in x,y position      
    gameDisplay.fill(white)
    if lastDir == 0:
        player(sprites[2][leftAn],x,y)
        
    elif lastDir == 1:
        player(sprites[0][upAn],x,y)
        
    elif lastDir == 2:
        player(sprites[3][rightAn],x,y)

    elif lastDir == 3:
        player(sprites[1][downAn],x,y)
    
    pygame.display.update()
    clock.tick(30)

def game_loop():
    global lastDir, leftAn, rightAn, upAn, downAn, rightTop, leftTop, upTop, downTop
    global x, y, x_change, y_change, pressed

    # Game close boolean
    gameExit = False
    stepCount = 0

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            

            keys = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pressed=True
                if event.key == pygame.K_UP:
                    pressed=True
                if event.key == pygame.K_RIGHT:
                    pressed=True
                if event.key == pygame.K_DOWN:
                    pressed=True
            while keys[pygame.K_LEFT] and pressed==True:
                x_change = -5
                lastDir = 0
                animation()
                x_change=0                
            while keys[pygame.K_UP]and pressed==True:
                y_change = -5
                lastDir = 1
                animation()
                y_change=0 

            while keys[pygame.K_RIGHT]and pressed==True:
                x_change = 5
                lastDir = 2
                animation()
                x_change=0 

            while keys[pygame.K_DOWN]and pressed==True:
                y_change = 5
                lastDir = 3
                animation()
                y_change=0 
                        
                if event.key == pygame.K_ESCAPE:
                    gameExit = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        

game_loop()
pygame.quit()
quit()





'''
******************************************** NOTES ********************************************
Animation works now, except you cant hold down button and switch directions immediately 
'''
