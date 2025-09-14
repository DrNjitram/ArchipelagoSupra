import json
import pkgutil
from typing import NamedTuple

from BaseClasses import ItemClassification


def get_IC(name: str) -> ItemClassification:
    if name in useful:
        return ItemClassification.useful
    elif name in progression:
        return ItemClassification.progression
    elif name in filler:
        return ItemClassification.filler
    elif name in trap:
        return ItemClassification.trap
    else:
        raise Exception(f"Could not find type {name} in item types")

class ItemData(NamedTuple):
    classification: ItemClassification
    count: int
    name: str
    type_name: str

if __name__ == "__main__":
    with open("./data/items.json", "r") as f:
        item_table = json.load(f)
else:
    f = pkgutil.get_data(__name__, "data/items.json").decode("utf-8-sig")
    item_table = json.loads(f)


useful = ["BP_UnlockMap_C", "BuyChestDetector_C", "BuyChestDetectorRadius_C", "BuyGunCriticalDamage_C",
          "BuyGunCriticalDamageChance_C", "BuyGunDamage+15_C", "BuyGunDamage+5_C", "BuyGunRefillSpeed+66_C",
          "BuyGunRefireRate50_C", "BuyGunSpeedx2_C", "BuyHealth+15_C", "BuyHealth+5_C", "BuyHealthRegen_C",
          "BuyHealthRegenMax10_C", "BuyHealthRegenMax5_C", "BuyShieldBreaker_C", "BuyShowProgress_C",
          "BuySmashdownDamage+33_C", "BuyStats_C", "BuySwordCriticalDamageChance_C", "BuySwordDamage+1_C",
          "BuySwordDamage+3_C", "BuyTripleJump_C", "BuyUpgradeChestNum_C", "BuySmashdownRadius+_C", "BuyHealth+2_C",
          "BuyNumberRising_C", "BuyTranslocatorDamagex3_C", "BuyTranslocatorShotForce_C", "BuyGunHoly2_C",
          "BuyTranslocatorCoolDownHalf_C", "MoonTake_C", "BuySwordDamage+02_C", "BuyCrystal_C", "BuySilentFeet_C",
          "BuyGraveDetector_C", "BuyUpgradeGraveNum_C", "BuyMoreLoot_C", "BuyForceBlockTelefrag_C",
          "BuyHealthRegenSpeed_C", "BP_PurchaseHealth+1_C", "BuySwordRange25_C", "BuySwordCriticalDamage_C",
          "BuyShowHealthbar_C", "BuyGunCoin_C", "BuyArmor1_C", "BuySwordRefireRate-33_C", "BuyHeartLuck_C",
          "BuyForceCubeStomp_C", "BuyCoinMagnet_C", "BuySwordHoly2_C", "BuyForceCubeStompGrave3_C", "BuyGunHoly1_C",
          "UpgradeHappiness_C", "BuyGunAltDamagex2_C", "BuyGunComboDamage+25_C", "BuyGunDamage+1_C", "Coin:Chest_C",
          "EnemySpawn1_C", "EnemySpawn2_C", "EnemySpawn3_C", "BP_DoubleHealthLoot_C", "_BuyHealth+10_C",
          "DeadHero2Austin", "DeadHero2Link", "DeadHero3Heman", "DeadHero3Pokemon", "DeadHero4Picard", "DeadHero4Santa",
          "DeadHero4Santa2", "DeadHero4Santa3", "DeadHero_3", "DeadHeroGoku", "DeadHeroGuybrush", "DeadHeroIndy",
          "Shell_C"
          ]
progression = ["BuyBelt_C", "BuyDoubleJump_C", "BuyForceBeamGold_C", "BuyForceBlock_C", "BuyGun1_C", "BuyGunAlt_C",
               "BuySpeedx15_C", "BuySpeedx2_C", "BuySword2_C", "BuySword_C", "BuyTranslocator_C", "BuyWalletx2_C",
               "BuyWalletx15_C", "BuyForceCubeBeam_C", "BuyGunSplashDamage_C", "BuySwordHoly1_C",
               "BuyEnemiesLoot_C", "BuySmashdown_C", "BuyForceBeam_C", "BP_A3_StrengthQuest_C"]
trap = []
filler = ["Coin_C", "CoinBig_C"]


#print(sum([v["count"] for k,v in item_table.items() if "Coin" not in k and "Enemy" not in k])) # 205 without coins and spawns
item_table = {v["id"]: ItemData(get_IC(k), v["count"], v["loc"], k) for k,v in item_table.items()}
#print(item_table)
#print(sum([v.count for v in item_table.values()]))