
from OpenGL.GL import *
import numpy as np
import math
from OpenGL.GLU import *

_lightVector = np.asfarray([0,0,1,0])

class SlowCube:
    def __init__(self, pos):
        self.verts = np.asfarray([(  1, -1, -1),
                                  (  1,  1, -1),
                                  ( -1,  1, -1),
                                  ( -1, -1, -1),
                                  (  1, -1,  1),
                                  (  1,  1,  1),
                                  ( -1, -1,  1),
                                  ( -1,  1,  1)])
        self.surfaces = np.array([(0,1,2,3), #each parantthesis is making a sided of a cube. Each number corelate to the index of vertics
                                 (3,2,7,6),
                                 (6,7,5,4),
                                 (4,5,1,0),
                                 (1,5,7,2),
                                 (4,0,3,6)])
        self.normal = np.asfarray([( 0, 0,-1, 0),
                                   (-1, 0, 0, 0),
                                   ( 0, 0, 1, 0),
                                   ( 1, 0, 0, 0),
                                   ( 0, 1, 0, 0),
                                   ( 0,-1, 0, 0)])
        self.color = np.asfarray([0,0,1])

        self.ang = [0,0,0]
        self.axis = None
        self.pos = pos
        self.rx = None
        self.ry = None
        self.rz = None
        self.rw = None
        self.stop = False
        

    def SetPos(self,pos):
        self.pos = pos

    def GetPos(self):
        return self.pos

    def CheckPos(self):
        if self.pos[0]>4:
            self.pos = (np.asfarray([4,self.pos[1],self.pos[2]]))
        elif self.pos[0]<-4:
            self.pos = (np.asfarray([-4,self.pos[1],self.pos[2]]))
        if self.pos[1]<-6:
            self.pos = (np.asfarray([self.pos[0],-6,self.pos[2]]))
            self.stop = True
        if self.pos[2]>4:
            self.pos = (np.asfarray([self.pos[0],self.pos[1],4]))
        elif self.pos[2]<-4:
            self.pos = (np.asfarray([self.pos[0],self.pos[1],-4]))

    def Update(self, deltaTime, move):
        if not self.stop:
            self.pos += move
        self.CheckPos()


    def _DrawBlock(self):
        global _lightVector

        m = np.linalg.inv(glGetDouble(GL_MODELVIEW_MATRIX)) #to make sure the light doesn't stay in the same direction
        light = np.matmul(_lightVector, m)

        glBegin(GL_QUADS) #Beggining a draw routine
        for n, surface in enumerate(self.surfaces):
            for vert in surface:
                dotP = np.dot(light, self.normal[n])
                mult = max(min(dotP,1),0)
                glColor3fv(self.color * mult)
                glVertex3fv(self.verts[vert])
        glEnd()

    def Translate(self, tx, ty, tz):
        self.pos += np.asfarray([tx,ty,tz])

    def Rotate(self,ang, di):
        self.ang[di] += ang


    def Render(self):
        #m  = glGetDouble(GL_MODELVIEW_MATRIX)

        glPushMatrix()
        glTranslatef(*self.pos) # the star act as this (self.ang, self.axis[0], self.axis[1], self.axis[2]) 
        glRotatef(self.ang[0], 1, 0, 0)  # Rotate around x-axis
        glRotatef(self.ang[1], 0, 1, 0)  # Rotate around y-axis
        glRotatef(self.ang[2], 0, 0, 1)  # Rotate around z-axis
        self._DrawBlock()
        glPopMatrix()

        #glLoadMatrixf(m) #restoring the matrix so that the translation/scling only affects this object.