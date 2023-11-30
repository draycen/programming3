
import pygame
from OpenGL.GL import *
import numpy as np
import math
import Cube
from TetrisBlock import *
import random
import UI.UI as UI

def Init():
    #global _cube
    global tetrisBlocks
    global stopGen
    global pause
    global NewBlock

    #_cube = Cube.Cube(np.asfarray([-1,7,-1]))
    stopGen = False
    pause = False 
    
    
    tetrisBlocks=[JBlock, LBlock, SBlock, ZBlock, TBlock, OBlock, IBlock]
    newBlock=np.array([])
    

def ProcessEvent(event):
    global newBlock
    global pause
    if event.type == pygame.KEYDOWN:
        if not pause:
            if event.key == pygame.K_a:
                newBlock.Rotate(90,2)
            elif event.key == pygame.K_s:
                newBlock.Rotate(90,0)
            elif event.key == pygame.K_d:
                newBlock.Rotate(90,1)
            elif event.key == pygame.K_UP:
                newBlock.Translate(0,0,-2)
            elif event.key == pygame.K_DOWN:
                newBlock.Translate(0,0,2)
            elif event.key == pygame.K_LEFT:
                newBlock.Translate(-2,0,0)
            elif event.key == pygame.K_RIGHT:
                newBlock.Translate(2,0,0)
            elif event.key == pygame.K_ESCAPE:
                pause = not pause
        elif event.key == pygame.K_ESCAPE:
                pause = not pause
            
            

def Update(deltaTime):
    #global _cube
    global tetrisBlocks
    global newBlock
    global stopGen
    global pause
    
    if pause:
        return

    if stopGen == False:
        blocks = random.randint(0,6)
        newBlock = tetrisBlocks[blocks](np.asfarray([-1,7,-1]))
        print("Next:" + newBlock.name)
        Nextblock = UI.GetElementByName("nextblock")
        Nextblock.text = newBlock.name

        stopGen = True


    move = np.asfarray([0, -5*deltaTime, 0])
    if move[1] + newBlock.GetPos()[1] <= -5:
        #move[1] += 12
        stopGen = False

    newBlock.Update(deltaTime, move)

def Render():
    global newBlock
    if not pause:
        
        newBlock.Render()
