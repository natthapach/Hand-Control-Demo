import bge
import math
from math import *
from mathutils import Quaternion, Vector, Matrix
import socket01

world = (1.5570, 1.8700, 1.1212)
flag1 = True

def translate():
    # predefine
    direction = 1
    axis = "x"
    tip = "indexTip_IK"
    speed = 0.1
    
    # query enviroment
    scene = bge.logic.getCurrentScene()
    source = scene.objects
    armature = source.get("Armature")
    ctrl = bge.logic.getCurrentController()
    ob = ctrl.owner
    ch = ob.channels[tip]
    loc = ch.location
    bone = ch.bone
    
    # route
    if ctrl.sensors["W"].positive :
        direction = 1
    elif ctrl.sensors["S"].positive :
        direction = -1
    else :
        return
    
    if ctrl.sensors["X"].positive :
        loc.x += speed * direction
    elif ctrl.sensors["Y"].positive :
        loc.y += speed * direction 
    elif ctrl.sensors["Z"].positive :
        loc.z += speed * direction
    else :
        return 
    print("1", loc, ob.worldPosition, ob.localPosition)
    # print("2", bone.arm_head, bone.arm_tail)
    # print("3", ob.worldPosition - bone.arm_head)
    # print(ch.channel_matrix)
    # print(ch.pose_matrix)
    # print(ch.pose_head)
    # print(bone.arm_head * ch.pose_matrix)
    print(bone.arm_head * ob.worldPosition)
    # print((ob.worldTransform * ch.pose_matrix).to_translation())
    ob.channels[tip].location = loc
    ob.update()
    
def directTranslate() :
  global flag1
  # predefine
  direction = 1
  axis = "x"
  tip = "indexTip_IK"
  speed = 0.1
  
  # query enviroment
  scene = bge.logic.getCurrentScene()
  source = scene.objects
  armature = source.get("Armature")
  ctrl = bge.logic.getCurrentController()
  ob = ctrl.owner
  ch = ob.channels[tip]
  loc = ch.location
  bone = ch.bone;
  raw_loc = (1.76881, )
  loc = [-0.9678, -1.00528, 1.68263]
  
  print(loc, ch.pose_head)
  # ob.channels[tip].location = loc

  set_bone_world_position(ch, ob, Vector([-0.9678, -1.00528, 1.68263]))

  flag1 = not flag1
  ob.update()
  
def getRotation() :
    scene = bge.logic.getCurrentScene()
    
    source = scene.objects
    
    main_arm = source.get("Amature")
    
    ob = bge.logic.getCurrentController().owner
    rotation = ob.channels["hand"].rotation_quaternion
    print(rotation.toEuler())
  
def directRotate() :
    scene = bge.logic.getCurrentScene()
    
    source = scene.objects
    
    main_arm = source.get("Amature")
    
    ob = bge.logic.getCurrentController().owner
    
    ob.channels["hand"]. joint_rotation = Vector([0, 0, 3.14])
    ob.update()
  
def get_bone_pose_matrix_cleaned(bone):
    # note that lack the scale (i'm not sure how make it)
    offset_m4 = (Matrix.Translation(bone.location) * Quaternion(bone.rotation_quaternion).to_matrix().to_4x4())
    return bone.pose_matrix * offset_m4.inverted()
    
def set_bone_world_position(bone, arm, worldPosition):
    bone.location = get_bone_pose_matrix_cleaned(bone).inverted() * arm.worldTransform.inverted() * worldPosition

    
    