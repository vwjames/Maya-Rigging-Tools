import maya.cmds as cmds
import Rigging_Functions as vfunctions

uiColour = [0.4, 0.42, 0.45]
uiOutlineColour = [0.33, 0.33, 0.33]
mainButtonColour = [0.25, 0.25, 0.25]

def switch(buttonOn, buttonOff):
    if cmds.button(buttonOn, query = True, m = True):
        cmds.button(buttonOn, edit = True, m = False)
        cmds.button(buttonOff, edit = True, m = True)
    else:
        cmds.button(buttonOff, edit = True, m = False)
        cmds.button(buttonOn, edit = True, m = True)

def switchAll(buttonOn, buttonOff, XbuttonOn, XbuttonOff, YbuttonOn, YbuttonOff, ZbuttonOn, ZbuttonOff):
    if cmds.button(buttonOn, query = True, m = True):
        cmds.button(buttonOn, edit = True, m = False)
        cmds.button(buttonOff, edit = True, m = True)
        cmds.button(XbuttonOn, edit = True, m = False)
        cmds.button(XbuttonOff, edit = True, m = True)
        cmds.button(YbuttonOn, edit = True, m = False)
        cmds.button(YbuttonOff, edit = True, m = True)
        cmds.button(ZbuttonOn, edit = True, m = False)
        cmds.button(ZbuttonOff, edit = True, m = True)
    else:
        cmds.button(buttonOff, edit = True, m = False)
        cmds.button(buttonOn, edit = True, m = True)
        cmds.button(XbuttonOff, edit = True, m = False)
        cmds.button(XbuttonOn, edit = True, m = True)
        cmds.button(YbuttonOff, edit = True, m = False)
        cmds.button(YbuttonOn, edit = True, m = True)
        cmds.button(ZbuttonOff, edit = True, m = False)
        cmds.button(ZbuttonOn, edit = True, m = True)

def colourSwitch(customColourInput, customColour):
    colors = cmds.colorInputWidgetGrp(customColourInput, query=True, rgb=True)

    cmds.button(customColour, edit = True, backgroundColor = (colors[0], colors[1], colors[2]))
    return colors

# Make a new window
#
windowName = "RiggingShortcuts"
if cmds.window(windowName, exists=True):
    cmds.deleteUI(windowName)
    cmds.windowPref(windowName, removeAll=True)

riggingWindow = cmds.window(windowName, title="Rigging shortcuts", iconName='Short Name', widthHeight=(450, 1000))
cmds.columnLayout(adjustableColumn=True, cal="center")
#1
cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[(1, 240), (2, 225)])
#2
cmds.columnLayout()
#3
cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[(1, 10), (2, 205), (3, 10)], bgc = (0.2, 0.2, 0.2))
#4 +
cmds.columnLayout( h = 10, bgc = (0.2, 0.2, 0.2))
#5 +
cmds.setParent('..')
#5 -
cmds.button(label='Space', command=('vfunctions.space()'), width=100, h = 45)
cmds.columnLayout( h = 10, bgc = (uiColour[0], uiColour[1], uiColour[2]))
#5 +
cmds.setParent('..')
#5 -
cmds.setParent('..')
#4 -

cmds.frameLayout(label = "Controls", bgc = (uiColour[0], uiColour[1], uiColour[2]), lw = 200)
# 4 +
cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[(1, 5), (2, 225), (3, 5)], bgc = (uiColour[0], uiColour[1], uiColour[2]))
#5 +
cmds.columnLayout(w = 5, bgc = (uiColour[0], uiColour[1], uiColour[2]))
#6 +
cmds.setParent('..')
#6 -
cmds.columnLayout(w = 225, bgc = (uiColour[0], uiColour[1], uiColour[2]))
#6 +
cmds.columnLayout(h = 5, bgc = (uiColour[0], uiColour[1], uiColour[2]))
#7 +
cmds.setParent('..')
#7-

cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[(1, 2), (2, 218), (3, 2)], bgc = (uiOutlineColour[0], uiOutlineColour[1], uiOutlineColour[2]))
#7 +
cmds.columnLayout(w = 2, bgc = (uiOutlineColour[0], uiOutlineColour[1], uiOutlineColour[2]))
#8+
cmds.setParent('..')
#8 -
cmds.columnLayout(w = 218)
#8+
cmds.columnLayout(h = 2, bgc = (uiOutlineColour[0], uiOutlineColour[1], uiOutlineColour[2]))
#9 +
cmds.setParent('..')
#9 -


cmds.gridLayout(numberOfColumns=5, cellWidthHeight=(43, 43))
# 9 +
cmds.button(label='Circle', command=('vfunctions.circleCtrl(cmds.checkBox(customName, query = True, value = True), cmds.textField(name, query = True, tx= True), cmds.textField(suffix, query = True, tx= True), cmds.checkBox(autoParent, query = True, value = True))'), bgc = (mainButtonColour[0], mainButtonColour[1], mainButtonColour[2]))
cmds.button(label='Locator', command=('vfunctions.locCtrl(cmds.checkBox(customName, query = True, value = True), cmds.textField(name, query = True, tx= True), cmds.textField(suffix, query = True, tx= True), cmds.checkBox(autoParent, query = True, value = True))'), bgc = (mainButtonColour[0], mainButtonColour[1], mainButtonColour[2]))
cmds.button(label='Square', command=('vfunctions.squareCtrl(cmds.checkBox(customName, query = True, value = True), cmds.textField(name, query = True, tx= True), cmds.textField(suffix, query = True, tx= True), cmds.checkBox(autoParent, query = True, value = True))'), bgc = (mainButtonColour[0], mainButtonColour[1], mainButtonColour[2]))
cmds.button(label='Cube', command=('vfunctions.cubeCtrl(cmds.checkBox(customName, query = True, value = True), cmds.textField(name, query = True, tx= True), cmds.textField(suffix, query = True, tx= True), cmds.checkBox(autoParent, query = True, value = True))'), bgc = (mainButtonColour[0], mainButtonColour[1], mainButtonColour[2]))
cmds.button(label='Sphere', command=('vfunctions.sphereCtrl(cmds.checkBox(customName, query = True, value = True), cmds.textField(name, query = True, tx= True), cmds.textField(suffix, query = True, tx= True), cmds.checkBox(autoParent, query = True, value = True))'), bgc = (mainButtonColour[0], mainButtonColour[1], mainButtonColour[2]))
cmds.button(label='Pill', command=('vfunctions.pillCtrl(cmds.checkBox(customName, query = True, value = True), cmds.textField(name, query = True, tx= True), cmds.textField(suffix, query = True, tx= True), cmds.checkBox(autoParent, query = True, value = True))'), bgc = (mainButtonColour[0], mainButtonColour[1], mainButtonColour[2]))
cmds.button(label='Four \nArrow', command=('vfunctions.fourArrowCtrl(cmds.checkBox(customName, query = True, value = True), cmds.textField(name, query = True, tx= True), cmds.textField(suffix, query = True, tx= True), cmds.checkBox(autoParent, query = True, value = True))'), bgc = (mainButtonColour[0], mainButtonColour[1], mainButtonColour[2]))
cmds.button(label='Two \nArrow', command=('vfunctions.twoArrowCtrl(cmds.checkBox(customName, query = True, value = True), cmds.textField(name, query = True, tx= True), cmds.textField(suffix, query = True, tx= True), cmds.checkBox(autoParent, query = True, value = True))'), bgc = (mainButtonColour[0], mainButtonColour[1], mainButtonColour[2]))
cmds.button(label='Curved \nArrow', command=('vfunctions.curvedArrowCtrl(cmds.checkBox(customName, query = True, value = True), cmds.textField(name, query = True, tx= True), cmds.textField(suffix, query = True, tx= True), cmds.checkBox(autoParent, query = True, value = True))'), bgc = (mainButtonColour[0], mainButtonColour[1], mainButtonColour[2]))
cmds.button(label='Arrow', command=('vfunctions.arrowCtrl(cmds.checkBox(customName, query = True, value = True), cmds.textField(name, query = True, tx= True), cmds.textField(suffix, query = True, tx= True), cmds.checkBox(autoParent, query = True, value = True))'), bgc = (mainButtonColour[0], mainButtonColour[1], mainButtonColour[2]))
cmds.setParent('..')
# 9 -
cmds.columnLayout(h = 2, bgc = (uiOutlineColour[0], uiOutlineColour[1], uiOutlineColour[2]))
# 9 +
cmds.setParent('..')
#9 -
cmds.setParent('..')
#8 -
cmds.columnLayout(w = 2, bgc = (uiOutlineColour[0], uiOutlineColour[1], uiOutlineColour[2]))
# 8 +
cmds.setParent('..')
# 8 -
cmds.setParent('..')
# 7 -
cmds.columnLayout(h = 5, bgc = (uiColour[0], uiColour[1], 0))
# 7 +
cmds.setParent('..')
# 7 -
cmds.columnLayout(w = 5, bgc = (uiColour[0], uiColour[1], uiColour[2]))
# 7 +

