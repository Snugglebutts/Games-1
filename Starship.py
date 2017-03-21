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
# Sprite animation step count once it reaches three set topCount to true and go down
topCount = False
an = 0

playerImg = pygame.image.load('Wizard-front-2.png')

pressed=False

# Arrays containing sprite animations; 0 is up, 1 is Down, 2 is left, 3 is right
sprites=[['Wizard-back-1.png','Wizard-back-2.png','Wizard-back-3.png'],['Wizard-front-1.png','Wizard-front-2.png','Wizard-front-3.png'],
         ['Wizard-left-1.png','Wizard-left-2.png','Wizard-left-3.png'],['Wizard-right-1.png','Wizard-right-2.png','Wizard-right-3.png']]

def player(img,x,y):
    playerImg = pygame.image.load(img)
    gameDisplay.blit(playerImg,(x,y))

def animation():
    global lastDir, topCount, an
    global x, y, x_change, y_change, sprites,pressed
    #Checks direction from keypressed and moves count for sprite animation
    if topCount:
        an -= 1
    else:
        an += 1
    if an==2:
        topCount=True
    elif an==0:
        topCount=False
    # Movement for the player
    if x + x_change >= 0 and x + x_change <= display_width - player_width:
            x += x_change
    if y + y_change >= 0 and y + y_change <= display_height - player_height:
        y += y_change

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
        if event.type==pygame.KEYUP:
            pressed=False
    #Draws the sprites based on direction and change in x,y position      
    gameDisplay.fill(white)
    if lastDir == 0:
        player(sprites[2][an],x,y)
        
    elif lastDir == 1:
        player(sprites[0][an],x,y)
        
    elif lastDir == 2:
        player(sprites[3][an],x,y)

    elif lastDir == 3:
        player(sprites[1][an],x,y)
    
    pygame.display.update()
    clock.tick(30)

def game_loop():
    global lastDir, x_change, y_change, pressed

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
                    animation()
                    x_change=0
                if lastDir == 1:
                    y_change = -5
                    animation()
                    y_change=0 

                if lastDir == 2:
                    x_change = 5
                    animation()
                    x_change=0 

                if lastDir == 3:
                    y_change = 5
                    animation()
                    y_change=0 
                        

        

game_loop()
pygame.quit()
quit()





'''
******************************************** NOTES ********************************************
Animation works now, except you cant hold down button and switch directions immediately 
'''
