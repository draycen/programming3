

from OpenGL.GL import *
import numpy as np
import math
from SlowCube import SlowCube

_lightVector = np.asfarray([0,0,1,0])

class OBlock(SlowCube):
    def __init__(self):
        super().__init__()
        self.verts = np.asfarray([(  2, -1, -2),
                                  (  2,  1, -2),
                                  ( -2,  1, -2),
                                  ( -2, -1, -2),
                                  (  2, -1,  2),
                                  (  2,  1,  2),
                                  ( -2, -1,  2),
                                  ( -2,  1,  2)])
        self.color = np.asfarray([1,1,0])
        

    def Update(self, deltaTime):
        super().Update(deltaTime)

    def _DrawBlock(self):
        super()._DrawBlock()

    def Render(self):
        super().Render()

class IBlock(SlowCube):
    def __init__(self):
        super().__init__()
        self.verts = np.asfarray([(  4, -1,-1),
                                  (  4,  1,-1),
                                  ( -4,  1,-1),
                                  ( -4, -1,-1),
                                  (  4, -1, 1),
                                  (  4,  1, 1),
                                  ( -4, -1, 1),
                                  ( -4,  1, 1)])
                                  
        self.color = np.asfarray([173/255, 216/255, 230/255])
        

    def Update(self, deltaTime):
        super().Update(deltaTime)

    def _DrawBlock(self):
        super()._DrawBlock()

    def Render(self):
        super().Render()

class SBlock(SlowCube):
    def __init__(self):
        super().__init__()
        self.verts = np.asfarray([(  3,  0, -1),
                                  (  3,  2, -1),
                                  ( -1,  2, -1),
                                  ( -1,  0, -1),
                                  (  3,  0,  1),
                                  (  3,  2,  1),
                                  ( -1,  0,  1),
                                  ( -1,  2,  1),
                                  (  1, -2, -1),
                                  (  1,  0, -1),
                                  ( -3,  0, -1),
                                  ( -3, -2, -1),
                                  (  1, -2,  1),
                                  (  1,  0,  1),
                                  ( -3, -2,  1),
                                  ( -3,  0,  1)])
        self.surfaces = np.array([(0,1,2,3), 
                                 (3,2,7,6),
                                 (6,7,5,4),
                                 (4,5,1,0),
                                 (1,5,7,2),
                                 (4,0,3,6),
                                 (8,9,10,11), 
                                 (11,10,15,14),
                                 (14,15,13,12),
                                 (12,13,9,8),
                                 (9,13,15,10),
                                 (12,8,11,14)])
        self.normal = np.asfarray([( 0, 0,-1, 0),
                                   (-1, 0, 0, 0),
                                   ( 0, 0, 1, 0),
                                   ( 1, 0, 0, 0),
                                   ( 0, 1, 0, 0),
                                   ( 0,-1, 0, 0),
                                   ( 0, 0,-1, 0),
                                   (-1, 0, 0, 0),
                                   ( 0, 0, 1, 0),
                                   ( 1, 0, 0, 0),
                                   ( 0, 1, 0, 0),
                                   ( 0,-1, 0, 0)])
        self.color = np.asfarray([0,1,0])
        

    def Update(self, deltaTime):
        super().Update(deltaTime)

    def _DrawBlock(self):
        super()._DrawBlock()

    def Render(self):
        super().Render()

class ZBlock(SlowCube):
    def __init__(self):
        super().__init__()
        self.verts = np.asfarray([(  3,  0, -1),
                                  (  3,  2, -1),
                                  ( -1,  2, -1),
                                  ( -1,  0, -1),
                                  (  3,  0,  1),
                                  (  3,  2,  1),
                                  ( -1,  0,  1),
                                  ( -1,  2,  1),
                                  (  1, -2, -1),
                                  (  1,  0, -1),
                                  ( -3,  0, -1),
                                  ( -3, -2, -1),
                                  (  1, -2,  1),
                                  (  1,  0,  1),
                                  ( -3, -2,  1),
                                  ( -3,  0,  1)])
        self.surfaces = np.array([(0,1,2,3), 
                                 (3,2,7,6),
                                 (6,7,5,4),
                                 (4,5,1,0),
                                 (1,5,7,2),
                                 (4,0,3,6),
                                 (8,9,10,11), 
                                 (11,10,15,14),
                                 (14,15,13,12),
                                 (12,13,9,8),
                                 (9,13,15,10),
                                 (12,8,11,14)])
        self.normal = np.asfarray([( 0, 0,-1, 0),
                                   (-1, 0, 0, 0),
                                   ( 0, 0, 1, 0),
                                   ( 1, 0, 0, 0),
                                   ( 0, 1, 0, 0),
                                   ( 0,-1, 0, 0),
                                   ( 0, 0,-1, 0),
                                   (-1, 0, 0, 0),
                                   ( 0, 0, 1, 0),
                                   ( 1, 0, 0, 0),
                                   ( 0, 1, 0, 0),
                                   ( 0,-1, 0, 0)])
        self.color = np.asfarray([1,0,0])
        

    def Update(self, deltaTime):
        super().Update(deltaTime)

    def _DrawBlock(self):
        super()._DrawBlock()

    def Render(self):
        super().Render()

