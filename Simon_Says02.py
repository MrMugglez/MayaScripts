import maya.cmds as mc

red = "red"
blue = "blue"
green = "green"
yellow = "yellow"

redShader = cmds.shadingNode("blinn", asShader=True)
mc.setAttr((redShader + '.color'), 1.0,0.0,0.0, type='double3')
blueShader = cmds.shadingNode("blinn", asShader=True)
mc.setAttr((blueShader + '.color'), 0.0,0.0,1.0, type='double3')
greenShader = cmds.shadingNode("blinn", asShader=True)
mc.setAttr((greenShader + '.color'), 0.0,1.0,0.0, type='double3')
yellowShader = cmds.shadingNode("blinn", asShader=True)
mc.setAttr((yellowShader + '.color'), 1.0,1.0,0.0, type='double3')

w_Simon = mc.window()
mc.columnLayout()
mc.button(l="Start",c="SetupGame()")
mc.button(l="Close",c="close()")
mc.showWindow()

def SetupGame():
    mc.sphere(n=red)
    mc.sphere(n=blue)
    mc.sphere(n=green)
    mc.sphere(n=yellow)
    mc.setAttr('red.translateY', 5)
    mc.setAttr('blue.translateY', -5)
    mc.setAttr('green.translateX', 5)
    mc.setAttr('yellow.translateX', -5)
    
    mc.select(red)
    mc.hyperShade(a=redShader)
    mc.select(blue)
    mc.hyperShade(a=blueShader)
    mc.select(green)
    mc.hyperShade(a=greenShader)
    mc.select(yellow)
    mc.hyperShade(a=yellowShader)
    start_game()


def start_game():
    game = Game()
    print(game.update())
    mc.select(blue)


def close():
    if mc.objExists(red):
        mc.delete(red)
    if mc.objExists(blue):
        mc.delete(blue)
    if mc.objExists(green):
        mc.delete(green)
    if mc.objExists(yellow):
        mc.delete(yellow)
    mc.deleteUI(w_Simon)


class Game:
    def __init__(self, running):
        self.running = running
        print("Updating")
        
    def update(self, func = lambda x : x*2 (4)):
        while self.running:
            yield self.func()
