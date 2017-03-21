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

playerImg = pygame.image.load('Wizard-front-2.png')

def player(img,x,y):
    playerImg = pygame.image.load(img)
    gameDisplay.blit(playerImg,(x,y))

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    #value for speed/direction
    x_change = 0
    y_change = 0

    lastDir = 0 # 0 = left, 1 = up, 2 = right, 3 = down

    # Sprite animation steps, 3 per direction; Top is for 1,2,3,2,1 cycle; detect if 3 or 1
    leftAn = 0
    leftTop = False
    rightAn = 0
    rightTop = False
    upAn = 0
    upTop = False
    downAn = 0
    downTop = False

    # Arrays containing sprite animations; 'back' is the back of sprite, sprite going up; 'front' is opposite
    upSprites = ['Wizard-back-1.png','Wizard-back-2.png','Wizard-back-3.png']
    downSprites = ['Wizard-front-1.png','Wizard-front-2.png','Wizard-front-3.png']
    leftSprites = ['Wizard-left-1.png','Wizard-left-2.png','Wizard-left-3.png']
    rightSprites = ['Wizard-right-1.png','Wizard-right-2.png','Wizard-right-3.png'] 

    # Game close boolean
    gameExit = False
    stepCount = 0

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            '''
            Checks if player is moving, if so, which direction
              x_change > 0 = right
              x_change < 0 = left
              y_change > 0 = down
              y_change < 0 = up
            '''
            print("X-Change Check: " + str(x_change))
            if x_change > 0:
                if rightTop:
                    rightAn -= 1
                else:
                    rightAn += 1
            elif x_change < 0:
                if leftTop:
                    leftAn -= 1
                else:
                    leftAn += 1
            else:
                if lastDir == 0:
                    leftAn = 1
                elif lastDir == 2:
                    rightAn = 1
                    

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
            
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if x > 0:
                        x_change = -5
                        lastDir = 0
                        
                if event.key == pygame.K_RIGHT:
                    if x < display_width - player_width:
                        x_change = 5
                        lastDir = 2
                        
                if event.key == pygame.K_UP:
                    if y > 0:
                        y_change = -5
                        lastDir = 1
                        
                if event.key == pygame.K_DOWN:
                    if y < display_height - player_height:
                        y_change = 5
                        lastDir = 3
                        
                if event.key == pygame.K_ESCAPE:
                    gameExit = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

#        if x >= display_width - player_width or x <= 0:
#            x_change = 0
#        if y > display_height - player_height or y < 0:
#            y_change = 0

        print("X: " + str(x) + "; x_change: " + str(x_change))
        tempx = x
        tempy = y
        if x + x_change >= 0 and x + x_change <= display_width - player_width:
            x += x_change
        if y + y_change >= 0 and y + y_change <= display_height - player_height:
            y += y_change

        gameDisplay.fill(white)
        if lastDir == 0:
            print(downAn)
            player(leftSprites[leftAn],x,y)
            
        elif lastDir == 1:
            print(upAn)
            player(upSprites[upAn],x,y)
            
        elif lastDir == 2:
            print(rightAn)
            player(rightSprites[rightAn],x,y)

        elif lastDir == 3:
            print(upAn)
            player(downSprites[downAn],x,y)

        #elif y_change == 0 and x_change == 0:
        #    downAn = 2
        #    player(downSprites[2],x,y)
        
        pygame.display.update()
        clock.tick(20)

game_loop()
pygame.quit()
quit()
    
