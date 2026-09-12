# Generate tower warp presets
# args: path/to/towers.yaml

import yaml
import sys

with open(sys.argv[1], "r") as f:
    towers = yaml.load(f, Loader=yaml.FullLoader)["data"]

print("_Tower:")
for tower_id in towers:
    tower = towers[tower_id]
    name = towers[tower_id]["name"]
    coord = towers[tower_id]["coord"]
    coord_str = str(coord[0]) + "," + str(coord[1]) + "," + str(coord[2])
    print(f"  {tower_id}:")
    print(f"    presets: _Tower<{name},{coord_str}>")
print("_Warp:")
print("  _Tower:")
for tower_id in towers:
    tower = towers[tower_id]
    abbr = towers[tower_id]["abbr"]
    coord = towers[tower_id]["coord"]
    coord_str = str(coord[0]) + "," + str(coord[1]) + "," + str(coord[2])
    print(f"    {tower_id}:")
    print(f"      presets:");
    print(f"        - _Warp::Tower::{tower_id}::Base")
    print(f"        - _Warp::Parts::DefaultSplitConfig")
    print(f"    _{tower_id}:")
    print(f"      Base:")
    print(f"        presets: _Warp::Parts::Base3<{abbr} Twr.,{coord_str}>")
    print(f"      SplitByDefault:")
    print(f"        - _Warp::{tower_id}::Base")
    print(f"        - _Warp::Parts::SplitByDefault")
    print(f"      NoSplitByDefault:")
    print(f"        - _Warp::{tower_id}::Base")
    print(f"        - _Warp::Parts::NoSplitByDefault")
    print(f"      NoSplit:")
    print(f"        - _Warp::{tower_id}::Base")
    print(f"        - _Warp::Parts::NoSplit")
