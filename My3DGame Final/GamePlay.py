
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
    global newBlock
    global score
    global _block
    global _nextBlock
    global _fallingSpeed
    #_cube = Cube.Cube(np.asfarray([-1,7,-1]))
    stopGen = False
    pause = False 
    score = 0
    newBlock = np.array([])
    
    tetrisBlocks=[JBlock, LBlock, SBlock, ZBlock, TBlock]
    

def ProcessEvent(event):
    global newBlock
    global currentBlock
    global pause
    if event.type == pygame.KEYDOWN:
        if not pause:
            if event.key == pygame.K_a:
                currentBlock.Rotate(90,2)
            elif event.key == pygame.K_s:
                currentBlock.Rotate(90,0)
            elif event.key == pygame.K_d:
                currentBlock.Rotate(90,1)
            elif event.key == pygame.K_UP:
                currentBlock.Translate(0,0,-2)
            elif event.key == pygame.K_DOWN:
                currentBlock.Translate(0,0,2)
            elif event.key == pygame.K_LEFT:
                currentBlock.Translate(-2,0,0)
            elif event.key == pygame.K_RIGHT:
                currentBlock.Translate(2,0,0)
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
    global currentBlock
    
    if pause:
        return

    if stopGen == False:
        blocks = random.randint(0,4)
        currentBlock = tetrisBlocks[blocks](np.asfarray([-1,7,-1]))
        newBlock = np.append(newBlock, currentBlock)
        print("Next:" + currentBlock.name)
        Nextblock = UI.GetElementByName("nextblock")
        Nextblock.text = currentBlock.name

        stopGen = True
        destroyCube = []
        

    move = np.asfarray([0, -1*deltaTime*10, 0])
    if move[1] + currentBlock.GetPos()[1] <= -6:
        #move[1] += 12
        stopGen = False

    currentBlock.Update(deltaTime, move)

def Render():
    global newBlock
    if not pause:
        for i in newBlock:
            i.Render()
        