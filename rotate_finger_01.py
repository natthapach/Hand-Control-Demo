import bge
import math
from math import *
import mathutils

x = 0
z = 0
def rotate():
    global x
    print(x)
    scene = bge.logic.getCurrentScene()
    source = scene.objects
    amature = source.get("Armature")
    ob = bge.logic.getCurrentController().owner
    ob.channels["littleCtrl"].joint_rotation = mathutils.Vector([0, 0, x])
    ob.update()
    
    x += 0.1
def translate():
    global z
    print(z)
    scene = bge.logic.getCurrentScene()
    source = scene.objects
    amature = source.get("Armature")
    ob = bge.logic.getCurrentController().owner
    loc = ob.channels["littleTip_IK"].location
    loc.x += z
    ob.channels["littleTip_IK"].location = loc
    ob.update()
    
    z += 0.1
    
def scale() :
    global z
    print(z)
    scene = bge.logic.getCurrentScene()
    source = scene.objects
    amature = source.get("Armature")
    ob = bge.logic.getCurrentController().owner
    ob.channels["littleCtrl"].location.z += z
    ob.update()
    
    z += 0.1
    