cmds.setParent('..')
# 7 -
cmds.setParent('..')
# 6 -
cmds.setParent('..')
# 5 -

cmds.frameLayout(label = "Control settings")

cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[(1, 125), (2, 100)])
cmds.text( label='Custom Name' )
cmds.text( label='Custom Suffix' )

name = cmds.textField()
suffix = cmds.textField()
cmds.setParent('..')
cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[(1, 112.5), (2, 112.5)])
customName = cmds.checkBox(label = "Custom Name")
autoParent = cmds.checkBox(label = "Auto-Parent")

cmds.textField(name, edit=True)
cmds.textField(suffix, edit=True)
cmds.setParent('..')
cmds.setParent('..')

cmds.setParent('..')


cmds.frameLayout(label = "Control Colours")

cmds.gridLayout(numberOfColumns=5, cellWidthHeight=(45, 35))
cmds.button(label='0', command=('vfunctions.colour(0)'), backgroundColor=(0.5, 0.5, 0.5), width=25)
cmds.button(label='1', command=('vfunctions.colour(1)'), backgroundColor=(0, 0, 0), width=25)
cmds.button(label='2', command=('vfunctions.colour(2)'), backgroundColor=(0.25, 0.25, 0.25), width=25)
cmds.button(label='3', command=('vfunctions.colour(3)'), backgroundColor=(0.75, 0.75, 0.75), width=25)
cmds.button(label='4', command=('vfunctions.colour(4)'), backgroundColor=(0.6, 0, 0.15), width=25)
cmds.button(label='5', command=('vfunctions.colour(5)'), backgroundColor=(0, 0, 0.37), width=25)
cmds.button(label='6', command=('vfunctions.colour(6)'), backgroundColor=(0, 0, 1), width=25)
cmds.button(label='7', command=('vfunctions.colour(7)'), backgroundColor=(0, 0.3, 0.1), width=25)
cmds.button(label='8', command=('vfunctions.colour(8)'), backgroundColor=(0.1490196078, 0, 0.262745098), width=25)
cmds.button(label='9', command=('vfunctions.colour(9)'), backgroundColor=(0.7843137255, 0, 0.7843137255), width=25)
cmds.button(label='10', command=('vfunctions.colour(10)'), backgroundColor=(0.537254902, 0.2823529412, 0.2), width=25)
cmds.button(label='11', command=('vfunctions.colour(11)'), backgroundColor=(0.2470588235, 0.137254902, 0.1215686275), width=25)
cmds.button(label='12', command=('vfunctions.colour(12)'), backgroundColor=(0.5960784314, 0.1490196078, 0), width=25)
cmds.button(label='13', command=('vfunctions.colour(13)'), backgroundColor=(1, 0, 0), width=25)
cmds.button(label='14', command=('vfunctions.colour(14)'), backgroundColor=(0, 1, 0.06274509804), width=25)
cmds.button(label='15', command=('vfunctions.colour(15)'), backgroundColor=(0, 0.2549019608, 0.6), width=25)
cmds.button(label='16', command=('vfunctions.colour(16)'), backgroundColor=(1, 1, 1), width=25)
cmds.button(label='17', command=('vfunctions.RGBcolour(1, 1, 0)'), backgroundColor=(1, 1, 0), width=25)
cmds.button(label='18', command=('vfunctions.colour(18)'), backgroundColor=(0.3921568627, 0.862745098, 1), width=25)
cmds.button(label='19', command=('vfunctions.colour(19)'), backgroundColor=(0.262745098, 1, 0.6392156863), width=25)
cmds.button(label='20', command=('vfunctions.colour(20)'), backgroundColor=(1, 0.6901960784, 0.6901960784), width=25)
cmds.button(label='21', command=('vfunctions.colour(21)'), backgroundColor=(0.8901960784, 0.6745098039, 0.4745098039), width=25)
cmds.button(label='22', command=('vfunctions.colour(22)'), backgroundColor=(0.9960784314, 1, 0.5490196078), width=25)
cmds.button(label='23', command=('vfunctions.colour(23)'), backgroundColor=(0, 0.6, 0.3294117647), width=25)
cmds.button(label='24', command=('vfunctions.colour(24)'), backgroundColor=(0.8509803922, 0.568627451, 0.4274509804), width=25)
cmds.button(label='25', command=('vfunctions.colour(25)'), backgroundColor=(0.8784313725, 0.7843137255, 0.3058823529), width=25)
cmds.button(label='26', command=('vfunctions.colour(26)'), backgroundColor=(0.6352941176, 0.8117647059, 0.2784313725), width=25)
cmds.button(label='27', command=('vfunctions.colour(27)'), backgroundColor=(0.231372549, 0.7568627451, 0.5803921569), width=25)
cmds.button(label='28', command=('vfunctions.colour(28)'), backgroundColor=(0.2549019608, 0.8196078431, 0.7254901961), width=25)
cmds.button(label='29', command=('vfunctions.colour(29)'), backgroundColor=(0.2156862745, 0.5843137255, 0.768627451), width=25)
cmds.button(label='30', command=('vfunctions.colour(30)'), backgroundColor=(0.6117647059, 0.4196078431, 0.8078431373), width=25)
cmds.button(label='31', command=('vfunctions.colour(31)'), backgroundColor=(0.8078431373, 0.3490196078, 0.6549019608), width=25)

