# Generate shrine and shrine warp presets
# argument: path/to/data/shrines.yaml
import yaml
import sys

with open(sys.argv[1], "r") as f:
    shrines = yaml.load(f, Loader=yaml.FullLoader)
icons = {}
types = shrines["meta"]["types"]
for shrine_type in types:
    icons[shrine_type] = types[shrine_type]["icon"]
warp_output = []
print("_Shrine:")
data = shrines["data"]
for shrine_id in data:
    typ = data[shrine_id]["type"]
    if typ not in icons:
        print(f"Unknown shrine type: {typ}")
        exit(1)
    icon_id = icons[typ]
    name = data[shrine_id]["name"]
    coord = data[shrine_id]["coord"]
    coord_str = str(coord[0]) + "," + str(coord[1]) + "," + str(coord[2])
    print(f"  {shrine_id}:")
    if typ.endswith("Cave"):
        preset = "ShrineCave"
    elif typ.endswith("Sky"):
        preset = "ShrineSky"
    elif typ == "Dlc":
        preset = "ShrineDlc"
    else:
        preset = "Shrine"
    print(f"    presets: _{preset}<{name},{icon_id},{coord_str}>")
    warp_output.append(f"    {shrine_id}:")
    warp_output.append(f"      presets: _Warp3<{name},{coord_str}>")
print("_Warp:")
print("  _Shrine:")
for x in warp_output:
    print(x)