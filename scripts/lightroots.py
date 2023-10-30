# Generate shrine and shrine warp presets
# argument: path/to/data/lightroots.yaml
import yaml
import sys

with open(sys.argv[1], "r") as f:
    lightroots = yaml.load(f, Loader=yaml.FullLoader)
warp_output = []
print("_Lightroot:")
data = lightroots["data"]
for id in data:
    
    name = data[id]["name"]
    coord = data[id]["coord"]
    coord_str = str(coord[0]) + "," + str(coord[1]) + "," + str(coord[2])
    print(f"  {id}:")
    print(f"    presets: _Lightroot<{name},{coord_str}>")
    warp_output.append(f"    {id}:")
    warp_output.append("      presets:")
    warp_output.append(f"      - _Warp3<{name},{coord_str}>")
    warp_output.append(f"      - _WarpDepth")
print("_Warp:")
print("  _Lightroot:")
for x in warp_output:
    print(x)