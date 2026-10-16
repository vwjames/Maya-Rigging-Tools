import maya.cmds as cmds
def numberFormating(count, len= 3):
    countString = format(count, '{}n'.format(len))
    countString = countString.replace(" ", "0")
    return(countString)

def circleCtrl(customName = False, name="", controlSuffix = "", parent = False):
    selected = cmds.ls(selection=True)
    count = 1
    if controlSuffix=="":
        controlSuffix = "_Ctrl"
    if len(selected) == 0:
        ctrl = cmds.circle(n="Circle_Control", nr=(0, 0, 1), c=(0, 0, 0))
        if customName:
            cmds.rename("Circle_Control", name + controlSuffix)
        else:
            cmds.rename("Circle_Control", "circle_Ctrl")
    else:
        for x in selected:
            cmds.select(clear=True)
            cmds.select(x)
            ctrl = cmds.circle(n="Circle_Control", nr=(0, 0, 1), c=(0, 0, 0))
            cmds.matchTransform("Circle_Control", x, scl=False)
            if customName:
                if len(selected) == 1:
                    ctrlName = name + controlSuffix
                else:
                    ctrlName = name + "_" + numberFormating(x) + controlSuffix
                cmds.rename("Circle_Control", ctrlName)
            else:
                ctrlName = x
                if (x.endswith(("_jnt", "_Jnt"))):
                    ctrlName = x.rsplit("_", 1)[0]
                ctrlName = ctrlName + controlSuffix
                cmds.rename("Circle_Control", ctrlName)

            if parent:
                cmds.parentConstraint(ctrlName,x)
                cmds.connectAttr("{}.rotateOrder".format(ctrlName), "{}.rotateOrder".format(x))
                cmds.setAttr("{}.rotateOrder".format(ctrlName), cb=True)

            count += 1


def locCtrl(customName = False, name="", controlSuffix = "", parent = False):
    selected = cmds.ls(selection=True)
    count = 1
    if controlSuffix=="":
        controlSuffix = "_Loc"
    if len(selected) == 0:
        ctrl = cmds.spaceLocator(n="Locator_Locator", p=(0, 0, 0))
        if customName:
            cmds.rename("Locator_Locator", name + controlSuffix)
        else:
            cmds.rename("Locator_Locator", "Locator_Loc")
    else:
        for x in selected:
            cmds.select(clear=True)
            cmds.select(x)
            ctrl = cmds.spaceLocator(n="Locator_Locator", p=(0, 0, 0))
            cmds.matchTransform("Locator_Locator", x, scl=False)
            if customName:
                if len(selected) == 1:
                    ctrlName = name + controlSuffix
                else:
                    ctrlName = name + "_" + numberFormating(x) + controlSuffix
                cmds.rename("Locator_Locator", ctrlName)
            else:
                ctrlName = x
                if (x.endswith(("_jnt", "_Jnt"))):
                    ctrlName = x.rsplit("_", 1)[0]
                ctrlName = ctrlName + controlSuffix
                cmds.rename("Locator_Locator", ctrlName)

            if parent:
                cmds.parentConstraint(ctrlName,x)
                cmds.connectAttr("{}.rotateOrder".format(ctrlName), "{}.rotateOrder".format(x))
                cmds.setAttr("{}.rotateOrder".format(ctrlName), cb=True)

            count += 1

def squareCtrl(customName = False, name="", controlSuffix = "", parent = False):
    selected = cmds.ls(selection=True)
    count = 1
    if controlSuffix=="":
        controlSuffix = "_Ctrl"
    if len(selected) == 0:
        ctrl = cmds.curve(n=("Square_Control"), d=1, p=[(-1, 0, 1), (-1, 0, -1), (1, 0, -1), (1, 0, 1), (-1, 0, 1)])
        if customName:
            cmds.rename("Square_Control", name + controlSuffix)
        else:
            cmds.rename("Square_Control", "square_Ctrl")
    else:
        for x in selected:
            cmds.select(clear=True)
            cmds.select(x)
            ctrl = cmds.curve(n=("Square_Control"), d=1, p=[(-1, 0, 1), (-1, 0, -1), (1, 0, -1), (1, 0, 1), (-1, 0, 1)])
            cmds.matchTransform("Square_Control", x, scl=False)
            if customName:
                if len(selected) == 1:
                    ctrlName = name + controlSuffix
                else:
                    ctrlName = name + "_" + numberFormating(x) + controlSuffix
                cmds.rename("Square_Control", ctrlName)
            else:
                ctrlName = x
                if (x.endswith(("_jnt", "_Jnt"))):
                    ctrlName = x.rsplit("_", 1)[0]
                ctrlName = ctrlName + controlSuffix
                cmds.rename("Square_Control", ctrlName)

            if parent:
                cmds.parentConstraint(ctrlName,x)
                cmds.connectAttr("{}.rotateOrder".format(ctrlName), "{}.rotateOrder".format(x))
                cmds.setAttr("{}.rotateOrder".format(ctrlName), cb=True)

            count += 1



