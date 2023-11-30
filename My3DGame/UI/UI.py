
from OpenGL.GL import *
from OpenGL.GLU import *
from UI.UIText import UIText
from UI.UIImage import UIImage
import sys

def GetElementByID(id):
    global _uiIds
    return _uiIds[id]

def GetElementByName(name):
    global _uiNames
    return _uiNames[name]

def Init():
    global _uiObjects
    global _uiNames
    global _uiIds
    _uiObjects = []
    _uiIds = {}
    _uiNames = {}
    #I = UIImage("I.png", align = "right", valign = "center", xoffset= -30, yoffset=-55, visible = False)
    #T = UIImage("T.png", align = "right", valign = "center", xoffset= -30, yoffset=-55, visible = False)
    #S = UIImage("S.png", align = "right", valign = "center", xoffset= -30, yoffset=-55, visible = False)
    #R = UIImage("R.png", align = "right", valign = "center", xoffset= -30, yoffset=-55, visible = False)
    #L = UIImage("L.png", align = "right", valign = "center", xoffset= -30, yoffset=-55, visible = False)
    title = UIText("Hello World", align = "center", yoffset= - 15)
    _uiObjects.append(title)
    _paused = UIText("Game Paused", align = "center", valign = "center", visible = False)
    _uiObjects.append(_paused)


    nextblock = UIText("", size = 32, align = "right", valign = "center", xoffset= -30, yoffset=-60, visible = True)
    _uiNames["nextblock"] = nextblock
    _uiObjects.append(nextblock)

def Update(deltaTime):
    global _uiObjects
    global _paused
    for i in _uiObjects:
        i.Update(deltaTime)

def Render():
    global _uiObjects
    for i in _uiObjects:
        i.Render()

def Cleanup():
    pass

