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
            if data[korok_id]["type"] == "Friend":
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
