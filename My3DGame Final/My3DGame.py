
import numpy as np
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from SlowCube import SlowCube
from TetrisBlock import *
import Cube
import Border
import GamePlay
import UI.UI as UI
import sys


pygame.init()
UI.Init()
size = width, height = 640, 750 
screen = pygame.display.set_mode(size, DOUBLEBUF|OPENGL)

glMatrixMode(GL_PROJECTION) #making 2d screen looks 3d
gluPerspective(45, (width/height), 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)

glEnable(GL_DEPTH_TEST) #Making the items in order
glDepthFunc(GL_LESS)

glTranslate(1.0, 0.0, -40)
glRotate(-15,0,1,0)
glRotate(30,1,0,0)

Cube.Init()
GamePlay.Init()



def Update(deltaTime):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if GamePlay.ProcessEvent(event):
            continue

    GamePlay.Update(deltaTime)

    #for o in tetrisBlocks:
    #    o.Update(deltaTime)
    UI.Update(deltaTime)


    return True

def Render():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    Border.Render()
    GamePlay.Render()
    #for o in tetrisBlocks:
    #    o.Render()
    

    UI.Render()
    pygame.display.flip()

_gTickLastFrame = pygame.time.get_ticks()
_gDeltaTime = 0.0
while Update(_gDeltaTime):
    UI.Render()

    Render()
    t = pygame.time.get_ticks()
    _gDeltaTime = (t - _gTickLastFrame) /1000.0
    _gTickLastFrame = t