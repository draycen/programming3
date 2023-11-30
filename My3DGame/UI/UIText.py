
from turtle import screensize
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from UI.UIImage import UIImage
from pygame.locals import *
import numpy as np
from freetype import *

class UIText():
    def __init__(self, text = "", x = 0, y = 750, align = "left", sizefont = 24, valign = "top", xoffset = 0, yoffset = 0, visible = True, font = 'TimesNewRoman', size = 0):
        self.text = text
        # origin in bottom left
        self.align = align
        self.valign = valign
        self.x = x
        self.y = y
        self.xoffset = xoffset
        self.yoffset = yoffset
        self.visible = visible
        self.font = pygame.font.SysFont(font, sizefont)
        self.color = (255, 255, 255)
        self.textSurface = self.font.render(self.text, True, self.color, None)
        self.width = self.textSurface.get_width()
        self.height = self.textSurface.get_height()
        
        if self.align == "left":
            self.x = 0 + xoffset
        elif self.align == "center":
            self.x = 640//2-self.width//2 + xoffset
        elif self.align == "right":
            self.x = 640 - self.width + xoffset
        if self.valign == "top":
            self.y = 750 - self.height + yoffset
        elif self.valign == "center":
            self.y = 750//2-self.height//2 + yoffset
        elif self.valign == "bottom":
            self.y = 0 + yoffset
        self.textData = pygame.image.tostring(self.textSurface, "RGBA", True)
        
    def _DrawText(self):
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glDrawPixels(self.width, self.height, GL_RGBA, GL_UNSIGNED_BYTE, self.textData)

    def Update(self, deltaTime):
        self.textSurface = self.font.render(self.text, True, self.color, None)
        self.width = self.textSurface.get_width()
        self.height = self.textSurface.get_height()
        if self.align == "left":
            self.x = 0 + self.xoffset
        elif self.align == "center":
            self.x = 640//2-self.width//2 + self.xoffset
        elif self.align == "right":
            self.x = 640 - self.width + self.xoffset
        if self.valign == "top":
            self.y = 750 - self.height + self.yoffset
        elif self.valign == "center":
            self.y = 750//2-self.height//2 + self.yoffset
        elif self.valign == "bottom":
            self.y = 0 + self.yoffset
        self.textData = pygame.image.tostring(self.textSurface, "RGBA", True)
        
    def Render(self):
        glWindowPos2d(self.x, self.y)
        if self.visible:
            self._DrawText()

    