from dataclasses import dataclass
from enum import Enum
from functools import cached_property
from typing import NamedTuple, TypeAlias
from .constants import BASE_ID, GAME_NAME

from BaseClasses import ItemClassification, Item


class SupralandItem(Item):
    game: str = GAME_NAME

class ItemGroup(str, Enum):
    N = "None"



class ProgressionItem(str, Enum):
    ProgSword = "Progressive Sword"
    Buckle = "Float Buckle"
    ProgSpeedJump = "Progressive Speed/Jumps"
    ProgForceBeam = "Progressive Force Beam"
    ProgCube = "Progressive Cube"
    ProgGun = "Progressive Gun"
    ProgTrans = "Progressive Translocator"
    Wallet15 = "Max Coins x1.5"
    Wallet2 = "Max Coins x2"
    GunAltDamage = "Gun Altfire Damage x2"
    GreenMoon = "Green Moon"
    RedMoon = "Red Moon"
    Loot = "Loot"
    Stomp = "Stomp Shoes"
    Strong = "Strong"
    Happiness = "Happiness"

    Health2 = "Max Health +2"
    Health5 = "Max Health +5"
    Health10 = "Max Health +10"
    Health15 = "Max Health +15"
    GunCritDamage = "Gun Critical Damage"
    GunCritChance = "Gun Critical Change +5%"
    GunDamage1 = "Gun Damage +1"
    GunDamage5 = "Gun Damage +5"
    GunDamage15 = "Gun Damage +15"
    SwordCriticalChance = "Sword Critical Chance +5%"
    SwordDamage1 = "Sword Damage +1"
    SwordDamage2 = "Sword Damage +2"
    SwordDamage3 = "Sword Damage +3"
    GunComboDamage = "Combo Damage +25"
    ProgGraveGun = "Progressive Holy Gun"
    ProgGraveSword = "Progressive Holy Sword"
    Armor = "Armor"
    Shell = "Shell"


class UsefulItem(str, Enum):
    ChestDetector = "Chest Detector"
    ChestDetectorRadius = "Chest Detector Radius x2"
    GunRefill = "Ammo refill speed +66%"
    GunCooldown = "Gun cooldown halved"
    GunProjSpeed = "Gun Projectile Speed x2"
    Health1 = "Max Health +1"
    ProgHealthRegen = "Progressive Health Regen"
    ShieldBreaker = "Shield Breaker"
    ShowProgress = "Awesome-Meter"
    StompDamage = "Stomp Damage +33%"
    SwordCriticalChance = "Sword Critical Chance +5%"
    StompRadius = "Stomp Radius +50cm"
    TransDamage = "Translocator Damage x2"
    TransCooldown = "Translocator Half Cooldown"
    GunSplash = "Gun Splash Damage"
    MoreLoot = "More Loot"
    CubeTelefrag = "Force Cube Telefrag"
    HealthRegenSpeed = "Regeneration Speed x2"
    SwordRange = "Sword Range +25%"
    SwordCritical = "Sword Critical Damage"
    GunCoin = "Gun Picks Up Coins"
    SwordSpeed = "Sword 33% Faster"
    DoubleHealth = "Double Health"
    LotOfCoin1 = "1 Coin"
    LotOfCoin2 = "2 Coins"
    LotOfCoin3 = "3 Coins"
    LotOfCoin5 = "5 Coins"
    LotOfCoin10 = "10 Coins"
    LotOfCoin15 = "15 Coins"
    LotOfCoin30 = "30 Coins"
    LotOfCoin50 = "50 Coins"
    LotOfCoin200 = "200 Coins"