def cubeCtrl(customName = False, name="", controlSuffix = "", parent = False):
    selected = cmds.ls(selection=True)
    count = 1
    if controlSuffix=="":
        controlSuffix = "_Ctrl"
    if len(selected) == 0:
        ctrl = cmds.curve(n=("Cube_Control"), d=1,
                          p=[(-1, -1, 1), (-1, -1, -1), (1, -1, -1), (1, -1, 1), (-1, -1, 1), (-1, 1, 1), (-1, 1, -1),
                             (1, 1, -1), (1, 1, 1), (-1, 1, 1), (1, 1, 1), (1, -1, 1), (1, -1, -1), (1, 1, -1),
                             (-1, 1, -1), (-1, -1, -1)])
        if customName:
            cmds.rename("Cube_Control", name + controlSuffix)
        else:
            cmds.rename("Cube_Control", "cube_Ctrl")
    else:
        for x in selected:
            cmds.select(clear=True)
            cmds.select(x)
            ctrl = cmds.curve(n=("Cube_Control"), d=1,
                              p=[(-1, -1, 1), (-1, -1, -1), (1, -1, -1), (1, -1, 1), (-1, -1, 1), (-1, 1, 1),
                                 (-1, 1, -1),
                                 (1, 1, -1), (1, 1, 1), (-1, 1, 1), (1, 1, 1), (1, -1, 1), (1, -1, -1), (1, 1, -1),
                                 (-1, 1, -1), (-1, -1, -1)])
            cmds.matchTransform("Cube_Control", x, scl=False)
            if customName:
                if len(selected) == 1:
                    ctrlName = name + controlSuffix
                else:
                    ctrlName = name + "_" + numberFormating(x) + controlSuffix
                cmds.rename("Cube_Control", ctrlName)
            else:
                ctrlName = x
                if (x.endswith(("_jnt", "_Jnt"))):
                    ctrlName = x.rsplit("_", 1)[0]
                ctrlName = ctrlName + controlSuffix
                cmds.rename("Cube_Control", ctrlName)

            if parent:
                cmds.parentConstraint(ctrlName,x)
                cmds.connectAttr("{}.rotateOrder".format(ctrlName), "{}.rotateOrder".format(x))
                cmds.setAttr("{}.rotateOrder".format(ctrlName), cb=True)

            count += 1

def sphereCtrl(customName = False, name="", controlSuffix = "", parent = False):
    selected = cmds.ls(selection=True)
    count = 1
    if controlSuffix=="":
        controlSuffix = "_Ctrl"
    if len(selected) == 0:
        ctrl = cmds.curve(n=("Sphere_Control"), d=1,
                          p=[(0, 1, 0), (0, 0.6, -0.6), (0, 0, -1), (0, -0.6, -0.6), (0, -1, 0), (0, -0.6, 0.6),
                             (0, 0, 1), (0, 0.6, 0.6), (0, 1, 0), (0.6, 0.6, 0), (1, 0, 0), (0.6, -0.6, 0), (0, -1, 0),
                             (-0.6, -0.6, 0), (-1, 0, 0), (-0.6, 0.6, 0), (0, 1, 0), (-0.6, 0.6, 0), (-1, 0, 0),
                             (-0.6, 0, 0.6), (0, 0, 1), (0.6, 0, 0.6), (1, 0, 0), (0.6, 0, -0.6), (0, 0, -1),
                             (-0.6, 0, -0.6), (-1, 0, 0)],
                          k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
                             25, 26])
        if customName:
            cmds.rename("Sphere_Control", name + controlSuffix)
        else:
            cmds.rename("Sphere_Control", "sphere_Ctrl")
    else:
        for x in selected:
            cmds.select(clear=True)
            cmds.select(x)
            ctrl = cmds.curve(n=("Sphere_Control"), d=1,
                              p=[(0, 1, 0), (0, 0.6, -0.6), (0, 0, -1), (0, -0.6, -0.6), (0, -1, 0), (0, -0.6, 0.6),
                                 (0, 0, 1), (0, 0.6, 0.6), (0, 1, 0), (0.6, 0.6, 0), (1, 0, 0), (0.6, -0.6, 0),
                                 (0, -1, 0),
                                 (-0.6, -0.6, 0), (-1, 0, 0), (-0.6, 0.6, 0), (0, 1, 0), (-0.6, 0.6, 0), (-1, 0, 0),
                                 (-0.6, 0, 0.6), (0, 0, 1), (0.6, 0, 0.6), (1, 0, 0), (0.6, 0, -0.6), (0, 0, -1),
                                 (-0.6, 0, -0.6), (-1, 0, 0)],
                              k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
                                 24,
                                 25, 26])
            cmds.matchTransform("Sphere_Control", x, scl=False)
            if customName:
                if len(selected) == 1:
                    ctrlName = name + controlSuffix
                else:
                    ctrlName = name + "_" + numberFormating(x) + controlSuffix
                cmds.rename("Sphere_Control", ctrlName)
            else:
                ctrlName = x
                if (x.endswith(("_jnt", "_Jnt"))):
                    ctrlName = x.rsplit("_", 1)[0]
                ctrlName = ctrlName + controlSuffix
                cmds.rename("Sphere_Control", ctrlName)

            if parent:
                cmds.parentConstraint(ctrlName,x)
                cmds.connectAttr("{}.rotateOrder".format(ctrlName), "{}.rotateOrder".format(x))
                cmds.setAttr("{}.rotateOrder".format(ctrlName), cb=True)

            count += 1