class LBlock(SlowCube):
    def __init__(self):
        super().__init__()
        self.verts = np.asfarray([(  3, -2, -1),
                                  (  3,  0, -1),
                                  ( -1,  0, -1),
                                  ( -1, -2, -1),
                                  (  3, -2,  1),
                                  (  3,  0,  1),
                                  ( -1, -2,  1),
                                  ( -1,  0,  1),
                                  ( -1, -2, -1), #2
                                  ( -1,  2, -1),
                                  ( -3,  2, -1),
                                  ( -3, -2, -1),
                                  ( -1, -2,  1),
                                  ( -1,  2,  1),
                                  ( -3, -2,  1),
                                  ( -3,  2,  1)
                                  ])
        self.surfaces = np.array([(0,1,2,3), 
                                 (3,2,7,6),
                                 (6,7,5,4),
                                 (4,5,1,0),
                                 (1,5,7,2),
                                 (4,0,3,6),
                                 (8,9,10,11), 
                                 (11,10,15,14),
                                 (14,15,13,12),
                                 (12,13,9,8),
                                 (9,13,15,10),
                                 (12,8,11,14)])
        self.normal = np.asfarray([( 0, 0,-1, 0),
                                   (-1, 0, 0, 0),
                                   ( 0, 0, 1, 0),
                                   ( 1, 0, 0, 0),
                                   ( 0, 1, 0, 0),
                                   ( 0,-1, 0, 0),
                                   ( 0, 0,-1, 0),
                                   (-1, 0, 0, 0),
                                   ( 0, 0, 1, 0),
                                   ( 1, 0, 0, 0),
                                   ( 0, 1, 0, 0),
                                   ( 0,-1, 0, 0)])
        self.color = np.asfarray([1,.5,0])
        

    def Update(self, deltaTime):
        super().Update(deltaTime)

    def _DrawBlock(self):
        super()._DrawBlock()

    def Render(self):
        super().Render()

class JBlock(SlowCube):
    def __init__(self):
        super().__init__()
        self.verts = np.asfarray([(  3, -2, -1),
                                  (  3,  0, -1),
                                  ( -1,  0, -1),
                                  ( -1, -2, -1),
                                  (  3, -2,  1),
                                  (  3,  0,  1),
                                  ( -1, -2,  1),
                                  ( -1,  0,  1),
                                  ( -1, -2, -1), #2
                                  ( -1,  2, -1),
                                  ( -3,  2, -1),
                                  ( -3, -2, -1),
                                  ( -1, -2,  1),
                                  ( -1,  2,  1),
                                  ( -3, -2,  1),
                                  ( -3,  2,  1)
                                  ])
        self.surfaces = np.array([(0,1,2,3), 
                                 (3,2,7,6),
                                 (6,7,5,4),
                                 (4,5,1,0),
                                 (1,5,7,2),
                                 (4,0,3,6),
                                 (8,9,10,11), 
                                 (11,10,15,14),
                                 (14,15,13,12),
                                 (12,13,9,8),
                                 (9,13,15,10),
                                 (12,8,11,14)])
        self.normal = np.asfarray([( 0, 0,-1, 0),
                                   (-1, 0, 0, 0),
                                   ( 0, 0, 1, 0),
                                   ( 1, 0, 0, 0),
                                   ( 0, 1, 0, 0),
                                   ( 0,-1, 0, 0),
                                   ( 0, 0,-1, 0),
                                   (-1, 0, 0, 0),
                                   ( 0, 0, 1, 0),
                                   ( 1, 0, 0, 0),
                                   ( 0, 1, 0, 0),
                                   ( 0,-1, 0, 0)])
        self.color = np.asfarray([0,0,1])
        

    def Update(self, deltaTime):
        super().Update(deltaTime)

    def _DrawBlock(self):
        super()._DrawBlock()

    def Render(self):
        super().Render()

class TBlock(SlowCube):
    def __init__(self):
        super().__init__()
        self.verts = np.asfarray([(  1,  0, -1),
                                  (  1,  2, -1),
                                  ( -1,  2, -1),
                                  ( -1,  0, -1),
                                  (  1,  0,  1),
                                  (  1,  2,  1),
                                  ( -1,  0,  1),
                                  ( -1,  2,  1),
                                  (  3, -2, -1), #2
                                  (  3,  0, -1),
                                  ( -3,  0, -1),
                                  ( -3, -2, -1),
                                  (  3, -2,  1),
                                  (  3,  0,  1),
                                  ( -3, -2,  1),
                                  ( -3,  0,  1)
                                  ])
        self.surfaces = np.array([(0,1,2,3), 
                                 (3,2,7,6),
                                 (6,7,5,4),
                                 (4,5,1,0),
                                 (1,5,7,2),
                                 (4,0,3,6),
                                 (8,9,10,11), 
                                 (11,10,15,14),
                                 (14,15,13,12),
                                 (12,13,9,8),
                                 (9,13,15,10),
                                 (12,8,11,14)])
        self.normal = np.asfarray([( 0, 0,-1, 0),
                                   (-1, 0, 0, 0),
                                   ( 0, 0, 1, 0),
                                   ( 1, 0, 0, 0),
                                   ( 0, 1, 0, 0),
                                   ( 0,-1, 0, 0),
                                   ( 0, 0,-1, 0),
                                   (-1, 0, 0, 0),
                                   ( 0, 0, 1, 0),
                                   ( 1, 0, 0, 0),
                                   ( 0, 1, 0, 0),
                                   ( 0,-1, 0, 0)])
        self.color = np.asfarray([1,0,1])
        

    def Update(self, deltaTime):
        super().Update(deltaTime)

    def _DrawBlock(self):
        super()._DrawBlock()

    def Render(self):
        super().Render()