class FillerItem(str, Enum):
    Map = "Map"
    Stats = "Stats"
    ChestCount = "See Chest Count"
    CoinBundle = "Coin Bundle" # Replaces Coin Chests
    EnemyHealth = "Enemy Health"
    Silent = "Silent Feet"
    GraveDetector = "Grave Detector"
    GraveCount = "See Grave Count"
    HealthBar = "Health Bar"
    LootLuck = "LootLuck"
    CoinMagnet = "Coin Magnet"
    Coin = "Coin"
    BigCoin = "BigCoin"
    HeroAustin = "Austin"
    HeroLink = "Link"
    HeroHeman = "Heman"
    HeroAsh = "Ash"
    HeroPicard = "Space Commander Toy"
    HeroSanta = "Hat and Fake Beard"
    HeroVault = "Vault Toy"
    HeroStar = "Hans Yolo"
    HeroMagic = "Magic Boy"
    HeroGoku = "Goku"
    HeroGuy = "Guybrush"
    HeroIndy = "Indy"
    EnemySpawn1 = "Wooden Cross"
    EnemySpawn2 = "Stone Grave"
    EnemySpawn3 = "Volcano"

class TheftItem(str, Enum):
    StolenBuckle = "Float  Buckle"
    StolenGun = "Might MacGuffin"
    StolenJump2 = "Double Jump"
    StolenJump3 = "Triple Jump"
    StolenCube = "Force Cube"
    StolenCoins = "Stolen Coins"

class TrapItem(str, Enum):
    pass

class Events(str, Enum):
    RH = "Rattlehag"
    MB = "Meatbag"

ItemName: TypeAlias = (
    FillerItem | ProgressionItem | UsefulItem | TrapItem | TheftItem
)


class ItemData(NamedTuple):
    name: ItemName
    classification: ItemClassification
    count: int
    group: ItemGroup = ItemGroup.N

@dataclass(frozen=True)
class EarlyItems:
    items: tuple[ItemName, ...] = ()
    @cached_property
    def all(self) -> set[ItemName]:
        return set(self.items)

EARLY_ITEMS = {
    "First_Sword": EarlyItems(items = (
        ProgressionItem.ProgSword,
        ProgressionItem.ProgGun,
        ProgressionItem.ProgTrans,
        ProgressionItem.Stomp
    )),
    "Early_Speed": EarlyItems(items = (
        ProgressionItem.ProgSpeedJump,
    ))
}

