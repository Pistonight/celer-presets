# Checks for korok integrity and generate korok presets
# args: path/to/data/koroks.yaml <total_count>

import yaml
import sys

with open(sys.argv[1], "r") as f:
    koroks = yaml.load(f, Loader=yaml.FullLoader)

meta = koroks["meta"]
data = koroks["data"]
total = 900
seed_total = int(sys.argv[2])


# Check for region data
regions = meta["regions"]
def check_regions(regions, data):
    count = 0
    seed_count = 0
    missing = []
    for region_id in sorted(regions):
        region_count = regions[region_id]["count"]
        main_count = region_count["main"]
        sky_count = region_count["sky"] if "sky" in region_count else 0
        count += main_count + sky_count
        for i in range(1,main_count+1):
            korok_id = f"{region_id}{i:02}"
            if korok_id not in data:
                missing.append(korok_id)
                continue
            seed_count += 1
            if data[korok_id]["type"] == "Friends":
                seed_count += 1
        for i in range(1,sky_count+1):
            korok_id = f"{region_id}S{i:02}"
            if korok_id not in data:
                missing.append(korok_id)
                continue
            seed_count += 1
            if data[korok_id]["type"] == "Friend":
                seed_count += 1
    
    if count != total:
        raise ValueError(f"Region korok total count mismatch: {count} != {total}")
    
    if missing:
        for korok_id in missing:
            print(f"  Missing korok: {korok_id}", file=sys.stderr)
        raise ValueError(f"Missing koroks: {len(missing)}")
    
    if seed_count != seed_total:
        raise ValueError(f"Seed korok total count mismatch: {seed_count} != {seed_total}")


check_regions(regions, data)
def fmt_coord(coord):
    return f"[{coord[0]:.2f},{coord[1]:.2f},{coord[2]:.2f}]"

types = meta["types"]
for korok_id in sorted(data):
    print(f"{korok_id}:")
    korok = data[korok_id]
    icon = types[korok["type"]]["icon"]
    name = types[korok["type"]]["name"].replace(")", "\\)")
    print(f"  presets: _Korok<{korok_id} {name},{icon}>")
    if korok["type"] == "Friends":
        print(f"  vars:")
        print(f"    counter-korok: .add(1)")
        print(f"    korok-seed: .add(2)")
    if "comment" in data:
        comment = korok["comment"]
        print(f"  comment: {comment}")
    movements = korok["move"]
    if len(movements) == 1:
        coord_str = fmt_coord(movements[0])
        print(f"  coord: {coord_str}")
    else:
        print(f"  movements:")
        print(f"  - _Korok::{korok_id}::Start")
        for m in movements[1:-1]:
            coord_str = fmt_coord(m)
            print(f"  - {coord_str}")
        print(f"  - _Korok::{korok_id}::End")
        print(f"_{korok_id}:")
        print(f"  Start:")
        if korok["type"] == "Friends":
            print(f"    presets: _KorokFriendStart<{korok_id}>")
        coord_str = fmt_coord(movements[0])
        print(f"    coord: {coord_str}")
        print(f"  End:")
        if korok["type"] == "Friends":
            print(f"    presets: _KorokFriendEnd<{korok_id}>")
        coord_str = fmt_coord(movements[-1])
        print(f"    coord: {coord_str}")