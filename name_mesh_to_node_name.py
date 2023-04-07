# rename mesh name to object name
import bpy

collection_name = 'south_east'

for collection in bpy.data.collections:    
    if collection.name == collection_name:
        for obj in collection.all_objects:
            print(obj.type)
            if (obj.type == 'MESH') or (obj.type == 'CURVE'):
                if (obj.data.name != obj.name) and (obj.data.users == 1):
                    print(f'Renaming {obj.data.name} -> {obj.name}')
                    obj.data.name = obj.name
            else:
                print(f'Skipping {obj.name}')