ALL_ITEMS: tuple[ItemData, ...] = (
    ItemData(FillerItem.Map, ItemClassification.filler, 1),
    ItemData(ProgressionItem.Buckle, ItemClassification.progression, 1),
    ItemData(UsefulItem.ChestDetector, ItemClassification.useful, 1),
    ItemData(UsefulItem.ChestDetectorRadius, ItemClassification.useful, 1),
    ItemData(ProgressionItem.ProgSpeedJump, ItemClassification.progression, 4), # Does not include Happiness
    ItemData(ProgressionItem.ProgForceBeam, ItemClassification.progression, 3),
    ItemData(ProgressionItem.ProgCube, ItemClassification.progression, 3),
    ItemData(ProgressionItem.ProgGun, ItemClassification.progression, 7),
    ItemData(ProgressionItem.GunCritDamage, ItemClassification.progression, 1),
    ItemData(ProgressionItem.GunCritChance, ItemClassification.progression, 6),
    ItemData(ProgressionItem.GunDamage15, ItemClassification.progression, 1),
    ItemData(ProgressionItem.GunDamage5, ItemClassification.progression, 9),
    ItemData(ProgressionItem.GunDamage1, ItemClassification.progression, 4),
    ItemData(UsefulItem.GunRefill, ItemClassification.useful, 4),
    ItemData(UsefulItem.GunCooldown, ItemClassification.useful, 2),
    ItemData(UsefulItem.GunProjSpeed, ItemClassification.useful, 1),
    ItemData(UsefulItem.Health1, ItemClassification.useful, 1),
    ItemData(ProgressionItem.Health2, ItemClassification.progression, 2),
    ItemData(ProgressionItem.Health5, ItemClassification.progression, 17),
    ItemData(ProgressionItem.Health15, ItemClassification.progression, 5),
    ItemData(UsefulItem.ProgHealthRegen, ItemClassification.useful, 18),
    ItemData(UsefulItem.ShieldBreaker, ItemClassification.useful, 1),
    ItemData(UsefulItem.ShowProgress, ItemClassification.progression, 1),
    ItemData(UsefulItem.StompDamage, ItemClassification.useful, 5),
    ItemData(FillerItem.Stats, ItemClassification.filler, 1),
    ItemData(ProgressionItem.ProgSword, ItemClassification.progression, 2),
    ItemData(UsefulItem.SwordCriticalChance, ItemClassification.useful, 10),
    ItemData(ProgressionItem.SwordDamage1, ItemClassification.progression, 9),
    ItemData(ProgressionItem.SwordDamage2, ItemClassification.progression, 6),
    ItemData(ProgressionItem.SwordDamage3, ItemClassification.progression, 7),
    ItemData(ProgressionItem.ProgTrans, ItemClassification.progression, 2),
    ItemData(FillerItem.ChestCount, ItemClassification.filler, 1),
    ItemData(ProgressionItem.Wallet2, ItemClassification.progression, 5),
    ItemData(ProgressionItem.Wallet15, ItemClassification.progression, 5),
    ItemData(UsefulItem.StompRadius, ItemClassification.useful, 8),
    ItemData(ProgressionItem.GunComboDamage, ItemClassification.progression, 8),
    ItemData(FillerItem.CoinBundle, ItemClassification.filler, 0),
    ItemData(FillerItem.EnemyHealth, ItemClassification.filler, 1),
    ItemData(UsefulItem.TransDamage, ItemClassification.useful, 2),
    ItemData(UsefulItem.TransCooldown, ItemClassification.useful, 1),
    ItemData(ProgressionItem.GreenMoon, ItemClassification.progression, 2),
    ItemData(ProgressionItem.RedMoon, ItemClassification.progression, 6),
    ItemData(UsefulItem.GunSplash, ItemClassification.useful, 1),
    ItemData(ProgressionItem.ProgGraveGun, ItemClassification.progression, 2),
    ItemData(ProgressionItem.ProgGraveSword, ItemClassification.progression, 2),
    ItemData(FillerItem.Silent, ItemClassification.filler, 1),
    ItemData(FillerItem.GraveCount, ItemClassification.filler, 1),
    ItemData(FillerItem.GraveDetector, ItemClassification.filler, 1),
    ItemData(UsefulItem.MoreLoot, ItemClassification.useful, 1),
    ItemData(UsefulItem.CubeTelefrag, ItemClassification.useful, 1),
    ItemData(UsefulItem.HealthRegenSpeed, ItemClassification.useful, 3),
    ItemData(UsefulItem.SwordRange, ItemClassification.useful, 1),
    ItemData(UsefulItem.SwordCritical, ItemClassification.useful, 1),
    ItemData(ProgressionItem.Loot, ItemClassification.progression, 1),
    ItemData(ProgressionItem.Stomp, ItemClassification.progression, 1),
    ItemData(FillerItem.HealthBar, ItemClassification.filler, 1),
    ItemData(UsefulItem.GunCoin, ItemClassification.useful, 1),
    ItemData(ProgressionItem.Armor, ItemClassification.progression, 1),
    ItemData(UsefulItem.SwordSpeed, ItemClassification.useful, 1),
    ItemData(FillerItem.LootLuck, ItemClassification.filler, 1),
    ItemData(FillerItem.CoinMagnet, ItemClassification.filler, 1),
    ItemData(FillerItem.Coin, ItemClassification.filler, 651),
    ItemData(FillerItem.BigCoin, ItemClassification.filler, 83),
    ItemData(FillerItem.HeroAustin, ItemClassification.filler, 1),
    ItemData(FillerItem.HeroLink, ItemClassification.filler, 1),
    ItemData(FillerItem.HeroHeman, ItemClassification.filler, 1),
    ItemData(FillerItem.HeroAsh, ItemClassification.filler, 1),
    ItemData(FillerItem.HeroPicard, ItemClassification.filler, 1),
    ItemData(FillerItem.HeroSanta, ItemClassification.filler, 1),
    ItemData(FillerItem.HeroVault, ItemClassification.filler, 1),
    ItemData(FillerItem.HeroStar, ItemClassification.filler, 1),
    ItemData(FillerItem.HeroMagic, ItemClassification.filler, 1),
    ItemData(FillerItem.HeroGoku, ItemClassification.filler, 1),
    ItemData(FillerItem.HeroGuy, ItemClassification.filler, 1),
    ItemData(FillerItem.HeroIndy, ItemClassification.filler, 1),
    ItemData(FillerItem.EnemySpawn1, ItemClassification.filler, 76),
    ItemData(FillerItem.EnemySpawn2, ItemClassification.filler, 55),
    ItemData(FillerItem.EnemySpawn3, ItemClassification.filler, 67),
    ItemData(UsefulItem.DoubleHealth, ItemClassification.useful, 1),
    ItemData(ProgressionItem.Shell, ItemClassification.progression, 6),
    ItemData(ProgressionItem.Strong, ItemClassification.progression, 1),
    ItemData(ProgressionItem.Happiness, ItemClassification.useful, 1),
    ItemData(TheftItem.StolenBuckle, ItemClassification.progression_skip_balancing, 0),
    ItemData(TheftItem.StolenGun, ItemClassification.progression_skip_balancing, 0),
    ItemData(TheftItem.StolenCube, ItemClassification.progression_skip_balancing, 0),
    ItemData(TheftItem.StolenJump2, ItemClassification.progression_skip_balancing, 0),
    ItemData(TheftItem.StolenJump3, ItemClassification.progression_skip_balancing, 0),
    ItemData(ProgressionItem.Health10, ItemClassification.progression, 1),
    ItemData(TheftItem.StolenCoins, ItemClassification.progression_skip_balancing, 0),
    ItemData(UsefulItem.LotOfCoin1, ItemClassification.useful, 0), # sums to 25
    ItemData(UsefulItem.LotOfCoin2, ItemClassification.useful, 0),
    ItemData(UsefulItem.LotOfCoin3, ItemClassification.useful, 0),
    ItemData(UsefulItem.LotOfCoin5, ItemClassification.useful, 1),
    ItemData(UsefulItem.LotOfCoin10, ItemClassification.useful, 9),
    ItemData(UsefulItem.LotOfCoin15, ItemClassification.useful, 3),
    ItemData(UsefulItem.LotOfCoin30, ItemClassification.useful, 4),
    ItemData(UsefulItem.LotOfCoin50, ItemClassification.useful, 5),
    ItemData(UsefulItem.LotOfCoin200, ItemClassification.useful, 2),
)

item_table = {item.name.value: item for item in ALL_ITEMS}
item_name_to_id: dict[str, int] = {str(data.name.value): int(i) for i, data in enumerate(ALL_ITEMS, start=BASE_ID)}

#print(item_name_to_id["Strong"])
#print(sum(i.count for i in ALL_ITEMS if i.name not in [FillerItem.Coin, FillerItem.BigCoin, FillerItem.EnemySpawn1, FillerItem.EnemySpawn2, FillerItem.EnemySpawn3]))

# for name, val in item_name_to_id.items():
#     print(f"[\"{val}\"] = \"{item_table[name].name.name}\",")
     #print(f"\t{val} = \"{item_table[name].name.name}\",")
    #print(f"\t{item_table[name].name.name} = \"{item_table[name].name.value}\",")

# all_names = [loc.name.value for loc in ALL_ITEMS]
# for loc in ALL_ITEMS:
#     count = all_names.count(loc.name)
#     if count>1:
#         print(loc, count, loc.name)