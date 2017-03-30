#from engine import misc, menu
#from data import jukebox
  
#from engine import character, battle, dialog, game_state, particle
#from data import cTest, story, sAttack
  
#import pygame, sys
#from pygame.locals import *

from Engine import misc, menu

import pygame, sys
from pygame.locals import *

class Game_Window(object):
    def __init__(self):
        pygame.init()
        pygame.key.set_repeat(300,25)

        # Create the window
        self.screen = pygame.display.set_mode((900,600))
        pygame.display.set_caption("Arcane Arena")

        # Load the game's icon
        icon_path = misc.filename("icon.png")
        try: pygame.display.set_icon(pygame.image.load(icon_path))
        except: pass

        # Black out the screen
        self.screen.fill((0,0,0))
        pygame.display.update()

        # A control variable to handle different parts of the run loop
        self.control = 0

    # This method handles everything
    def start(self, *args):

        # Create a game_layer object and play it, make conditional (if we want to skip
        # the main menu or if we go into editor mode)

        game = menu.Menu()
        game.play()
        '''
        c = character.Character( cTest.cTest() )
        b = battle.Battle()
        b.background = pygame.Surface( (800,600) )
        b.background.fill((100,100,0))
        b.tiles = ["tile"]
        b.grid = [[0,-1,-1,0],[0,-1,-1,0],[0,0,0,0],[0,0,-1,0]]
        b.draw_grid()
        c.create(1)
        c.retrieve()
        b.heroes.append(c)
        '''

        s = pygame.Surface((100,100))
        s.fill((127,0,0))
        s2 = pygame.Surface((100,100))
        s2.fill((127,0,127))
        '''
        p = particle.Particle(["test"], 500, 200, 400)
        p.animspeed = .1
        p.loop = True
        p.dx = .8
        p.particles.append( p )
        b.next_turn()
        b.speak(c, "Testing is fun to do. You should really try it sometime.")
        b.osds.append(dialog.Text((10,10,100,0), "Demo...", None, 0))
        b.play
        '''

        # Now we just blank out the screen for effect.
        self.screen.fill((0,0,0))
        pygame.display.update()

def main():
    print(" ")
    print("Arcane Arena")
    the_game = Game_Window()
    the_game.start(*sys.argv)
    pygame.quit()

main()
