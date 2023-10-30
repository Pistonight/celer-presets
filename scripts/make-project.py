# generate a celer project for testing presets
# args: path/to/preset.yaml

import sys
import yaml

preset_path = sys.argv[1]
game = preset_path.split("/")[0]

project = {}
project["title"] = f"Test {preset_path}"
project["version"] = "test"
project["config"] = [
    {
        "plugins": [
            { "use": "variables" }
        ]
    },
    {
        "use": f"./{game}/full.yaml"
    }
]

route = []

with open(preset_path, "r") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
presets = config["presets"]

def process_namespace(namespace, presets, route):
    for id in sorted(presets):
        if id.startswith("_"):
            process_namespace(f"{namespace}::{id[1:]}", presets[id], route)
            continue
        preset = f"{namespace}::{id}"
        route.append({
            preset: [preset]
        })
for id in sorted(presets):
    if id.startswith("_"):
        process_namespace(id, presets[id], route)

project["route"] = route

with open("project.yaml", "w") as f:
    yaml.dump(project, f)