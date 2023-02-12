from math import *
from ion import *
from kandinsky import *
from time import *


class Vector2:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    @staticmethod
    def Distance(this, position1, position2):
        dist = sqrt((position2.x - position1.x)**2 +
                    (position2.y - position1.y)**2)


class Canvas:
    def __init__(self):
        self.canvases = []

    def loadCanvas(self, canvases):
        self.canvases = canvases

    def drawAllCanvas(self):
        for i in range(len(self.canvases)):
            if self.canvases[i].enabled:
                self.canvases[i].Draw()


class Map:
    def __init__(self):
        self.sprites = []

    def loadMap(self, sprites):
        self.sprites = sprites

    def drawMap(self):
        self.clearMap()
        for i in range(len(self.sprites)):
            self.sprites[i].Draw()

    def clearMap(self):
        fill_rect(0, 0, 320, 240, color(255, 255, 255))


class gameEngine:
    x = 0
    gameObjects = []
    canvases = []
    map = Map()
    canvas = Canvas()

    def __init__(self):
        pass

    def setGameObjects(self, gameObjects):
        gameEngine.gameObjects = gameObjects

    def setCanvases(self, canvases):
        gameEngine.canvases = canvases

    def startGame(self):
        self.mainLoop()

    @staticmethod
    def createGameObject(newGameObject):
        gameEngine.gameObjects.append(newGameObject)
        gameEngine.map.loadMap(gameEngine.gameObjects)
        gameEngine.refreshUi()

    def mainLoop(self):
        self.dispatchAwake()
        self.dispatchStart()
        self.load_map()
        self.load_canvas()
        gameEngine.map.drawMap()
        gameEngine.canvas.drawAllCanvas()
        previousTime = monotonic()
        deltaTime = 0
        while True:
            self.dispatchUpdate()
            self.eventListener()


    def eventListener(self):
        if keydown(KEY_SHIFT):
            self.dispatchEvent("onKeyShiftPressed")
        if keydown(KEY_PLUS):
            self.dispatchEvent("onKeyPlusPressed")
        if keydown(KEY_MINUS):
            self.dispatchEvent("onKeyMinusPressed")
        if keydown(KEY_ZERO):
            self.dispatchEvent("onKeyZeroPressed")
        if keydown(KEY_ONE):
            self.dispatchEvent("onKeyOnePressed")
        if keydown(KEY_TWO):
            self.dispatchEvent("onKeyTwoPressed")
        if keydown(KEY_THREE):
            self.dispatchEvent("onKeyThreePressed")
        if keydown(KEY_FOUR):
            self.dispatchEvent("onKeyFourPressed")

    @staticmethod
    def refreshUi():
      gameEngine.dispatchCleanSprite()
      gameEngine.map.drawMap()
      gameEngine.canvas.drawAllCanvas()

    @staticmethod
    def dispatchCleanSprite() : 
        for object in gameEngine.gameObjects:
            object.CleanSprite()
        for object in gameEngine.canvases:
            object.CleanSprite()

    @staticmethod
    def dispatchAwake():
        for object in gameEngine.gameObjects:
            object.Awake()
        for object in gameEngine.canvases:
            object.Awake()

    @staticmethod
    def dispatchStart():
        for object in gameEngine.gameObjects:
            object.Start()
        for object in gameEngine.canvases:
            object.Start()

    @staticmethod
    def dispatchUpdate():
        for object in gameEngine.gameObjects:
            object.Update()
        for object in gameEngine.canvases:
            object.Update()

    @staticmethod
    def dispatchEvent(event):
        for object in gameEngine.gameObjects:
            function = getattr(object, event)
            function()
        for object in gameEngine.canvases:
            function = getattr(object, event)
            function()

    @staticmethod
    def load_map():
        objects = []
        for object in gameEngine.gameObjects:
            if object.drawable == True:
                objects.append(object)
        gameEngine.map.loadMap(objects)

    @staticmethod
    def load_canvas():
        gameEngine.canvas.loadCanvas(gameEngine.canvases)

    @staticmethod
    def getAllGameObjects():
        return gameEngine.gameObjects

    @staticmethod
    def getObjectsWithTag(tag):
        objects = []
        for object in gameEngine.gameObjects:
            if object.tag == tag:
                objects.append(object)
        return objects

    @staticmethod
    def getObjectWithName(name):
        for object in gameEngine.gameObjects:
            if object.name == name:
                return object
        return None


class gameObject:
    def __init__(self):
        self.tag = "none"
        self.name = "none"
        self.drawable = False

    def Awake(self):
        pass

    def Start(self):
        pass

    def Update(self):
        pass

    def Draw(self):
        pass

    def CleanSprite(self): 
        pass

    def onkeyShiftPressed(self) : 
        pass

    def onKeyPlusPressed(self):
        pass

    def onKeyMinusPressed(self):
        pass

    def onKeyZeroPressed(self):
        pass

    def onKeyOnePressed(self):
        pass

    def onKeyTwoPressed(self):
        pass

    def onKeyThreePressed(self):
        pass

    def onKeyFourPressed(self):
        pass
