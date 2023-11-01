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
def process_namespace(namespace, presets, route):
    for id in sorted(presets):
        if id.startswith("_"):
            process_namespace(f"{namespace}::{id[1:]}", presets[id], route)
            continue
        preset = f"{namespace}::{id}"
        route.append({
            preset: [preset]
        })

def process_file(file_path, route):
    with open(file_path, "r") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    presets = config["presets"]
    for id in sorted(presets):
        if id.startswith("_"):
            process_namespace(id, presets[id], route)

for file_path in sys.argv[1:]:
    process_file(file_path, route)

project["route"] = route

with open("project.yaml", "w") as f:
    yaml.dump(project, f)