def pillCtrl(customName = False, name="", controlSuffix = "", parent = False):
    selected = cmds.ls(selection=True)
    count = 1
    if controlSuffix=="":
        controlSuffix = "_Ctrl"
    if len(selected) == 0:
        ctrl = cmds.curve(n=("Pill_Control"), bez=True, d=3,
                          p=[(-1, 0, -1), (-1, 0, -1), (-1, 0, -2), (0, 0, -2), (1, 0, -2), (1, 0, -1), (1, 0, -1),
                             (1, 0, -1), (1, 0, 1), (1, 0, 1), (1, 0, 1), (1, 0, 2), (0, 0, 2), (-1, 0, 2), (-1, 0, 1),
                             (-1, 0, 1), (-1, 0, 1), (-1, 0, -1), (-1, 0, -1)],
                          k=[0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6])
        if customName:
            cmds.rename("Pill_Control", name + controlSuffix)
        else:
            cmds.rename("Pill_Control", "pill_Ctrl")
    else:
        for x in selected:
            cmds.select(clear=True)
            cmds.select(x)
            ctrl = cmds.curve(n=("Pill_Control"), bez=True, d=3,
                              p=[(-1, 0, -1), (-1, 0, -1), (-1, 0, -2), (0, 0, -2), (1, 0, -2), (1, 0, -1), (1, 0, -1),
                                 (1, 0, -1), (1, 0, 1), (1, 0, 1), (1, 0, 1), (1, 0, 2), (0, 0, 2), (-1, 0, 2),
                                 (-1, 0, 1),
                                 (-1, 0, 1), (-1, 0, 1), (-1, 0, -1), (-1, 0, -1)],
                              k=[0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6])
            cmds.matchTransform("Pill_Control", x, scl=False)
            if customName:
                if len(selected) == 1:
                    ctrlName = name + controlSuffix
                else:
                    ctrlName = name + "_" + numberFormating(x) + controlSuffix
                cmds.rename("Pill_Control", ctrlName)
            else:
                ctrlName = x
                if (x.endswith(("_jnt", "_Jnt"))):
                    ctrlName = x.rsplit("_", 1)[0]
                ctrlName = ctrlName + controlSuffix
                cmds.rename("Pill_Control", ctrlName)

            if parent:
                cmds.parentConstraint(ctrlName,x)
                cmds.connectAttr("{}.rotateOrder".format(ctrlName), "{}.rotateOrder".format(x))
                cmds.setAttr("{}.rotateOrder".format(ctrlName), cb=True)

            count += 1

def fourArrowCtrl(customName = False, name="", controlSuffix = "", parent = False):
    selected = cmds.ls(selection=True)
    count = 1
    if controlSuffix=="":
        controlSuffix = "_Ctrl"
    if len(selected) == 0:
        ctrl = cmds.curve(n=("FourArrow_Control"), d=1,
                          p=[(1, 0, 1), (1, 0, 3), (2, 0, 3), (0, 0, 5), (-2, 0, 3), (-1, 0, 3), (-1, 0, 1), (-3, 0, 1),
                             (-3, 0, 2), (-5, 0, 0), (-3, 0, -2), (-3, 0, -1), (-2, 0, -1), (-1, 0, -1), (-1, 0, -3),
                             (-2, 0, -3), (0, 0, -5), (2, 0, -3), (1, 0, -3), (1, 0, -1), (3, 0, -1), (3, 0, -2),
                             (5, 0, 0), (3, 0, 2), (3, 0, 1), (1, 0, 1)],
                          k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
                             25])
        if customName:
            cmds.rename("FourArrow_Control", name + controlSuffix)
        else:
            cmds.rename("FourArrow_Control", "fourArrow_Ctrl")
    else:
        for x in selected:
            cmds.select(clear=True)
            cmds.select(x)
            ctrl = cmds.curve(n=("FourArrow_Control"), d=1,
                              p=[(1, 0, 1), (1, 0, 3), (2, 0, 3), (0, 0, 5), (-2, 0, 3), (-1, 0, 3), (-1, 0, 1),
                                 (-3, 0, 1),
                                 (-3, 0, 2), (-5, 0, 0), (-3, 0, -2), (-3, 0, -1), (-2, 0, -1), (-1, 0, -1),
                                 (-1, 0, -3),
                                 (-2, 0, -3), (0, 0, -5), (2, 0, -3), (1, 0, -3), (1, 0, -1), (3, 0, -1), (3, 0, -2),
                                 (5, 0, 0), (3, 0, 2), (3, 0, 1), (1, 0, 1)],
                              k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
                                 24, 25])
            cmds.matchTransform("FourArrow_Control", x, scl=False)
            if customName:
                if len(selected) == 1:
                    ctrlName = name + controlSuffix
                else:
                    ctrlName = name + "_" + numberFormating(x) + controlSuffix
                cmds.rename("FourArrow_Control", ctrlName)
            else:
                ctrlName = x
                if (x.endswith(("_jnt", "_Jnt"))):
                    ctrlName = x.rsplit("_", 1)[0]
                ctrlName = ctrlName + controlSuffix
                cmds.rename("FourArrow_Control", ctrlName)

            if parent:
                cmds.parentConstraint(ctrlName,x)
                cmds.connectAttr("{}.rotateOrder".format(ctrlName), "{}.rotateOrder".format(x))
                cmds.setAttr("{}.rotateOrder".format(ctrlName), cb=True)

            count += 1


