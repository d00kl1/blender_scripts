# rename mesh name to object name
import bpy

collection_name = 'north'

obj_name_prefix = 'n_'

for collection in bpy.data.collections:    
    if collection.name == collection_name:
        for obj in collection.all_objects:
            if not obj.name.startswith(obj_name_prefix) and obj.name != collection_name:
                print(f'Renaming {obj.name} -> {obj_name_prefix}{obj.name}')
                obj.name = obj_name_prefix + obj.name                
                
            if (obj.type == 'MESH') or (obj.type == 'CURVE'):
                if (obj.data.name != obj.name) and (obj.data.users == 1):
                    print(f'Renaming {obj.data.name} -> {obj.name}')
                    obj.data.name = obj.name
            else:
                print(f'Skipping {obj.name}')
