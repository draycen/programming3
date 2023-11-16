
from OpenGL.GL import *
from OpenGL.GLU import *
from UI.UIText import UIText
from UI.UIImage import UIImage

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
    title = UIText("Hello World", align = "center", yoffset= - 15)
    
    _uiObjects.append(title)

def Update(deltaTime):
    global _uiObjects
    for i in _uiObjects:
        i.Update(deltaTime)

def Render():
    global _uiObjects
    for i in _uiObjects:
        i.Render()

def Cleanup():
    pass

