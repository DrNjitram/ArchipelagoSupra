region_list = {}

with open("Supraland Access Sheet - Locations.csv") as f:
    raw_data = f.readlines()

loc_replace = {
    "Lavafield": "Lavafield",
    "Redville": "Redville",
    "Red_Crystal": "Red Crystal",
    "Desert 2": "Desert 2",
    "Suprafield": "Suprafield",
    "Desert1": "Desert 1",
    "Blue_Crystal_Before_Gate": "Blue Crystal - Before Gate",
    "Before_Boss3": "Before Boss 3",
    "in paper hut": "After Green",
    "Before_Chapel": "Before Chapel",
    "Introduction": "Introduction",
    "Blueville": "Blueville",
    "Surprafield": "Surprafield",
    "Farm": "Farm",
    "After_Chapel3": "After Chapel 3",
    "Behind_Blueville": "Behind Blueville",
    "Blue_Crystal_inside": "Blue Crystal - Inside",
    "After_Green": "After_Green",
    "Blue_Crystal_Inside": "Blue Crystal - Inside",
    "After_Chapel4": "After Chapel 4",
    "Before_Purple": "Before Purple",
    "Boss_Arena": "Boss Arena",
    "After_Rattlehag": "After Rattlehag",
    "Green_Crystal": "Green Crystal",
    "Purple_Crystal": "Purple Crystal",
    "Behind_Suprafield": "Behind Suprafield",
    "Desert3": "Desert 3",
    "Boss_Area": "Boss Arena",
    "Carrot_Town": "Carrot Town",
    "Before_Boss2": "Before Boss 2",
    "After_Chapel1": "After Chapel 1",
    "After_Chapel2": "After Chapel 2",
    "Rattlehag": "Rattlehag",
    "Behind_Green": "Behind Green",
    "on top of nugget wall": "Desert 3",
    "Desert": "Desert 1",
    "Under_Cactus": "Under Cactus",
    "Before_Boss": "Before Boss 1",
    "Red Crystal": "Red Crystal",
    "Desert2": "Desert 2",
    "Blue_Crystal_After_Gate": "Blue Crystal - After Gate",
    "Carrot_Field": "Carrot Field",
}

RegionKeys = {
    "Lavafield": "LV",
    "Redville": "RV",
    "Red_Crystal": "RC",
    "Desert 2": "D2",
    "Suprafield": "SF",
    "Desert1": "D1",
    "Blue_Crystal_Before_Gate": "BC_AG",
    "Before_Boss3": "BFB3",
    "in paper hut": "BH_CG",
    "Before_Chapel": "BC",
    "Introduction": "Intro",
    "Blueville": "BV",
    "Surprafield": "SF",
    "Farm": "FR",
    "After_Chapel3": "AF3",
    "Behind_Blueville": "BH_BV",
    "Blue_Crystal_inside": "BC_IN",
    "After_Green": "BH_GC",
    "Blue_Crystal_Inside": "BC_IN",
    "After_Chapel4": "AF4",
    "Before_Purple": "BF_PC",
    "Boss_Arena": "BA",
    "After_Rattlehag": "AF_RH",
    "Green_Crystal": "GC",
    "Purple_Crystal": "PC",
    "Behind_Suprafield": "BSF",
    "Desert3": "D3",
    "Boss_Area": "BA",
    "Carrot_Town": "CT",
    "Before_Boss2": "BFB2",
    "After_Chapel1": "AF1",
    "After_Chapel2": "AF2",
    "Rattlehag": "RH",
    "Behind_Green": "BH_GC",
    "on top of nugget wall": "D3",
    "Desert": "D1",
    "Under_Cactus": "CA",
    "Before_Boss": "BFB1",
    "Red Crystal": "RC",
    "Desert2": "D2",
    "Blue_Crystal_After_Gate": "BC_AG",
    "Carrot_Field": "CT",
}

print(raw_data[0].split(","))
i = 0
for line in raw_data[2:]:
    location = [l.strip() for l in line.strip().split(",")]
    if location[6] in ["Coin_C", "CoinBig_C", "EnemySpawn1_C", "EnemySpawn2_C", "EnemySpawn3_C"]:
        continue
    i+=1
    loc = location[0].replace("+", "_")
    print(f"{loc} = {location[6]}")
    #print(f"{location[0].replace("+", "_")} = \"{loc_replace[location[9]]} - {location[8]}\"")
print(i)
# for line in raw_data[2:]:
#     location = [l.strip() for l in line.strip().split(",")]
#     if location[6] in ["Coin_C", "CoinBig_C", "EnemySpawn1_C", "EnemySpawn2_C", "EnemySpawn3_C"]:
#         continue
#     coins = 0
#     if "coins" in location[10].lower() and "gives" not in location[10].lower():
#         coins = int(location[10].split()[0])
#     if coins:
#         print(f"LocationData(LocationName.{location[0].replace("+", "_")}, RegionName.{RegionKeys[location[9]]}, {coins}),")
#     else:
#         print(
#             f"LocationData(LocationName.{location[0].replace("+", "_")}, RegionName.{RegionKeys[location[9]]}),")

# for line in raw_data[2:]:
#     location = [l.strip() for l in line.strip().split(",")]
#
#     print(f"L.{location[0].replace("+", "_")}: True_(),")

