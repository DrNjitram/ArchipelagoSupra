import json
from collections import defaultdict
from typing import TypedDict

# This file is intended to parse the data as provided by the devs into our various blocks of data we need.
# Map related logic must be manually added
# The output of these files must be added to items.py and locations.py
# Should never need to be regenerated unless the devs update things

# These are all Classes given by buying in shops, finding in the world, etc
item_types = ['BuyForceBeamGold_C', 'BuySpeedx2_C', 'BuyGunCriticalDamage_C', 'BuyGunDamage+5_C',
              'BuyHealthRegenMax5_C', 'CoinBig_C', 'Coin_C', 'Coin:Chest_C', 'BuyWalletx2_C', 'BuyWalletx15_C',
              'BuyUpgradeChestNum_C', 'BuyTripleJump_C', 'BuyTranslocator_C', 'BuySwordDamage+1_C', 'BuySwordDamage+2_C',
              'BuySwordDamage+3_C', 'BuySwordCriticalDamageChance_C', 'BuyStats_C', 'BuySword2_C', 'BuySword_C',
              'BuySpeedx15_C', 'BuySmashdownDamage+33_C', 'BuyShowProgress_C', 'BuyShieldBreaker_C',
              'BuyHealthRegenMax10_C', 'BuyHealthRegen_C', 'BuyHealth+5_C', 'BuyHealth+15_C', 'BuyGunSpeedx2_C',
              'BuyGunRefireRate50_C', 'BuyGunRefillSpeed+66_C', 'BP_UnlockMap_C', 'BuyBelt_C', 'BuyChestDetector_C',
              'BuyChestDetectorRadius_C', 'BuyDoubleJump_C', 'BuyForceBlock_C', 'BuyGun1_C', 'BuyGunAlt_C',
              'BuyGunCriticalDamageChance_C', 'BuyGunDamage+15_C', 'UpgradeHappiness_C', "Shell_C"
              ]
# Other pipe types arent used i think
pipe_types = ['PipesystemNew_C']
# The three spawner types (wooden cross, stone cross, volcano)
enemy_spawner_types = ['EnemySpawn1_C', 'EnemySpawn2_C', 'EnemySpawn3_C']
# All classes that are found in the world, as chests, loose coins, or loose items
location_types = ['Chest_C', 'CoinBig_C', 'Coin_C', 'Coin:Chest_C', 'BuyGunAlt_C', 'BuyStats_C', 'BuySword_C',
                  'BuyTranslocator_C', 'BuyWalletx2_C', 'Juicer_C', "Shell_C", 'DeadHero_C']
# This is to ensure we aren't missing any type of items
ignore_types = ['SmallbuttonQuickOnoff_C', 'DoorStone_C', 'Smallbutton2_C', 'Smallbutton_C', 'Door3_C', 'Lever_C',
                'CarryStones_C', 'ButtonFloor_C', 'BallButton_C', 'BarrelClosed_Blueprint_C', 'BarrelColor_C',
                'BarrelRed_C', 'Battery_C', 'BigButton_C', 'TriggerVolume_C', 'Valve_C','TaskHintGuy_C','SwingingDoor_C',
                'Supraball_C', 'Stone_C', 'Sponge_C', 'SmallbuttonOpenClose_C', 'SmallbuttonWhile_C',
                'SmallbuttonOnceMultipleActors_C', 'SmallbuttonNINE_C', 'SmallbuttonMultipleActors_C',
                'SmallbuttonFlipFlop_C', 'Seed_C', 'SecretFound_C', 'RingColorerFlower_C', 'RingColorer_C',
                'RespawnActor_C', 'RingRusty_C', 'RedGuy_C', 'ProjectileShooter_C', 'Plumbus_C', 'PipeCap_C',
                'PedestalButton_C', 'NomNomFlies_C', 'MinecraftBrick_C', 'MetalBall_C', 'Anvil_C', 'Lighttrigger_C',
                'Lift1_C', 'KeyLock_C', 'KeycardReader_C', 'KeycardColor_C', 'Key_C', 'Juicer_C', 'GoldBlock_C',
                'EnemySpawner_C', 'DoorInverted_C', 'Door_C', 'Door2_C', 'Crystal_C', 'DoorPhysical_C', 'Button_C'
                , 'Pipesystem_C', '_Pickaxe_C']

# We might do something with these later
maybe_types = ['PlayerStart', 'PhysicalCoin_C', 'Jumppad_C',
               'Coin:DestroyablePots_C', 'PipesystemNewDLC_C']


all_types = item_types + pipe_types + enemy_spawner_types + ignore_types + maybe_types + location_types
relevant_types = item_types + pipe_types + enemy_spawner_types + location_types


