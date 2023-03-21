import bpy
import os

DELTA_X = 2
DELTA_Y = 2
COL_COUNT = 10

input_folder = "C:\\Users\\harik\\OneDrive\\Desktop\\OBJ format"

def fileList(path):
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            yield os.path.join(dirpath, filename)

col = 0
row = 0

for f in fileList(input_folder):
    if f.lower().endswith(".obj"):        
        bpy.ops.import_scene.obj(filepath=f)
        
        objs = bpy.context.selected_objects

        for obj in objs:
            
            if col > COL_COUNT:
                col = 0
                row += 1
                                
            obj.location.x = col * DELTA_X
            obj.location.y = row * DELTA_Y
            col += 1
        
        
        
