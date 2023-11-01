# Generate cave presets
# argument: path/to/data/caves.yaml
import yaml
import sys

with open(sys.argv[1], "r") as f:
    caves = yaml.load(f, Loader=yaml.FullLoader)
print("_Cave:")
data = caves["data"]
enter_lines = []
exit_lines = []
for id in sorted(data):
    name = data[id]["name"]
    entrances = data[id]["entrances"]
    if len(entrances) == 1:
        entrance = entrances[0]
        coord = entrance["coord"]
        coord_str = str(coord[0]) + "," + str(coord[1]) + "," + str(coord[2])
        enter_lines.append(f"    {id}:")
        enter_lines.append(f"      presets: _CaveEnter<{name},{coord_str}>")
        exit_lines.append(f"    {id}:")
        exit_lines.append(f"      presets: _CaveExit<{name},{coord_str}>")
    else:
        enter_lines.append(f"    _{id}:")
        exit_lines.append(f"    _{id}:")
        for i, entrance in enumerate(entrances):
            entrance_id = chr(ord("A") + i)
            coord = entrance["coord"]
            coord_str = str(coord[0]) + "," + str(coord[1]) + "," + str(coord[2])
            enter_lines.append(f"      {entrance_id}:")
            enter_lines.append(f"        presets: _CaveEnter<{name},{coord_str}>")
            exit_lines.append(f"      {entrance_id}:")
            exit_lines.append(f"        presets: _CaveExit<{name},{coord_str}>")

print("  _Enter:")
for x in enter_lines:
    print(x)
print("  _Exit:")
for x in exit_lines:
    print(x)
