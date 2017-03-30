import math
import os
import sys

import pygame
from pygame.locals import *

# Find the distance between two points. Yay, Algebra.
def dist(st, en):
    O = en[1] - st[1]
    A = en[0] - st[0]
    return math.sqrt(O*O + A*A)

# Find the angle of the vector between st and en. 0 degrees is directly
# to the right. 90 degrees is straight up.
def angle(st, en):
    x = -(st[0] - en[0])
    y = st[1] - en[1]
    R = dist(st, en)
    theta = 0
    if x > 0 and y <= 0:
        theta = math.atan(y/x)
    if x > 0 and y > 0:
        theta = math.atan(y/x) + 2*math.pi
    if x < 0:
        theta = math.atan(y/x) + math.pi
    if x == 0 and y > 0:
        theta = math.pi / 2
    if x == 0 and y < 0:
        theta = math.pi * 3 / 2
    return math.degrees(theta)%360

# Takes an indefinite number of strings and creates an absolute file name
# reference.
def filename(*paths):
    pathway = os.path.abspath(os.path.dirname(__file__))
    pathway = os.path.normpath(os.path.join(pathway, ".."))
    for x in paths:
        pathway = os.path.normpath(os.path.join( pathway, str(x) ))
    return pathway

# Get the game's font. There are a few fonts we would really like to use,
# but Pygame has a default one if everything goes badly.
def get_font(sz):
    f = None
    
    # Here are the 3 fonts we would like to use. We want sans serif fonts
    # for this game.
    try:
        n = pygame.font.match_font("dejavusans,bitstreamverasans,arial")
        #n = pygame.font.match_font("bitstreamverasans") #DEBUG LINE
        #n = pygame.font.match_font("arial") #DEBUG LINE
        f = pygame.font.Font( n, sz )
    except:
        f = None
    
    # This is our last try. We must be sure that we can get a font.
    if f is None:
        f = pygame.font.Font( None, sz )
    
    return f

# Returns a wordwrapped list of strings in the given font over a particular
# amount of space.
def wordwrap(words, f, width):
    lines = words.split("\n")
    v = []
    for l in lines:
        st = 0
        en = len(l)
        while st < en:
            if f.size(l[st:en])[0] < width:
                v.append(l[st:en])
                st = en+1
                en = len(l)
            else:
                en = l.rfind(" ",st,en)
        if l[st:].strip() != "":
            v.append(l[st:])
    if v == []: v = [""]
    return v

# This gets a filename in the player's savedata directory.
def savefile(name):
    savepath = os.path.expanduser('~')
    if savepath == '~': savepath = filename( ".anachronist" )
    else:               savepath = os.path.join( savepath, ".anachronist" )
    
    if not os.path.exists( savepath ):
        os.makedirs( savepath )
    
    return os.path.join( savepath, name )

# This is a two-dimensional growth function. The 'rate' is the speed at which
# the function reaches 1, and the 'value' is the progress to 1. This function
# returns a float between 0 and 1 than can be scaled to the desired result.
# This is the same math used to do the grayscale colorization in gfx.py.
# Both values should be between 0 and 1.
def growth(rate, value):
    if rate <= 0 or value <= 0: return 0
    if rate >= 1 or value >= 1: return 1
    
    q = 1.5-rate
    if rate > .5:
        q = .5/rate
    return math.pow(value,q)
