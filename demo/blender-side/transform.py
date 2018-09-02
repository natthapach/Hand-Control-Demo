from mathutils import Matrix, Quaternion, Vector

class Transformer :

  def translate(self, channel, armature, location) :
    worldPosition = Vector(location)
    self._set_bone_world_position(channel, armature, worldPosition)
    
  def rotate(self, channel, rotation) :
    channel.joint_rotation = Vector(rotation)
    

  def _get_bone_pose_matrix_cleaned(self, bone):
    offset_m4 = (Matrix.Translation(bone.location) * Quaternion(bone.rotation_quaternion).to_matrix().to_4x4())
    return bone.pose_matrix * offset_m4.inverted()
    
  def _set_bone_world_position(self, bone, arm, worldPosition):
      bone.location = self._get_bone_pose_matrix_cleaned(bone).inverted() * arm.worldTransform.inverted() * worldPosition
