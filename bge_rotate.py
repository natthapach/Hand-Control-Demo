import bge
import math
from math import *
import mathutils

x = 0

def rotate():
    print(x)
    global x
    scene = bge.logic.getCurrentScene()
    
    source = scene.objects
    
    main_arm = source.get("Amature")
    
    ob = bge.logic.getCurrentController().owner
    print(ob.channels["Bone"].channel_matrix)
    ob.channels["Bone"].joint_rotation = mathutils.Vector([0, 0, x])
    ob.channels["Bone.001"].joint_rotation = mathutils.Vector([0, 0, x])
    ob.channels["Bone.002"].joint_rotation = mathutils.Vector([0, 0, x])
    ob.update()
    print(ob.channels["Bone"].channel_matrix)
    
    x += 1