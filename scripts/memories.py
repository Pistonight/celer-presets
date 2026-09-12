# Generate memory presets
# argument: path/to/data/memories.yaml
import yaml
import sys

with open(sys.argv[1], "r") as f:
    memories = yaml.load(f, Loader=yaml.FullLoader)

data = memories["data"]
for memory_id in data:
    typ = data[memory_id]["type"]
    name = data[memory_id]["name"]
    comment = data[memory_id]["comment"]
    coord = data[memory_id]["coord"]
    coord_str = str(coord[0]) + "," + str(coord[1]) + "," + str(coord[2])
    print(f"  {memory_id}:")
    print(f"    presets:")
    print(f"      - _Memory::{memory_id}::Base")
    print(f"      - _Memory::Parts::DefaultSplitConfig")
    print(f"  _{memory_id}:")
    print(f"    Base:")
    print(f"      presets:")
    print(f"        - _Memory::Parts::Base::{typ}<{name},{comment},{coord_str}>")
    print(f"    SplitByDefault:")
    print(f"      presets:")
    print(f"        - _Memory::{memory_id}::Base")
    print(f"        - _Memory::Parts::SplitByDefault")
    print(f"    NoSplitByDefault:")
    print(f"      presets:")
    print(f"        - _Memory::{memory_id}::Base")
    print(f"        - _Memory::Parts::NoSplitByDefault")
    print(f"    NoSplit:")
    print(f"      presets:")
    print(f"        - _Memory::{memory_id}::Base")
    print(f"        - _Memory::Parts::NoSplit")



