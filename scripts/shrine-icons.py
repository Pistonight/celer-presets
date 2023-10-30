# Generate the shrine icons blob
# argument: path/to/data/shrines.yaml
import yaml
import sys

with open(sys.argv[1], "r") as f:
    shrines = yaml.load(f, Loader=yaml.FullLoader)
types = shrines["meta"]["types"]
for shrine_type in types:
    icon_id = types[shrine_type]["icon"]
    icon_url = types[shrine_type]["url"]
    print(f"{icon_id}: {icon_url}")