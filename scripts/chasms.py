# Generate chasm presets
# argument: path/to/data/chasms.yaml
import yaml
import sys

with open(sys.argv[1], "r") as f:
    chasms = yaml.load(f, Loader=yaml.FullLoader)
print("_Chasm:")
data = chasms["data"]
enter_lines = []
exit_lines = []
for id in sorted(data):
    name = data[id]["name"]
    coord = data[id]["coord"]
    coord_str = str(coord[0]) + "," + str(coord[1]) + "," + str(coord[2])
    enter_lines.append(f"    {id}:")
    enter_lines.append(f"      presets: _ChasmEnter<{name},{coord_str}>")
    exit_lines.append(f"    {id}:")
    exit_lines.append(f"      presets: _ChasmExit<{name},{coord_str}>")

print("  _Enter:")
for x in enter_lines:
    print(x)
print("  _Exit:")
for x in exit_lines:
    print(x)