def twoArrowCtrl(customName = False, name="", controlSuffix = "", parent = False):
    selected = cmds.ls(selection=True)
    count = 1
    if controlSuffix=="":
        controlSuffix = "_Ctrl"
    if len(selected) == 0:
        ctrl = cmds.curve(n=("TwoArrow_Control"), d=1,
                          p=[(-1, 0, 1), (-1, 0, -1), (-2, 0, -1), (0, 0, -3), (2, 0, -1), (1, 0, -1), (1, 0, 1),
                             (2, 0, 1), (0, 0, 3), (-2, 0, 1), (-1, 0, 1)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        if customName:
            cmds.rename("TwoArrow_Control", name + controlSuffix)
        else:
            cmds.rename("TwoArrow_Control", "twoArrow_Ctrl")
    else:
        for x in selected:
            cmds.select(clear=True)
            cmds.select(x)
            ctrl = cmds.curve(n=("TwoArrow_Control"), d=1,
                              p=[(-1, 0, 1), (-1, 0, -1), (-2, 0, -1), (0, 0, -3), (2, 0, -1), (1, 0, -1), (1, 0, 1),
                                 (2, 0, 1), (0, 0, 3), (-2, 0, 1), (-1, 0, 1)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
            cmds.matchTransform("TwoArrow_Control", x, scl=False)
            if customName:
                if len(selected) == 1:
                    ctrlName = name + controlSuffix
                else:
                    ctrlName = name + "_" + numberFormating(x) + controlSuffix
                cmds.rename("TwoArrow_Control", ctrlName)
            else:
                ctrlName = x
                if (x.endswith(("_jnt", "_Jnt"))):
                    ctrlName = x.rsplit("_", 1)[0]
                ctrlName = ctrlName + controlSuffix
                cmds.rename("TwoArrow_Control", ctrlName)

            if parent:
                cmds.parentConstraint(ctrlName,x)
                cmds.connectAttr("{}.rotateOrder".format(ctrlName), "{}.rotateOrder".format(x))
                cmds.setAttr("{}.rotateOrder".format(ctrlName), cb=True)

            count += 1

def arrowCtrl(customName = False, name="", controlSuffix = "", parent = False):
    selected = cmds.ls(selection=True)
    count = 1
    if controlSuffix=="":
        controlSuffix = "_Ctrl"
    if len(selected) == 0:
        ctrl = cmds.curve(n=("Arrow_Control"), d=1,
                          p=[(-1, 0, -1), (-2, 0, -1), (0, 0, -3), (2, 0, -1), (1, 0, -1), (1, 0, 2), (-1, 0, 2),
                             (-1, 0, -1)], k=[0, 1, 2, 3, 4, 5, 6, 7])
        if customName:
            cmds.rename("Arrow_Control", name + controlSuffix)
        else:
            cmds.rename("Arrow_Control", "arrow_Ctrl")
    else:
        for x in selected:
            cmds.select(clear=True)
            cmds.select(x)
            ctrl = cmds.curve(n=("Arrow_Control"), d=1,
                              p=[(-1, 0, -1), (-2, 0, -1), (0, 0, -3), (2, 0, -1), (1, 0, -1), (1, 0, 2), (-1, 0, 2),
                                 (-1, 0, -1)], k=[0, 1, 2, 3, 4, 5, 6, 7])
            cmds.matchTransform("Arrow_Control", x, scl=False)
            if customName:
                if len(selected) == 1:
                    ctrlName = name + controlSuffix
                else:
                    ctrlName = name + "_" + numberFormating(x) + controlSuffix
                cmds.rename("Arrow_Control", ctrlName)
            else:
                ctrlName = x
                if (x.endswith(("_jnt", "_Jnt"))):
                    ctrlName = x.rsplit("_", 1)[0]
                ctrlName = ctrlName + controlSuffix
                cmds.rename("Arrow_Control", ctrlName)

            if parent:
                cmds.parentConstraint(ctrlName,x)
                cmds.connectAttr("{}.rotateOrder".format(ctrlName), "{}.rotateOrder".format(x))
                cmds.setAttr("{}.rotateOrder".format(ctrlName), cb=True)

            count += 1

def curvedArrowCtrl(customName=False, name="", controlSuffix="", parent=False):
    selected = cmds.ls(selection=True)
    count = 1
    if controlSuffix == "":
        controlSuffix = "_Ctrl"
    if len(selected) == 0:
        ctrl = cmds.curve(n=("Curved_Arrow_Control"), d=1,
                          p=[(0, 0, 1), (0.382683, 0.5, 0.92388), (0.707107, 1, 0.707107), (0.707107, 0.5, 0.707107),
                             (0.92388, 0.5, 0.382683), (1, 0.5, 0), (0.92388, 0.5, -0.382683),
                             (0.707107, 0.5, -0.707106), (0.382684, 0.5, -0.923879), (0, 0.5, -1),
                             (-0.382683, 0.5, -0.92388), (-0.707106, 0.5, -0.707107), (-0.923879, 0.5, -0.382684),
                             (-1, 0.5, 0), (-0.92388, 0.5, 0.382683), (-0.707107, 0.5, 0.707107),
                             (-0.382684, 0.5, 0.923879), (-0.382684, -0.5, 0.923879), (-0.707107, -0.5, 0.707107),
                             (-0.92388, -0.5, 0.382683), (-1, -0.5, 0), (-0.923879, -0.5, -0.382684),
                             (-0.707106, -0.5, -0.707107), (-0.382683, -0.5, -0.92388), (0, -0.5, -1),
                             (0.382684, -0.5, -0.923879), (0.707107, -0.5, -0.707106), (0.92388, -0.5, -0.382683),
                             (1, -0.5, 0), (0.92388, -0.5, 0.382683), (0.707107, -0.5, 0.707107),
                             (0.707107, -1, 0.707107), (0.382683, -0.5, 0.92388), (0, 0, 1)], k = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33])
        if customName:
            cmds.rename("Curved_Arrow_Control", name + controlSuffix)
        else:
            cmds.rename("Curved_Arrow_Control", "curvedArrow_Ctrl")
    else:
        for x in selected:
            cmds.select(clear=True)
            cmds.select(x)
            ctrl = cmds.curve(n=("Curved_Arrow_Control"), d=1,
                              p=[(0, 0, 1), (0.382683, 0.5, 0.92388), (0.707107, 1, 0.707107),
                                 (0.707107, 0.5, 0.707107),
                                 (0.92388, 0.5, 0.382683), (1, 0.5, 0), (0.92388, 0.5, -0.382683),
                                 (0.707107, 0.5, -0.707106), (0.382684, 0.5, -0.923879), (0, 0.5, -1),
                                 (-0.382683, 0.5, -0.92388), (-0.707106, 0.5, -0.707107), (-0.923879, 0.5, -0.382684),
                                 (-1, 0.5, 0), (-0.92388, 0.5, 0.382683), (-0.707107, 0.5, 0.707107),
                                 (-0.382684, 0.5, 0.923879), (-0.382684, -0.5, 0.923879), (-0.707107, -0.5, 0.707107),
                                 (-0.92388, -0.5, 0.382683), (-1, -0.5, 0), (-0.923879, -0.5, -0.382684),
                                 (-0.707106, -0.5, -0.707107), (-0.382683, -0.5, -0.92388), (0, -0.5, -1),
                                 (0.382684, -0.5, -0.923879), (0.707107, -0.5, -0.707106), (0.92388, -0.5, -0.382683),
                                 (1, -0.5, 0), (0.92388, -0.5, 0.382683), (0.707107, -0.5, 0.707107),
                                 (0.707107, -1, 0.707107), (0.382683, -0.5, 0.92388), (0, 0, 1)],
                              k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
                                 24, 25, 26, 27, 28, 29, 30, 31, 32, 33])
            cmds.matchTransform("Curved_Arrow_Control", x, scl=False)
            if customName:
                if len(selected) == 1:
                    ctrlName = name + controlSuffix
                else:
                    ctrlName = name + "_" + numberFormating(x) + controlSuffix
                cmds.rename("Curved_Arrow_Control", ctrlName)
            else:
                ctrlName = x
                if (x.endswith(("_jnt", "_Jnt"))):
                    ctrlName = x.rsplit("_", 1)[0]
                ctrlName = ctrlName + controlSuffix
                cmds.rename("Curved_Arrow_Control", ctrlName)

            if parent:
                cmds.parentConstraint(ctrlName, x)
                cmds.connectAttr("{}.rotateOrder".format(ctrlName), "{}.rotateOrder".format(x))
                cmds.setAttr("{}.rotateOrder".format(ctrlName), cb=True)

            count += 1
def colour(c):
    selected = cmds.ls(selection=True)
    for x in selected:
        cmds.setAttr('{}.overrideEnabled'.format(x), 1)
        cmds.setAttr('{}.overrideRGBColors'.format(x), False)
        cmds.setAttr('{}.overrideColor'.format(x), c)


def RGBcolour(r, g, b):
    selected = cmds.ls(selection=True)
    for x in selected:
        cmds.setAttr('{}.overrideEnabled'.format(x), 1)
        cmds.setAttr('{}.overrideRGBColors'.format(x), True)
        cmds.setAttr('{}.overrideColorR'.format(x), r)
        cmds.setAttr('{}.overrideColorG'.format(x), g)
        cmds.setAttr('{}.overrideColorB'.format(x), b)


def space():
    selected = cmds.ls(selection=True)
    for x in selected:
        my_grp = cmds.createNode("transform", name=x + "_Grp")
        cmds.matchTransform(my_grp, x)
        cmds.parent(x, my_grp)
        cmds.warning("{} Spaced".format(my_grp))

def lock(all, suffixBool, suffix, RX, RY, RZ, TX, TY, TZ, SX, SY, SZ, V):
    if suffixBool:
        filter = cmds.itemFilter(byName='*{}'.format(suffix))
    else:
        filter = cmds.itemFilter(byName='*')
    if all:
        objects = cmds.lsThroughFilter(filter)
    else:
        objects = cmds.lsThroughFilter(filter, sl = True)

    for x in objects:
        #cmds.select(clear=True)
        #cmds.select(x)
        if(RX):
            cmds.setAttr('{}.rotateX'.format(x), k=False, lock=True)
            cmds.setAttr('{}.rotateX'.format(x), cb=False)
        if (RY):
            cmds.setAttr('{}.rotateY'.format(x), k=False, lock=True)
            cmds.setAttr('{}.rotateY'.format(x), cb=False)
        if (RZ):
            cmds.setAttr('{}.rotateZ'.format(x), k=False, lock=True)
            cmds.setAttr('{}.rotateZ'.format(x), cb=False)
        if (TX):
            cmds.setAttr('{}.translateX'.format(x), k=False, lock=True)
            cmds.setAttr('{}.translateX'.format(x), cb=False)
        if (TY):
            cmds.setAttr('{}.translateY'.format(x), k=False, lock=True)
            cmds.setAttr('{}.translateY'.format(x), cb=False)
        if (TZ):
            cmds.setAttr('{}.translateZ'.format(x), k=False, lock=True)
            cmds.setAttr('{}.translateZ'.format(x), cb=False)
        if (SX):
            cmds.setAttr('{}.scaleX'.format(x), k=False, lock=True)
            cmds.setAttr('{}.scaleX'.format(x), cb=False)
        if (SY):
            cmds.setAttr('{}.scaleY'.format(x), k=False, lock=True)
            cmds.setAttr('{}.scaleY'.format(x), cb=False)
        if (SZ):
            cmds.setAttr('{}.scaleZ'.format(x), k=False, lock=True)
            cmds.setAttr('{}.scaleZ'.format(x), cb=False)
        if (V):
            cmds.setAttr('{}.visibility'.format(x), k=False, lock=True)
            cmds.setAttr('{}.visibility'.format(x), cb=False)
        print("{} was locked".format(x))

def unlock(all, suffixBool, suffix, RX, RY, RZ, TX, TY, TZ, SX, SY, SZ, V):

    if suffixBool:
        filter = cmds.itemFilter(byName='*{}'.format(suffix))
    else:
        filter = cmds.itemFilter(byName='*')
    if all:
        objects = cmds.lsThroughFilter(filter)
    else:
        objects = cmds.lsThroughFilter(filter, sl = True)

    for x in objects:
        #cmds.select(clear=True)
        #cmds.select(x)

        if(RX):
            cmds.setAttr('{}.rotateX'.format(x), cb=True)
            cmds.setAttr('{}.rotateX'.format(x), k=True, lock=False)
        if (RY):
            cmds.setAttr('{}.rotateY'.format(x), cb=True)
            cmds.setAttr('{}.rotateY'.format(x), k=True, lock=False)
        if (RZ):
            cmds.setAttr('{}.rotateZ'.format(x), cb=True)
            cmds.setAttr('{}.rotateZ'.format(x), k=True, lock=False)
        if (TX):
            cmds.setAttr('{}.translateX'.format(x), cb=True)
            cmds.setAttr('{}.translateX'.format(x), k=True, lock=False)
        if (TY):
            cmds.setAttr('{}.translateY'.format(x), cb=True)
            cmds.setAttr('{}.translateY'.format(x), k=True, lock=False)
        if (TZ):
            cmds.setAttr('{}.translateZ'.format(x), cb=True)
            cmds.setAttr('{}.translateZ'.format(x), k=True, lock=False)
        if (SX):
            cmds.setAttr('{}.scaleX'.format(x), cb=True)
            cmds.setAttr('{}.scaleX'.format(x), k=True, lock=False)
        if (SY):
            cmds.setAttr('{}.scaleY'.format(x), cb=True)
            cmds.setAttr('{}.scaleY'.format(x), k=True, lock=False)
        if (SZ):
            cmds.setAttr('{}.scaleZ'.format(x), cb=True)
            cmds.setAttr('{}.scaleZ'.format(x), k=True, lock=False)
        if (V):
            cmds.setAttr('{}.visibility'.format(x), cb=True)
            cmds.setAttr('{}.visibility'.format(x), k=True, lock=False)
        print("{} was unlocked".format(x))

def sdk(inputs, output, driver):
    x = 0
    # make parent constraints
    while x < len(inputs):
        cmds.parentConstraint(inputs[x], output)
        x += 1

    x = 0
    while x < len(inputs):
        cmds.setAttr(driver, x)
        y = 0
        while y < len(inputs):
            if y == x:
                cmds.setAttr("{}_parentConstraint1.{}W{}".format(output, inputs[y], y), 1)

            else:
                cmds.setAttr("{}_parentConstraint1.{}W{}".format(output, inputs[y], y), 0)
            cmds.setDrivenKeyframe("{}_parentConstraint1.{}W{}".format(output, inputs[y], y), cd=driver)
            y += 1
        x += 1


def inbetween(joint1, joint2, name,  type=1, driver=False, driverName=""):
    if type == 2:
        ctrl = cmds.spaceLocator(n="Locator_Locator", p=(0, 0, 0))
        cmds.matchTransform(ctrl, joint2, scl=False)
        ctrlName = joint2
        if (name.endswith(("_jnt", "_Jnt"))):
            ctrlName = name.rsplit("_", 1)[0]
        ctrlName = ctrlName + "_Loc"
        print(ctrlName)
        cmds.rename('Locator_Locator', ctrlName)
    elif type == 1:
        ctrl = cmds.joint(n="Joint_", p=(0, 0, 0))
        cmds.matchTransform(ctrl, joint2, scl=False)
        ctrlName = joint2
        if (name.endswith(("_jnt", "_Jnt"))):
            ctrlName = name.rsplit("_", 1)[0]
        ctrlName = ctrlName + "_jnt"
        print(ctrlName)
        cmds.rename('Joint_', ctrlName)
    else:
        print("ERROR: invalid type")
        return

    my_grp = cmds.createNode("transform", name=ctrlName + "_Grp")
    cmds.matchTransform(my_grp, ctrlName)
    cmds.parent(ctrlName, my_grp)
    cmds.warning("Spaced")

    cmds.parent(my_grp, joint1)

    # Create float Constants
    cmds.createNode('floatConstant', n="{}_Rotate_X".format(joint2))
    cmds.createNode('floatConstant', n="{}_Rotate_Y".format(joint2))
    cmds.createNode('floatConstant', n="{}_Rotate_Z".format(joint2))

    # Crate Rotation Nodes
    cmds.createNode('plusMinusAverage', n="{}_Rotate_Sum".format(joint2))
    cmds.createNode('multiplyDivide', n="{}_Rotate_Reduced".format(joint2))

    # Set operations to correct values
    cmds.setAttr("{}_Rotate_Reduced.operation".format(joint2), 1)
    cmds.setAttr("{}_Rotate_Sum.operation".format(joint2), 1)

    # Save extant rotation values
    cmds.setAttr("{}_Rotate_X.inFloat".format(joint2), cmds.getAttr("{}.rotateX".format(joint2)))
    cmds.setAttr("{}_Rotate_Y.inFloat".format(joint2), cmds.getAttr("{}.rotateY".format(joint2)))
    cmds.setAttr("{}_Rotate_Z.inFloat".format(joint2), cmds.getAttr("{}.rotateZ".format(joint2)))

    # Set multiplydivide values
    cmds.setAttr("{}_Rotate_Reduced.input2X".format(joint2), 0.5)
    cmds.setAttr("{}_Rotate_Reduced.input2Y".format(joint2), 0.5)
    cmds.setAttr("{}_Rotate_Reduced.input2Z".format(joint2), 0.5)

    # Connect saved rotation values
    cmds.connectAttr("{}_Rotate_X.outFloat".format(joint2), "{}_Rotate_Sum.input3D[0].input3Dx".format(joint2))
    cmds.connectAttr("{}_Rotate_Y.outFloat".format(joint2), "{}_Rotate_Sum.input3D[0].input3Dy".format(joint2))
    cmds.connectAttr("{}_Rotate_Z.outFloat".format(joint2), "{}_Rotate_Sum.input3D[0].input3Dz".format(joint2))

    cmds.connectAttr("{}_Rotate_Reduced.output".format(joint2), "{}_Rotate_Sum.input3D[1]".format(joint2))
    cmds.connectAttr("{}.rotate".format(joint2), "{}_Rotate_Reduced.input1".format(joint2))

    cmds.connectAttr("{}_Rotate_Sum.output3D".format(joint2), "{}.rotate".format(my_grp))
    cmds.connectAttr("{}.translate".format(joint2), "{}.translate".format(my_grp))
    if driver:
        try:
            cmds.connectAttr(driverName, "{}_Rotate_Reduced.input2X".format(joint2))
            cmds.connectAttr(driverName, "{}_Rotate_Reduced.input2Y".format(joint2))
            cmds.connectAttr(driverName, "{}_Rotate_Reduced.input2Z".format(joint2))
        except:
            print("Error, {} is not a valid driver".format(driverName))
    else:
        cmds.createNode('floatConstant', n="{}_Driver".format(joint2))

def curveIKSetup(IKName, bones, driver, curvePoints = 4,controls = 3):
    if curvePoints == 4:
        ikCurveParts = cmds.ikHandle(n = IKName, sj = bones[0], ee = bones[len(bones)-1], sol ="ikSplineSolver",ccv =True, ns = 1, scv = True)
    if curvePoints == 10:
        ikCurveParts = cmds.ikHandle(n = IKName, sj = bones[0], ee = bones[len(bones)-1], sol ="ikSplineSolver",ccv =True, ns = 7, scv = True)

    cmds.rename(ikCurveParts[2], "{}_Crv".format(IKName))
    if controls == 0:
        i = 0
        while i < curvePoints:
            cmds.cluster("{}_Crv.cv[{}]".format(IKName,i), n="{}_Cluster_{}".format(IKName, numberFormating(i)))
            i+=1
    if controls == 3:
        cmds.cluster("{}_Crv.cv[0]".format(IKName), n="{}_Cluster_001".format(IKName))
        cmds.cluster("{}_Crv.cv[1:2]".format(IKName), n="{}_Cluster_002".format(IKName))
        cmds.cluster("{}_Crv.cv[3]".format(IKName), n="{}_Cluster_003".format(IKName))

    cmds.createNode( 'curveInfo', n = "{}_curveInfo".format(IKName))
    curveShape = cmds.listRelatives("{}_Crv".format(IKName), s=True)
    cmds.connectAttr("{}.worldSpace[0]".format(curveShape[0]), "{}_curveInfo.inputCurve".format(IKName))
    cmds.createNode( 'multiplyDivide', n = "{}_multiplyDivide".format(IKName))
    cmds.connectAttr("{}_curveInfo.arcLength".format(IKName), "{}_multiplyDivide.input1X".format(IKName))
    cmds.setAttr("{}_multiplyDivide.operation".format(IKName), 2)
    cmds.setAttr("{}_multiplyDivide.input2X".format(IKName), cmds.getAttr("{}_curveInfo.arcLength".format(IKName)))

    x = 0
    while x < len(bones):
        cmds.connectAttr("{}_multiplyDivide.outputX".format(IKName), "{}.scaleY".format(bones[x]))
        x +=1

def enumDrivenVis(name, driver, value):
    driverName = driver.replace(".", "_")
    if not(cmds.objExists("{}_Condition_{}".format(driverName, numberFormating(value)))):
        cmds.createNode('condition', n = "{}_Condition_{}".format(driverName, numberFormating(value)))
        cmds.connectAttr(driver, "{}_Condition_{}.firstTerm".format(driverName, numberFormating(value)))
    cmds.setAttr("{}_Condition_{}.secondTerm".format(driverName, numberFormating(value)), value)
    cmds.setAttr("{}_Condition_{}.operation".format(driverName, numberFormating(value)), 0)
    cmds.setAttr("{}_Condition_{}.colorIfTrueR".format(driverName, numberFormating(value)), 1)
    cmds.setAttr("{}_Condition_{}.colorIfFalseR".format(driverName, numberFormating(value)), 0)
    cmds.connectAttr("{}_Condition_{}.outColorR".format(driverName, numberFormating(value)), "{}.visibility".format(name))

def enumDrivenParent(name, target, driver, value, parent = False):
    driverName = driver.replace(".", "_")
    if not(cmds.objExists("{}_Condition_{}".format(driverName, numberFormating(value)))):
        print("{}_Condition_{}".format(driverName, numberFormating(value)))
        cmds.createNode('condition', n = "{}_Condition_{}".format(driverName, numberFormating(value)))
        cmds.connectAttr(driver, "{}_Condition_{}.firstTerm".format(driverName, numberFormating(value)))
    cmds.setAttr("{}_Condition_{}.secondTerm".format(driverName, numberFormating(value)), value)
    cmds.setAttr("{}_Condition_{}.operation".format(driverName, numberFormating(value)), 0)
    cmds.setAttr("{}_Condition_{}.colorIfTrueR".format(driverName, numberFormating(value)), 1)
    cmds.setAttr("{}_Condition_{}.colorIfFalseR".format(driverName, numberFormating(value)), 0)
    #Make more robust
    cmds.connectAttr("{}_Condition_{}.outColorR".format(driverName, numberFormating(value)), "{}.{}W{}".format(target, name,value))

def findCentre(objects):
    x = 0
    y = 0
    z = 0

    xyz = []
    for o in objects:
        object = cmds.xform(o, q=True, t=True, ws=True)
        x += object[0]
        y += object[1]
        z += object[2]
    x/=len(objects)
    xyz.append(x)
    y/=len(objects)
    xyz.append(y)
    z/=len(objects)
    xyz.append(z)
    return(xyz)
tailJoints = ["Tail_001", "Tail_006"]
#def setupRotateOrder(inputs):
#    for x in inputs:

def transformControl(name, rot = [0, 0, 0], trans = [0, 0, 0], scl = [1, 1, 1]):
    verts = cmds.ls('{}.cv[:]'.format(name), fl=True)
    cmds.select(clear = True)
    for v in verts:
        cmds.select(v, add = True)

    cmds.rotate("{}deg".format(rot[0]), rotateX =True)
    cmds.rotate("{}deg".format(rot[1]), rotateY =True)
    cmds.rotate("{}deg".format(rot[2]), rotateZ =True)

    cmds.move(trans[0], ls = True, x =True, r = True)
    cmds.move(trans[1], ls = True, y =True, r = True)
    cmds.move(trans[2], ls = True, z =True, r = True)

    cmds.scale(scl[0], x = True)
    cmds.scale(scl[1], y = True)
    cmds.scale(scl[2], z = True)
