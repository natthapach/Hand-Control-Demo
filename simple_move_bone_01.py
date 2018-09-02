import bpy
pb = bpy.data.objects["bone"].pose.bones["indexTip_IK"]
ob = bpy.context.object
mw = ob.convert_space(pose_bone=pb, 
        matrix=pb.matrix, 
        from_space='POSE', 
        to_space='WORLD')
mw.translation = (10, 10, 10)
pb.matrix = ob.convert_space(pose_bone=pb, 
        matrix=mw, 
        from_space='WORLD', 
        to_space='POSE')