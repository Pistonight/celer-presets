# Generate well presets
# argument: path/to/data/wells.yaml
import yaml
import sys

with open(sys.argv[1], "r") as f:
    wells = yaml.load(f, Loader=yaml.FullLoader)
print("_Well:")
data = wells["data"]
for id in data:
    name = data[id]["name"]
    coord = data[id]["coord"]
    coord_str = str(coord[0]) + "," + str(coord[1]) + "," + str(coord[2])
    print(f"  {id}:")
    print(f"    presets: _Well<{name},{coord_str}>")