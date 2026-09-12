# Generate extra warp presets
# args: path/to/warps.yaml

import yaml
import sys

with open(sys.argv[1], "r") as f:
    data = yaml.load(f, Loader=yaml.FullLoader)["data"]
data_namespaced = {}
for w in data:
    namespace = w["name"]
    parent = data_namespaced
    for n in namespace[:-1]:
        if n not in parent:
            parent[n] = {}
        parent = parent[n]
    w["sentinel__"] = True
    parent[namespace[-1]] = w

def print_recur(indent: str, data: dict):
    for key in data:
        if "sentinel__" in data[key]:
            w = data[key]
            name = w["name"][-1]
            ns_name = "::".join(w["name"])
            abbr = w["abbr"]
            typ = w["type"]
            icon = "warp"
            if typ == "WarpDepth":
                icon = "warp-depth"
            coord = w["coord"]
            coord_str = str(coord[0]) + "," + str(coord[1]) + "," + str(coord[2])
            print(f"{indent}{name}:")
            print(f"{indent}  presets:")
            print(f"{indent}    - _Warp::{ns_name}::Base")
            print(f"{indent}    - _Warp::Parts::DefaultSplitConfig")
            print(f"{indent}_{name}:")
            print(f"{indent}  Base:")
            print(f"{indent}    presets: _Warp::Parts::Base3<{abbr},{coord_str}>")
            print(f"{indent}    icon: {icon}")
            print(f"{indent}  SplitByDefault:")
            print(f"{indent}    - _Warp::{ns_name}::Base")
            print(f"{indent}    - _Warp::Parts::SplitByDefault")
            print(f"{indent}  NoSplitByDefault:")
            print(f"{indent}    - _Warp::{ns_name}::Base")
            print(f"{indent}    - _Warp::Parts::NoSplitByDefault")
            print(f"{indent}  NoSplit:")
            print(f"{indent}    - _Warp::{ns_name}::Base")
            print(f"{indent}    - _Warp::Parts::NoSplit")
            continue

        print(f"{indent}_{key}:")
        print_recur(indent + "  ", data[key])
print_recur("", data_namespaced)
