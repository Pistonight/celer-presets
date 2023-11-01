# Generate bubbulfrog presets
# argument: path/to/data/bubbulfrogs.yaml path/to/data/caves.yaml
import yaml
import sys

with open(sys.argv[1], "r") as f:
    bbfs = yaml.load(f, Loader=yaml.FullLoader)
with open(sys.argv[2], "r") as f:
    caves = yaml.load(f, Loader=yaml.FullLoader)
print("_Bubbulfrog:")
data = bbfs["data"]
for id in sorted(data):
    if id.endswith("Cave"):
        cave_id = id[:-4]
    elif id == "CaveUnderZorasDomain":
        cave_id = "UnderZorasDomain"
    else:
        cave_id = id
    name = caves["data"][cave_id]["name"]
    
    coord = data[id]["coord"]
    coord_str = str(coord[0]) + "," + str(coord[1]) + "," + str(coord[2])
    print(f"  {id}:")
    print(f"    presets: _Bubbulfrog<{name},{coord_str}>")