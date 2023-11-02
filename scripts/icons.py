# Generate the icons blob
# argument: path/to/data/xxx.yaml
import yaml
import sys

with open(sys.argv[1], "r") as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
types = data["meta"]["types"]
for t in types:
    icon_id = types[t]["icon"]
    icon_url = types[t]["url"]
    print(f"{icon_id}: {icon_url}")