cmds.setParent('..')
colors = [1.0, 0.0, 0.0]
customColourInput = cmds.colorInputWidgetGrp( label='Custom \nColor', rgb=(1, 0, 0), cw3 = [0, 0, 215], cc= 'colors = colourSwitch(customColourInput, customColour)' )

customColour = cmds.button(label='Custom Colour', command=('vfunctions.RGBcolour(colors[0], colors[1], colors[2])'), backgroundColor=(1, 0, 0), width=100, h = 30)
cmds.setParent('..')
cmds.setParent('..')
cmds.columnLayout()
cmds.frameLayout(label = "Lock")


cmds.gridLayout(numberOfColumns=2, cellWidthHeight=(112.5, 35))

cmds.button(label='Lock Selected', command=('vfunctions.lock(False, cmds.checkBox(lockBool, query = True, value = True), cmds.textField(lockSuffix, query = True, tx= True), cmds.button(TransXButtonOn, query = True, m = True), cmds.button(TransYButtonOn, query = True, m = True), cmds.button(TransZButtonOn, query = True, m = True),cmds.button(RotXButtonOn, query = True, m = True), cmds.button(RotYButtonOn, query = True, m = True), cmds.button(RotZButtonOn, query = True, m = True), cmds.button(ScaleXButtonOn, query = True, m = True), cmds.button(ScaleYButtonOn, query = True, m = True), cmds.button(ScaleZButtonOn, query = True, m = True), cmds.button(VisButtonOn, query = True, m = True))'), width=112.5)
cmds.button(label='Lock All', command=('vfunctions.lock(True, cmds.checkBox(lockBool, query = True, value = True), cmds.textField(lockSuffix, query = True, tx= True), cmds.button(TransXButtonOn, query = True, m = True), cmds.button(TransYButtonOn, query = True, m = True), cmds.button(TransZButtonOn, query = True, m = True),cmds.button(RotXButtonOn, query = True, m = True), cmds.button(RotYButtonOn, query = True, m = True), cmds.button(RotZButtonOn, query = True, m = True), cmds.button(ScaleXButtonOn, query = True, m = True), cmds.button(ScaleYButtonOn, query = True, m = True), cmds.button(ScaleZButtonOn, query = True, m = True), cmds.button(VisButtonOn, query = True, m = True))'), width=112.5)
cmds.button(label='Unlock\n Selected', command=('vfunctions.unlock(False, cmds.checkBox(lockBool, query = True, value = True), cmds.textField(lockSuffix, query = True, tx= True), cmds.button(TransXButtonOn, query = True, m = True), cmds.button(TransYButtonOn, query = True, m = True), cmds.button(TransZButtonOn, query = True, m = True),cmds.button(RotXButtonOn, query = True, m = True), cmds.button(RotYButtonOn, query = True, m = True), cmds.button(RotZButtonOn, query = True, m = True), cmds.button(ScaleXButtonOn, query = True, m = True), cmds.button(ScaleYButtonOn, query = True, m = True), cmds.button(ScaleZButtonOn, query = True, m = True), cmds.button(VisButtonOn, query = True, m = True))'), width=112.5)
cmds.button(label='Unlock All', command=('vfunctions.unlock(True, cmds.checkBox(lockBool, query = True, value = True), cmds.textField(lockSuffix, query = True, tx= True), cmds.button(TransXButtonOn, query = True, m = True), cmds.button(TransYButtonOn, query = True, m = True), cmds.button(TransZButtonOn, query = True, m = True),cmds.button(RotXButtonOn, query = True, m = True), cmds.button(RotYButtonOn, query = True, m = True), cmds.button(RotZButtonOn, query = True, m = True), cmds.button(ScaleXButtonOn, query = True, m = True), cmds.button(ScaleYButtonOn, query = True, m = True), cmds.button(ScaleZButtonOn, query = True, m = True), cmds.button(VisButtonOn, query = True, m = True))'), width=112.5)
cmds.setParent('..')
lockBool = cmds.checkBox(label = "Lock by Suffix")
cmds.text( label='Suffix' )
lockSuffix = cmds.textField()
cmds.textField(lockSuffix, edit=True)

cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[(1, 22.5), (2, 180), (3, 22.5)])
cmds.columnLayout( h = 10)
cmds.setParent('..')

cmds.gridLayout(numberOfColumns=4, cellWidthHeight=(45, 45))

cmds.columnLayout( cal="center", h = 45, w = 45)

TransXButtonOn = cmds.button( label='TransX', command=("switch(TransXButtonOn, TransXButtonOff)"), backgroundColor=(0.7, 0, 0),  h = 45, w = 45)
TransXButtonOff = cmds.button( label='TransX', command=("switch(TransXButtonOn, TransXButtonOff)"), backgroundColor=(0.3, 0.2, 0.2),  h = 45, w = 45, m=False)
cmds.setParent('..')

cmds.columnLayout( cal="center", h = 45, w = 45)
TransYButtonOn = cmds.button( label='TransY', command=("switch(TransYButtonOn, TransYButtonOff)"), backgroundColor=(0, 0.7, 0),  h = 45, w = 45)
TransYButtonOff = cmds.button( label='TransY', command=("switch(TransYButtonOn, TransYButtonOff)"), backgroundColor=(0.2, 0.3, 0.2),  h = 45, w = 45, m=False)
cmds.setParent('..')

cmds.columnLayout(h = 45, w = 45)
TransZButtonOn = cmds.button( label='TransY', command=("switch(TransZButtonOn, TransZButtonOff)"), backgroundColor=(0, 0, 0.7),  h = 45, w = 45)
TransZButtonOff = cmds.button( label='TransY', command=("switch(TransZButtonOn, TransZButtonOff)"), backgroundColor=(0.2, 0.2, 0.3),  h = 45, w = 45, m=False)
cmds.setParent('..')
cmds.columnLayout(h = 45, w = 45)
TransButtonOn = cmds.button( label='Trans', command=("switchAll(TransButtonOn, TransButtonOff, TransXButtonOn, TransXButtonOff, TransYButtonOn, TransYButtonOff, TransZButtonOn, TransZButtonOff)"), backgroundColor=(0.4, 0.4, 0.4),  h = 45, w = 45)
TransButtonOff = cmds.button( label='Trans', command=("switchAll(TransButtonOn, TransButtonOff, TransXButtonOn, TransXButtonOff, TransYButtonOn, TransYButtonOff, TransZButtonOn, TransZButtonOff)"), backgroundColor=(0.2, 0.2, 0.2),  h = 45, w = 45, m=False)
cmds.setParent('..')

