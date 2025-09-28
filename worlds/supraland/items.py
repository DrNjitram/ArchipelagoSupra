from enum import Enum
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
    ProgForceBeam = "Progressive Force Beams"
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


class UsefulItem(str, Enum):
    ChestDetector = "Chest Detector"
    ChestDetectorRadius = "Chest Detector Radius x2"
    GunCritDamage = "Gun Critical Damage"
    GunCritChance = "Gun Critical Change +5%"
    GunDamage1 = "Gun Damage +1"
    GunDamage5 = "Gun Damage +5"
    GunDamage15 = "Gun Damage +15"
    GunRefill = "Ammo refill speed +66%"
    GunCooldown = "Gun cooldown halved"
    GunProjSpeed = "Gun Projectile Speed x2"
    Health1 = "Max Health +1"
    Health2 = "Max Health +2"
    Health5 = "Max Health +5"
    Health15 = "Max Health +15"
    ProgHealthRegen = "Progressive Health Regen"
    ShieldBreaker = "Shield Breaker"
    ShowProgress = "Awesome-Meter"
    StompDamage = "Stomp Damage +33%"
    SwordCriticalChance = "Sword Critical Chance +5%"
    SwordDamage1 = "Sword Damage +1"
    SwordDamage2 = "Sword Damage +2"
    SwordDamage3 = "Sword Damage +3"
    StompRadius = "Stomp Radius +50cm"
    GunComboDamage = "Combo Damage +25"
    TransDamage = "Translocator Damage x2"
    TransCooldown = "Translocator Half Cooldown"
    GunSplash = "Gun Splash Damage"
    ProgGraveGun = "Progressive Holy Gun"
    ProgGraveSword = "Progressive Holy Sword"
    MoreLoot = "More Loot"
    CubeTelefrag = "Force Cube Telefrag"
    HealthRegenSpeed = "Regeneration Speed x2"
    SwordRange = "Sword Range +25%"
    SwordCritical = "Sword Critical Damage"
    GunCoin = "Gun Picks Up Coins"
    Armor = "Armor"
    SwordSpeed = "Sword 33% Faster"
    DoubleHealth = "Double Health"
    Shell = "Shell"



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


class TrapItem(str, Enum):
    pass

class Events(str, Enum):
    RH = "Rattlehag"
    MB = "Meatbag"

ItemName: TypeAlias = (
    FillerItem | ProgressionItem | UsefulItem | TrapItem
)


class ItemData(NamedTuple):
    name: ItemName
    classification: ItemClassification
    count: int
    group: ItemGroup = ItemGroup.N



