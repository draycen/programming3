
import numpy as np
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from SlowCube import SlowCube
from TetrisBlock import *
import Cube


pygame.init()
size = width, height = 640, 750 
screen = pygame.display.set_mode(size, DOUBLEBUF|OPENGL)

glMatrixMode(GL_PROJECTION) #making 2d screen looks 3d
gluPerspective(45, (width/height), 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)

glEnable(GL_DEPTH_TEST) #Making the items in order
glDepthFunc(GL_LESS)

glTranslate(0.0, 0.0, -40) 

#Cube.Init()
#cube = Cube()
iBlock = IBlock()
iBlock.Translate(5.0,5.0,0)
jBlock = JBlock()
jBlock.Translate(-5.0,5.0,0)
lBlock = LBlock()
lBlock.Translate(5.0,-5.0,0)
oBlock = OBlock()
oBlock.Translate(-5.0,-5.0,0)
sBlock = SBlock()
sBlock.Translate(10.0,10.0,0)
zBlock = ZBlock()
zBlock.Translate(-10.0,10.0,0)
tBlock = TBlock()
tBlock.Translate(10.0,-10.0,0)
tetrisBlocks=[iBlock, jBlock, lBlock, oBlock, sBlock, zBlock, tBlock]



def Update(deltaTime):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

    #cube.Update(deltaTime)

    for o in tetrisBlocks:
        o.Update(deltaTime)


    return True

def Render():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    #cube.Render()
    for o in tetrisBlocks:
        o.Render()

    pygame.display.flip()

_gTickLastFrame = pygame.time.get_ticks()
_gDeltaTime = 0.0
while Update(_gDeltaTime):
    Render()
    t = pygame.time.get_ticks()
    _gDeltaTime = (t - _gTickLastFrame) /1000.0
    _gTickLastFrame = t