cmds.columnLayout(h = 45, w = 45)
RotXButtonOn = cmds.button( label='RotX', command=("switch(RotXButtonOn, RotXButtonOff)"), backgroundColor=(0.7, 0, 0),  h = 45, w = 45)
RotXButtonOff = cmds.button( label='RotX', command=("switch(RotXButtonOn, RotXButtonOff)"), backgroundColor=(0.3, 0.2, 0.2),  h = 45, w = 45, m=False)
cmds.setParent('..')

cmds.columnLayout(h = 45, w = 45)
RotYButtonOn = cmds.button( label='RotY', command=("switch(RotYButtonOn, RotYButtonOff)"), backgroundColor=(0, 0.7, 0),  h = 45, w = 45)
RotYButtonOff = cmds.button( label='RotY', command=("switch(RotYButtonOn, RotYButtonOff)"), backgroundColor=(0.2, 0.3, 0.2),  h = 45, w = 45, m=False)
cmds.setParent('..')

cmds.columnLayout(h = 45, w = 45)
RotZButtonOn = cmds.button( label='RotY', command=("switch(RotZButtonOn, RotZButtonOff)"), backgroundColor=(0, 0, 0.7),  h = 45, w = 45)
RotZButtonOff = cmds.button( label='RotY', command=("switch(RotZButtonOn, RotZButtonOff)"), backgroundColor=(0.2, 0.2, 0.3),  h = 45, w = 45, m=False)
cmds.setParent('..')

cmds.columnLayout(h = 45, w = 45)
RotButtonOn = cmds.button( label='Rot', command=("switchAll(RotButtonOn, RotButtonOff, RotXButtonOn, RotXButtonOff, RotYButtonOn, RotYButtonOff, RotZButtonOn, RotZButtonOff)"), backgroundColor=(0.4, 0.4, 0.4),  h = 45, w = 45)
RotButtonOff = cmds.button( label='Rot', command=("switchAll(RotButtonOn, RotButtonOff, RotXButtonOn, RotXButtonOff, RotYButtonOn, RotYButtonOff, RotZButtonOn, RotZButtonOff)"), backgroundColor=(0.2, 0.2, 0.2),  h = 45, w = 45, m=False)
cmds.setParent('..')

cmds.columnLayout(h = 45, w = 45)
ScaleXButtonOn = cmds.button( label='ScaleX', command=("switch(ScaleXButtonOn, ScaleXButtonOff)"), backgroundColor=(0.7, 0, 0),  h = 45, w = 45)
ScaleXButtonOff = cmds.button( label='ScaleX', command=("switch(ScaleXButtonOn, ScaleXButtonOff)"), backgroundColor=(0.3, 0.2, 0.2),  h = 45, w = 45, m=False)
cmds.setParent('..')

