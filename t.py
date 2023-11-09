# The script is here as a reference for processing/creating the data files
# It is not used after the data files were created

import yaml
import requests
import time
from tqdm import tqdm

RADAR = "https://radar-totk.zeldamods.org"

def hit_radar(path):
    time.sleep(0.1)
    r = requests.get(f"{RADAR}{path}")
    if r.status_code != 200:
        raise Exception(f"Failed to hit radar: {path}")
    return r.json()

def find_starting_block(korok_hash):
    korok_data = hit_radar(f"/obj_by_hash/{korok_hash}")
    map_name = korok_data["map_name"]
    map_type = korok_data["map_type"]

    gen_group = hit_radar(f"/obj/{map_type}/{map_name}/{korok_hash}/gen_group")
    for obj in gen_group:
        if obj["name"] != "FldObj_KorokStartingBlock_A_01":
            continue
        start_hash = obj["data"]["Hash"]
        pos = obj["data"]["Translate"]
        return start_hash, pos
    
def find_flowers(korok_hash):
    korok_data = hit_radar(f"/obj_by_hash/{korok_hash}")
    map_name = korok_data["map_name"]
    map_type = korok_data["map_type"]

    ai_group = hit_radar(f"/obj/{map_type}/{map_name}/{korok_hash}/ai_groups")
    gen_group = hit_radar(f"/obj/{map_type}/{map_name}/{korok_hash}/gen_group")
    if len(ai_group) != 1:
        raise ValueError("ai group count != 1")
    ai_group = ai_group[0]
    is_5 = "TrackingFlower_05" in ai_group["data"]["Logic"]
    is_10 = "TrackingFlower_10" in ai_group["data"]["Logic"]
    if not is_5 and not is_10:
        raise ValueError("no flowers")
    keys = ['29a0_37f6', '196a_cb2f', '196a_c822', '196a_9cde', '53b7_0732'] if is_5 else ['29a0_d827', '196a_3435', '196a_994b', '196a_95b8', '196a_7ed8',
          '196a_5af9', '196a_a1d9', '196a_68c7', '196a_d26c', '53b7_e9c4']
    refs: list = ai_group["data"]["References"]
    flowers = []
    for key in keys:
        ai_flower = next((x for x in refs if x["Id"] == "AiGroup" and x["InstanceName"].endswith(key)), None)
        if ai_flower is None:
            raise ValueError("no flower")
        path = ai_flower["Path"].split("/", 1)[0]
        flower = next((x for x in refs if x["Id"].startswith("Obj_Plant_Korok") and x["Path"].startswith(path)), None)
        flower_hash = f"0x{int(flower['Reference'], 16):016x}"
        flower = next((x for x in gen_group if x["hash_id"] == flower_hash), None)
        flowers.append((flower["pos"], flower_hash))
    return flowers

def find_friend_passenger_and_destination(korok_hash):
    korok_data = hit_radar(f"/obj_by_hash/{korok_hash}")
    map_name = korok_data["map_name"]
    map_type = korok_data["map_type"]

    gen_group = hit_radar(f"/obj/{map_type}/{map_name}/{korok_hash}/gen_group")
    
    dest = None
    source = None
    for obj in gen_group:
        if dest is None and obj["name"] == "KorokCarry_Destination":
            dest = obj["hash_id"], obj["pos"]
        if source is None and obj["name"] == "KorokCarryPassenger_Pair":
            source = obj["hash_id"], obj["pos"]
        if dest is not None and source is not None:
            return source, dest
    if source is None:
        raise ValueError("no source for " + korok_hash)
    raise ValueError("no destination")

def find_lift_rock_type(korok_hash):
    korok_data = hit_radar(f"/obj_by_hash/{korok_hash}")
    map_name = korok_data["map_name"]
    map_type = korok_data["map_type"]

    gen_group = hit_radar(f"/obj/{map_type}/{map_name}/{korok_hash}/gen_group")
    if len(gen_group) == 2:
        for obj in gen_group:
            if "Korok" not in obj["name"] and "LiftRock" not in obj["name"]:
                raise ValueError("bad lift rock")
        return "LiftRock"
    for obj in gen_group:
        if "Obj_Plant_IvyBurn_Korok" in obj["name"]:
             return "LiftRockLeaves"
        if "FldObj_DamagePlant" in obj["name"]:
             return "LiftRockThorns"
        if "IceWall" in obj["name"]:
            if obj["name"] != "IceWall":
                raise ValueError("bad ice wall")
            return "LiftRockIce"

    
    return None

with open("totk/data/koroks.yaml", "r") as f:
    koroks = yaml.load(f, Loader=yaml.FullLoader)["data"]

#region_ids = {}

def coord_str(coord):
    return f"[{coord[0]:.2f}, {coord[1]:.2f}, {coord[2]:.2f}]"

def z_inverted(coord):
    return [coord[0], coord[1], -coord[2]]

for id in tqdm(koroks):
#     if koroks[id]["type"] == "Friends":
#         old_hash = koroks[id]["hash"]
#         source, dest = find_friend_passenger_and_destination(old_hash)
#         koroks[id]["hash"] = source[0]
#         koroks[id]["move"] = [z_inverted(source[1]), z_inverted(dest[1])]
#         print(f"Friends: {id} {old_hash} -> {koroks[id]['hash']}")
    if koroks[id]["type"].startswith("FlowerChase"):
        koroks[id]["move"] = [z_inverted(x) for x in koroks[id]["move"]]

with open("out", "w") as f:
    for id in sorted(koroks):
        f.write(f"  {id}:\n")
        f.write(f"    type: {koroks[id]['type']}\n")
        f.write(f"    hash: \"{koroks[id]['hash']}\"\n")
        m = koroks[id]["move"]
        if not isinstance(m[0], list):
            m = [m]
        if len(m) == 1:
            f.write(f"    move: [{coord_str(m[0])}]\n")
        else:
            f.write(f"    move:\n")
            for coord in m:
                f.write(f"    - {coord_str(coord)}\n")
        if "extra_hashes" in koroks[id]:
            eh = koroks[id]["extra_hashes"]
            if len(eh) == 1:
                f.write(f"    extra_hashes: [\"{eh[0]}\"]\n")
            else:
                f.write(f"    extra_hashes:\n")
                for hash in eh:
                    f.write(f"    - \"{hash}\"\n")