ALL_ITEMS: tuple[ItemData, ...] = (
    ItemData(FillerItem.Map, ItemClassification.filler, 1),
    ItemData(ProgressionItem.Buckle, ItemClassification.progression, 1),
    ItemData(UsefulItem.ChestDetector, ItemClassification.useful, 1),
    ItemData(UsefulItem.ChestDetectorRadius, ItemClassification.useful, 1),
    ItemData(ProgressionItem.ProgSpeedJump, ItemClassification.progression, 4), # Does not include Happiness
    ItemData(ProgressionItem.ProgForceBeam, ItemClassification.progression, 3),
    ItemData(ProgressionItem.ProgCube, ItemClassification.progression, 3),
    ItemData(ProgressionItem.ProgGun, ItemClassification.progression, 7),
    ItemData(UsefulItem.GunCritDamage, ItemClassification.useful, 1),
    ItemData(UsefulItem.GunCritChance, ItemClassification.useful, 6),
    ItemData(UsefulItem.GunDamage15, ItemClassification.useful, 1),
    ItemData(UsefulItem.GunDamage5, ItemClassification.useful, 9),
    ItemData(UsefulItem.GunDamage1, ItemClassification.useful, 4),
    ItemData(UsefulItem.GunRefill, ItemClassification.useful, 4),
    ItemData(UsefulItem.GunCooldown, ItemClassification.useful, 2),
    ItemData(UsefulItem.GunProjSpeed, ItemClassification.useful, 1),
    ItemData(UsefulItem.Health1, ItemClassification.useful, 1),
    ItemData(UsefulItem.Health2, ItemClassification.useful, 2),
    ItemData(UsefulItem.Health5, ItemClassification.useful, 17),
    ItemData(UsefulItem.Health15, ItemClassification.useful, 5),
    ItemData(UsefulItem.ProgHealthRegen, ItemClassification.useful, 18),
    ItemData(UsefulItem.ShieldBreaker, ItemClassification.useful, 1),
    ItemData(UsefulItem.ShowProgress, ItemClassification.useful, 1),
    ItemData(UsefulItem.StompDamage, ItemClassification.useful, 5),
    ItemData(FillerItem.Stats, ItemClassification.filler, 1),
    ItemData(ProgressionItem.ProgSword, ItemClassification.progression, 2),
    ItemData(UsefulItem.SwordCriticalChance, ItemClassification.useful, 10),
    ItemData(UsefulItem.SwordDamage1, ItemClassification.useful, 9),
    ItemData(UsefulItem.SwordDamage2, ItemClassification.useful, 6),
    ItemData(UsefulItem.SwordDamage3, ItemClassification.useful, 7),
    ItemData(ProgressionItem.ProgTrans, ItemClassification.progression, 2),
    ItemData(FillerItem.ChestCount, ItemClassification.filler, 1),
    ItemData(ProgressionItem.Wallet2, ItemClassification.progression, 5),
    ItemData(ProgressionItem.Wallet15, ItemClassification.progression, 5),
    ItemData(UsefulItem.StompRadius, ItemClassification.useful, 8),
    ItemData(UsefulItem.GunComboDamage, ItemClassification.useful, 8),
    ItemData(FillerItem.CoinBundle, ItemClassification.filler, 25),
    ItemData(FillerItem.EnemyHealth, ItemClassification.filler, 1),
    ItemData(UsefulItem.TransDamage, ItemClassification.useful, 2),
    ItemData(UsefulItem.TransCooldown, ItemClassification.useful, 1),
    ItemData(ProgressionItem.GunAltDamage, ItemClassification.progression, 5),
    ItemData(ProgressionItem.GreenMoon, ItemClassification.progression, 2),
    ItemData(ProgressionItem.RedMoon, ItemClassification.progression, 6),
    ItemData(UsefulItem.GunSplash, ItemClassification.useful, 1),
    ItemData(UsefulItem.ProgGraveGun, ItemClassification.useful, 2),
    ItemData(UsefulItem.ProgGraveSword, ItemClassification.useful, 2),
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
    ItemData(UsefulItem.Armor, ItemClassification.useful, 1),
    ItemData(UsefulItem.SwordSpeed, ItemClassification.useful, 1),
    ItemData(FillerItem.LootLuck, ItemClassification.filler, 1),
    ItemData(FillerItem.CoinMagnet, ItemClassification.filler, 1),
    # ItemData(FillerItem.Coin, ItemClassification.filler, 651),
    # ItemData(FillerItem.BigCoin, ItemClassification.filler, 83),
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
    # ItemData(FillerItem.EnemySpawn1, ItemClassification.filler, 76),
    # ItemData(FillerItem.EnemySpawn2, ItemClassification.filler, 55),
    # ItemData(FillerItem.EnemySpawn3, ItemClassification.filler, 67),
    ItemData(UsefulItem.DoubleHealth, ItemClassification.useful, 1),
    ItemData(UsefulItem.Shell, ItemClassification.useful, 6),
    ItemData(ProgressionItem.Strong, ItemClassification.progression, 1),
    #ItemData(ProgressionItem.Happiness, ItemClassification.progression, 1),
)

item_table = {item.name.value: item for item in ALL_ITEMS}
item_name_to_id: dict[str, int] = {data.name.value: i for i, data in enumerate(ALL_ITEMS, start=BASE_ID)}

#print(sum(i.count for i in ALL_ITEMS))