cmds.columnLayout(h = 45, w = 45)
ScaleYButtonOn = cmds.button( label='ScaleY', command=("switch(ScaleYButtonOn, ScaleYButtonOff)"), backgroundColor=(0, 0.7, 0),  h = 45, w = 45)
ScaleYButtonOff = cmds.button( label='ScaleY', command=("switch(ScaleYButtonOn, ScaleYButtonOff)"), backgroundColor=(0.2, 0.3, 0.2),  h = 45, w = 45, m=False)
cmds.setParent('..')

cmds.columnLayout(h = 45, w = 45)
ScaleZButtonOn = cmds.button( label='ScaleY', command=("switch(ScaleZButtonOn, ScaleZButtonOff)"), backgroundColor=(0, 0, 0.7),  h = 45, w = 45)
ScaleZButtonOff = cmds.button( label='ScaleY', command=("switch(ScaleZButtonOn, ScaleZButtonOff)"), backgroundColor=(0.2, 0.2, 0.3),  h = 45, w = 45, m=False)
cmds.setParent('..')

cmds.columnLayout(h = 45, w = 45)
ScaleButtonOn = cmds.button( label='Scale', command=("switchAll(ScaleButtonOn, ScaleButtonOff, ScaleXButtonOn, ScaleXButtonOff, ScaleYButtonOn, ScaleYButtonOff, ScaleZButtonOn, ScaleZButtonOff)"), backgroundColor=(0.4, 0.4, 0.4),  h = 45, w = 45)
ScaleButtonOff = cmds.button( label='Scale', command=("switchAll(ScaleButtonOn, ScaleButtonOff, ScaleXButtonOn, ScaleXButtonOff, ScaleYButtonOn, ScaleYButtonOff, ScaleZButtonOn, ScaleZButtonOff)"), backgroundColor=(0.2, 0.2, 0.2),  h = 45, w = 45, m=False)
cmds.setParent('..')
cmds.setParent('..')
cmds.columnLayout( h = 10)
cmds.setParent('..')
cmds.columnLayout( h = 10)
cmds.setParent('..')
cmds.columnLayout(h = 45, w = 180)
VisButtonOn = cmds.button( label='Visibility', command=("switch(VisButtonOn, VisButtonOff)"), backgroundColor=(0.4, 0.4, 0.4),  h = 45, w = 180)
VisButtonOff = cmds.button( label='Visibility', command=("switch(VisButtonOn, VisButtonOff)"), backgroundColor=(0.2, 0.2, 0.2),  h = 45, w = 180, m=False)
cmds.setParent('..')

cmds.setParent('..')
cmds.setParent('..')
cmds.frameLayout(label = "Inbetween")

cmds.text( label='Joint 1' )
joint1 = cmds.textField()
cmds.text( label='Joint 2' )
joint2 = cmds.textField()
cmds.text( label='Inbetween Joint Name' )
inbetweenName = cmds.textField()

cmds.textField(joint1, edit=True)
cmds.textField(joint2, edit=True)
cmds.textField(inbetweenName, edit=True)

inbetweenType = cmds.optionMenu(label = 'type')
cmds.menuItem(label ='joint')
cmds.menuItem(label = 'locator')
inbetweenDriverBool = cmds.checkBox(label = "Driver")

cmds.text( label='Driver' )
inbetweenDriver = cmds.textField()
cmds.textField(inbetweenDriver, edit=True)
cmds.button(label='Create Inbetween', command=('vfunctions.inbetween(cmds.textField(joint1, query = True, tx= True), cmds.textField(joint2, query = True, tx= True), cmds.textField(inbetweenName, query = True, tx= True), cmds.optionMenu(inbetweenType, query = True, sl = True), cmds.checkBox(inbetweenDriverBool, query = True, value = True), cmds.textField(inbetweenDriver, query = True, tx= True))'), width=112.5)

cmds.setParent('..')
cmds.setParent('..')

cmds.setParent('..')
cmds.button(label='Close', command=('cmds.deleteUI(\"' + riggingWindow + '\", window=True)'))
cmds.setParent('..')

cmds.window(riggingWindow, edit=True, visible=True, widthHeight=(450, 1000))

