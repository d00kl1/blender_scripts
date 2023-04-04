# geometry node -> list of objects using this geometry node
import bpy

modif_names = {}

for obj in bpy.data.objects:
    for modif in obj.modifiers:
        if type(modif) == bpy.types.NodesModifier:            
            obj_name = obj.name            
            modif_name = modif.node_group.name
            
            if modif_name not in modif_names.keys():
                modif_names[modif_name] = []
            
            modif_names[modif_name].append(obj_name)


modif_names = {k: v for k, v in sorted(modif_names.items(), key=lambda item: len(item[1]))}

for m in modif_names:
    values = modif_names[m]
    print(f'{m} -> {values}')

