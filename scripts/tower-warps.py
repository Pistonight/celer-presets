# Generate tower warp presets
# args: path/to/towers.yaml

import yaml
import sys

with open(sys.argv[1], "r") as f:
    towers = yaml.load(f, Loader=yaml.FullLoader)["presets"]["_Tower"]


for tower_id in towers:
    preset = towers[tower_id]["presets"]
    preset = preset.replace("_Tower", "_Warp3", 1)
    preset = preset.replace(",", " Tower,", 1)
    print(f"{tower_id}:")
    print(f"  presets: {preset}")