with open("markers.sl.json") as f:
    markers_sl = json.load(f)
    marker_data = {d["name"]: d for d in markers_sl}

with open("custom-markers.sl.json") as f:
    custom_markers_sl= json.load(f)
    for d in custom_markers_sl:
        if d["name"] in marker_data:
            marker_data[d["name"]] = d | marker_data[d["name"]]
        else:
            marker_data[d["name"]] = d

with open("custom-loc.json") as f:
    custom_loc = json.load(f)

with open("gameClasses.json") as f:
    game_classes = json.load(f)

items = defaultdict(int)
locations = {}
connections = {}
localisation = {}

for d in marker_data.values():
    if d["type"] not in all_types:
        raise Exception(f"Type not found: {d["type"]}. Add to ignore_types if it isn't needed")
    if d["type"] in relevant_types and d["type"] not in game_classes:
        raise Exception(f"Missing Localisation for {d["type"]}")
    if d["type"] not in relevant_types:
        continue


    if d["type"] in location_types:
        if d["type"] == 'Chest_C':
            locations[d["name"]] = {"type": "ChestItem", "item": d["spawns"], "pos": (d["lng"], d["lat"], d["alt"])}
            items[d["spawns"]] += 1
        elif "coins" in d:
            locations[d["name"]] = {"type": "CoinItem", "item": d["type"], "coins": d["coins"], "pos": (d["lng"], d["lat"], d["alt"])}
        elif "Juicer_C" == d["type"]:
            locations[d["name"]] = {"type": "JuicerItem", "item": d["spawns"], "pos": (d["lng"], d["lat"], d["alt"])}
            items[d["spawns"]] += 1
        elif "DeadHero_C" == d["type"]:
            locations[d["name"]] = {"type": "HeroItem", "item": d["name"], "pos": (d["lng"], d["lat"], d["alt"])}
            items[d["name"]] += 1
        else:
            locations[d["name"]] = {"type": "FoundItem", "item": d["type"], "pos": (d["lng"], d["lat"], d["alt"])}
    if "cost" in d:
        locations[d["name"]] = {"type": "ShopItem", "item": d["type"], "cost": d["cost"], "pos": (d["lng"], d["lat"], d["alt"])}
    if d["type"] in enemy_spawner_types:
        locations[d["name"]] = {"type": "EnemySpawner", "item": d["type"], "pos": (d["lng"], d["lat"], d["alt"])}
        items[d["type"]] += 1
    if d["type"] in item_types:
        items[d["type"]] += 1
    if d["type"] in pipe_types:
        connections[d["name"]] = d["other_pipe"]

check_items = defaultdict(int)
for k,v in locations.items():
    if v["item"] not in items:
        print(k,v)
    check_items[v["item"]] += 1
    if "HeroItem" != v["type"]:
        localisation[v["item"]] = game_classes[v["item"]]["friendly"]

localisation |= {
    "DeadHero2Austin" : "Austin",
    "DeadHero2Link" : "Link",
    "DeadHero3Heman" : "Heman",
    "DeadHero3Pokemon" :"Ash",
    "DeadHero4Picard" : "Picard",
    "DeadHero4Santa" : "Santa",
    "DeadHero4Santa2" : "Santa",
    "DeadHero4Santa3" : "Santa",
    "DeadHero_3" : "Hero_3",
    "DeadHeroGoku" : "Goku",
    "DeadHeroGuybrush" :"GuyBrush",
    "DeadHeroIndy" : "Indy"
}

print("Connections", len(connections), connections)
print("Locations", len(locations), locations)
print("Items in item_types", sum(items.values()), items)
print("Items in Locations", sum(check_items.values()), check_items)

# The section below checks that we correctly identify all items and locations
assert(len([d for d in locations.keys() if "Coin" in d]) == items["Coin_C"] + items["CoinBig_C"])
assert(len(locations) == sum(items.values()))
assert(sum(check_items.values()) == sum(items.values()))


for k,v in items.items():
    if k not in check_items:
        print(k,v)
    elif v != check_items[k]:
        print(k, v, check_items[k])


print("Found all items\nWriting locations and items to file.")


locations_json = {k: {"id": i+1, "loc": localisation[v["item"]]} | v for i, (k,v) in enumerate(locations.items())}
items_json = {k: {"id": 2000 + i, "loc": localisation[k], "count": v}  for i, (k,v) in enumerate(items.items())}

with open("locations.json", "w") as location_file:
        json.dump(locations_json, location_file, indent = 6)

with open("items.json", "w") as items_file:
    json.dump(items_json, items_file, indent = 6)










