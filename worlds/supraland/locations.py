import json
import pkgutil
from dataclasses import dataclass
from enum import Enum

from .constants import BASE_ID, GAME_NAME
from .regions import RegionName




# This will get pipe openings added later
event_list: list[str] = [
    "Introduction",
    "Blueville Theft",
    "Rattlehag",
    "Final Boss"
]

class LocationGroup(str, Enum):
    C = "Coin"
    BC = "Big Coin"
    Star = "Star" # Gives a star, i think

class LocationName(str, Enum):
    BP_UnlockMap_2 = "Blue Crystal - After Gate - on top of tower"
    BuyBelt2_2 = "Blueville - Shop"
    BuyChestDetector_30 = "Before Boss 1 - Chest Detector Shop"
    BuyChestDetectorRadius = "Redville - Shop - Credits"
    BuyDoubleJump2 = "Blueville - Shop"
    BuyDoubleJump_786 = "Redville - Shop - Barrel at lava"
    BuyForceBeamGold = "Blueville - Shop"
    BuyForceBlock3 = "Blueville - Shop"
    BuyForceBlock_695 = "Desert 1 - Shop - Barrel at launcher"
    BuyGun2_2 = "Blueville - Shop"
    BuyGunAlt_478 = "Suprafield - in lockerrooms"
    BuyGunCriticalDamage_1496 = "Farm - Shop - Standard"
    BuyGunCriticalDamageChance2_1856 = "Surprafield - Shop - Standard"
    BuyGunCriticalDamageChance3_3189 = "Rattlehag - Shop - Standard"
    BuyGunCriticalDamageChance4_198 = "Carrot Town - Shop"
    BuyGunCriticalDamageChance_1426 = "Before Chapel - Shop"
    BuyGunDamage_15_1234 = "After Chapel 1 - Shop - Red barrel on wall"
    BuyGunDamage_5_235 = "Rattlehag - Shop - Standard"
    BuyGunRefillSpeed_66_478 = "Suprafield - Shop - Standard"
    BuyGunRefillSpeed_67_198 = "Carrot Town - Shop"
    BuyGunRefillSpeedx2_374 = "Rattlehag - Shop - Standard"
    BuySilentFeet2 = "After Chapel 1 - Shop - Red Barrel in House"
    BuyGunRefireRate50_506 = "After Chapel 1 - Shop - Red Barrel in trees"
    BuySilentFeet_902 = "After Chapel 1 - Shop - Standard"
    BuyGunSpeedx2_436 = "After Chapel 1 - Shop - Barrel near stomp"
    BuyHealth_15_765 = "Redville - Shop - Barrel on lever"
    BuyHealth_16_457 = "After Chapel 1 - Shop - White Barrel"
    BuyHealth_17 = "Rattlehag - Shop - Standard"
    BuyHealth_5 = "Farm - Shop - Standard"
    BuyHealthRegen2_695 = "Redville - Shop - Barrel behind Red Planks"
    BuyHealthRegenMax10_330 = "Rattlehag - Shop - Standard"
    BuyHealthRegenMax5_1162 = "Carrot Town - Shop"
    BuyShieldBreaker_1026 = "Suprafield - Shop - Standard"
    BuyShowProgress2_2 = "Farm - Shop - Standard"
    BuySmashdownDamage_33 = "Carrot Town - Shop"
    BuySpeedx15_2 = "Redville - Shop - Credits"
    BuySpeedx2_206 = "Redville - Shop - Standard"
    BuyStats = "Redville - Stats"
    BuySword2_2 = "Desert 3 - Moon Sword"
    BuySword_695 = "Introduction - Sword"
    BuySwordCriticalDamageChance2_2395 = "Suprafield - Shop - Standard"
    BuySwordCriticalDamageChance3_296 = "Carrot Town - Shop"
    BuySwordCriticalDamageChance_1657 = "Farm - Shop - Standard"
    BuySwordDamage_11 = "Redville - Shop - Standard"
    BuySwordDamage_10_2 = "Redville - Shop - Standard"
    UpgradeSwordDamageX2_716 = "After Chapel 1 - Shop - Barrel on stump"
    BuyTranslocator_7 = "Green Crystal - Translocator"
    BuyTripleJump2 = "Blueville - Shop"
    BuyTripleJump_877 = "Redville - Shop - Barrel with Double Jump"
    BuyUpgradeChestNum = "Redville - Shop - Credits"
    BuyWalletx15 = "After Chapel 1 - Shop - Standard"
    BuyWalletx16 = "Farm - Shop - Standard"
    BuyWalletx17_426 = "Carrot Town - Shop - Standard"
    BuyWallet_50_737 = "Redville - Shop - Standard"
    BuyWallet_51 = "Redville - Shop - Credits"
    BuyWalletx2_986 = "Desert 2 - Way to Red Crystal"
    Chest100_2221 = "Before Purple - below supraballers house"
    Chest101_2025 = "Before Purple - on top of wooden structure"
    Chest102_2567 = "Carrot Town - behind high cracked block"
    Chest103_3711 = "Before Chapel - next to yellow pipe"
    Chest104_6073 = "After Chapel 4 - on high stone shelf"
    Chest105_6706 = "Before Chapel - chest on high stone ledge"
    Chest106_8060 = "Blue Crystal - After Gate - High ledge next to Crystal"
    Chest107_9218 = "After Chapel 2 - on stone peak"
    Chest108_10670 = "Desert 2 - next to twigs at door"
    Chest109 = "Redville - beneath heavy block"
    Chest110 = "Purple Crystal - behind yellow ball jump"
    Chest111_3 = "Blue Crystal - After Gate - High ledge next to crystal"
    Chest112 = "Redville - behind breakable block"
    Chest113 = "Desert 1 - Behind Carrot"
    Chest116 = "Suprafield - on top of tree stump"
    Chest117_2 = "Blueville - behind cracked block"
    Chest118_2 = "Green Crystal - behind waterfall"
    Chest119_2 = "Lavafield - Gold Nugget House"
    Chest11_13130 = "Redville - House with Green Button"
    Chest120_2 = "Lavafield - on Ledge"
    Chest121_2 = "Green Crystal - next to firepipe"
    Chest122_2 = "After_Green - in blockhouse"
    Chest123_5 = "After_Green - on top of blockhouse"
    Chest124_8 = "Green Crystal - in paper hut"
    Chest125_2 = "After_Green - in blue house"
    Chest126 = "After Rattlehag - inside small hut"
    Chest12_686 = "Desert 1 - Chest behind Cube Door"
    Chest130 = "Blueville - attic of laser house"
    Chest133 = "After_Green - on top of blockhouse behind paper"
    Chest134_13 = "Red Crystal - Cactus Jumps on hill"
    Chest135 = "Behind Suprafield - 2nd floor lockerrroom"
    Chest136_3 = "Red Crystal - bricked house"
    Chest137 = "Red Crystal - behind glass"
    Chest138_5 = "Desert 2 - through small pipe"
    Chest139 = "Rattlehag - on sword"
    Chest13_410 = "Desert 1 - Chest halfway on structure"
    Chest142 = "Suprafield - in pan"
    Chest143 = "After Chapel 1 - after harddrive"
    Chest144 = "Blue Crystal - Inside - Behind door in attic"
    Chest145_2 = "Blue Crystal - Inside - Float Buckle"
    Chest146_2 = "Lavafield - on top of hut"
    Chest147_2 = "Farm - behind metal strips"
    Chest148_5 = "Suprafield - behind metal strips"
    Chest149 = "Redville - behind metal strips"
    Chest14_1121 = "Red Crystal - Gun chest"
    Chest150 = "Blueville - house behind gate"
    Chest151_3 = "Red Crystal - high ledge in corner"
    Chest152_6 = "Boss Arena - high on shelf"
    Chest154 = "Farm - on stone shelf"
    Chest155_2 = "Redville - Chest on ledge near firepipe"
    Chest156_2 = "Blue Crystal - Before Gate - on top of pipe"
    Chest157 = "Redville - behind combat challenge"
    Chest158 = "Behind Blueville - behind water"
    Chest159_6 = "Under Cactus - Volcano Stomp"
    Chest160 = "Before Boss 1 - back of arena"
    Chest161_2 = "Before Boss 1 - in blue house"
    Chest162 = "Redville - Chest in cardboard"
    Chest163 = "Farm - behind blocks"
    Chest164 = "Red Crystal - Beneath glass"
    Chest165 = "Before Purple - hidden chest behind ravine"
    Chest166 = "Before Purple - next to girders"
    Chest167 = "After Rattlehag - on shelf in corner"
    Chest168 = "Boss Arena - in pan"
    Chest169 = "Desert 2 - Chest behind Candle"
    Chest16_5090 = "Behind Suprafield - on dirt ledge"
    Chest170 = "Red Crystal - behind metal door"
    Chest171_2 = "Behind Blueville - beneath throne"
    Chest172 = "Desert 1 - Chest near switch"
    Chest17_812 = "Red Crystal - at lever puzzle on tower"
    Chest18_812 = "Red Crystal - On Hill next to pipe"
    Chest19_6182 = "Red Crystal - Behind Gate in yellow Cave"
    Chest2 = "Desert 2 - Chest behind steel fence"
    Chest20_9041 = "Desert 1 - Chest behind Firepipe near Barrel"
    Chest21_10208 = "Red Crystal - Chest in wood house roof"
    Chest22_11777 = "Introduction - Through fire pipe"
    Chest23_14291 = "Red Crystal - across level"
    Chest24_16178 = "Red Crystal - Cooking Guy Kitchen"
    Chest25_692 = "Red Crystal - at lever puzzle"
    Chest27_4172 = "Redville - Cave Behind House next to Juicer"
    Chest28_4997 = "Desert 3 - above door to Desert2"
    Chest29_7214 = "Red Crystal - In Wood House"
    Chest31_9005 = "Red Crystal - next to house on wall"
    Chest32_1454 = "Redville - Purple Button House"
    Chest33_1094 = "Redville - ceiling of start house"
    Chest35_2137 = "Desert 2 - Next to door"
    Chest36_4639 = "Red Crystal - under gun chest"
    Chest37_1815 = "Desert 1 - Near candle in the back"
    Chest38_3995 = "Red Crystal - Next to metal in distance"
    Chest39_5860 = "Redville - Behind cave with paint machine"
    Chest40_8 = "Rattlehag - on sword"
    Chest41_2 = "Before Boss 2 - behind red planks"
    Chest43 = "Red Crystal - Behind gate in yellow cave"
    Chest44_2721 = "After Chapel 4 - Stomp Shoes"
    Chest45_4075 = "After Chapel 4 - behind stomp blocks"
    Chest46 = "Redville - House with red target"
    Chest47 = "After Chapel 4 - behind metal door"
    Chest4_1544 = "Desert 1 - Above Force Cube barrel"
    Chest51_1360 = "After Chapel 1 - in elevated nook"
    Chest53_1192 = "Blue Crystal - Inside - above yellow ring"
    Chest54_8402 = "After Rattlehag - in stomp house"
    Chest55_3907 = "After Chapel 3 - on floor of cave"
    Chest56_5023 = "After Chapel 4 - behind purple button"
    Chest57_1073 = "Suprafield - behind arena"
    Chest58 = "Redville - Star House"
    Chest59 = "Redville - House with blue roof"
    Chest5_1955 = "Desert 2 - Chest around Trees and Pipes"
    Chest60_2151 = "Red Crystal - Cactus Jumps House"
    Chest61_2816 = "Suprafield - in house on hill"
    Chest62_3729 = "Suprafield - in attic"
    Chest63_1565 = "Blue Crystal - Before Gate - before blue crystal"
    Chest64_1416 = "Blue Crystal - Inside - behind purple rings"
    Chest65_5150 = "Blue Crystal - Inside - behind ball parcourse"
    Chest66_7106 = "Suprafield - behind lockers"
    Chest67 = "Desert 2 - stomp down chest"
    Chest68 = "After Chapel 3 - in cave ceiling"
    Chest6_710 = "Red Crystal - Armor House"
    Chest70 = "Blue Crystal - Inside - through green pipe"
    Chest71 = "Desert 1 - top chest on structure"
    Chest72_2 = "Red Crystal - shot from yellow pipe"
    Chest73_1605 = "Rattlehag - through yellow pipe"
    Chest74 = "Introduction - Chest on top of pipe"
    Chest75 = "Red Crystal - beneath glass pane and chasm"
    Chest76 = "Introduction - Under Coin Chest"
    Chest77_4 = "Purple Crystal - Force Beam"
    Chest78_7640 = "Blue Crystal - Inside - behind hinge"
    Chest79_2 = "Farm - on gum"
    Chest7_818 = "Desert 2 - Loot luck"
    Chest80_1332 = "Before Purple - Moon beyond chasm"
    Chest81 = "Purple Crystal - behind stomp pillar"
    Chest82_4377 = "After Rattlehag - behind yellow ball launch"
    Chest83_1920 = "Carrot Town - behind keylock"
    Chest84_3197 = "After Rattlehag - behind electric lock"
    Chest86_2441 = "Blueville - behind grate"
    Chest87 = "Suprafield - attic opposite lockerroom"
    Chest88_1696 = "Carrot Town - behind ball parkour"
    Chest89_3036 = "Carrot Town - behind key house"
    Chest8_878 = "Desert 2 - Near Link"
    Chest90_2137 = "Purple Crystal - behind cardboard"
    Chest91 = "After Chapel 1 - behind green key"
    Chest92 = "Rattlehag - behind graves"
    Chest93_3307 = "Red Crystal - Shell Dude"
    Chest94 = "After Chapel 3 - on dirt shelf"
    Chest95_6394 = "Blue Crystal - Before Gate - below stomp planks"
    Chest96_8035 = "Blue Crystal - After Gate - in grass on ledge"
    Chest97_9186 = "Carrot Town - beneath stomp glass"
    Chest98_10407 = "Carrot Town - ceiling under glass"
    Chest99_2116 = "Carrot Town - hidden next to carrots"
    UpgradeHappiness2_2 = "Redville - Shop - Barrel behind combat"
    Juicer2 = "Farm - in basement"
    Juicer3 = "Redville - Juicer"
    Juicer_286 = "Carrot Town - Strong"
    Shell13_3781 = "Red Crystal - Cooking Guy Kitchen"
    Shell16_5895 = "Red Crystal - Open nook"
    Shell2_1957 = "Red Crystal - under structure"
    Shell5_1015 = "Red Crystal - behind metal door"
    Shell9_2044 = "Red Crystal - next to tree"
    Shell_1483 = "Red Crystal - hidden cave"
    DeadHero2Austin = "After Chapel 2 - behind carrot"
    DeadHero2Link = "Desert 2 - Chest8_878"
    DeadHero3Heman = "Desert 3 - on top of rock"
    DeadHero3Pokemon = "Blue Crystal - Inside - inside tube"
    DeadHero4Picard = "After Chapel 2 - on high stone ledge"
    DeadHero4Santa = "Before Purple - on supraballers House"
    DeadHero4Santa2 = "Before Purple - in flooded valley"
    DeadHero4Santa3 = "Boss Arena - next to farm"
    DeadHero_3 = "Blueville - on roof"
    DeadHeroGoku = "Lavafield - ForceBeam3 & BuyForceCube_C & HeightIncrease3 & BuyBelt_C"
    DeadHeroGuybrush = "Suprafield - behind arena"
    DeadHeroIndy = "Red Crystal - next to purple button"

@dataclass(frozen=True)
class LocationData:
    name: LocationName
    region: RegionName
    description: str = ""
    group: LocationGroup = LocationGroup.Star

ALL_LOCATIONS: tuple[LocationData, ...] = (
    LocationData(LocationName.BP_UnlockMap_2, RegionName.BC_AG),
    LocationData(LocationName.BuyBelt2_2, RegionName.BV),
    LocationData(LocationName.BuyChestDetector_30, RegionName.BFB1),
    LocationData(LocationName.BuyChestDetectorRadius, RegionName.RV),
    LocationData(LocationName.BuyDoubleJump2, RegionName.BV),
    LocationData(LocationName.BuyDoubleJump_786, RegionName.RV),
    LocationData(LocationName.BuyForceBeamGold, RegionName.BV),
    LocationData(LocationName.BuyForceBlock3, RegionName.BV),
    LocationData(LocationName.BuyForceBlock_695, RegionName.D1),
    LocationData(LocationName.BuyGun2_2, RegionName.BV),
    LocationData(LocationName.BuyGunAlt_478, RegionName.SF),
    LocationData(LocationName.BuyGunCriticalDamage_1496, RegionName.FR),
    LocationData(LocationName.BuyGunCriticalDamageChance2_1856, RegionName.SF),
    LocationData(LocationName.BuyGunCriticalDamageChance3_3189, RegionName.RH),
    LocationData(LocationName.BuyGunCriticalDamageChance4_198, RegionName.CT),
    LocationData(LocationName.BuyGunCriticalDamageChance_1426, RegionName.BC),
    LocationData(LocationName.BuyGunDamage_15_1234, RegionName.AF1),
    LocationData(LocationName.BuyGunDamage_5_235, RegionName.RH),
    LocationData(LocationName.BuyGunRefillSpeed_66_478, RegionName.SF),
    LocationData(LocationName.BuyGunRefillSpeed_67_198, RegionName.CT),
    LocationData(LocationName.BuyGunRefillSpeedx2_374, RegionName.RH),
    LocationData(LocationName.BuySilentFeet2, RegionName.AF1),
    LocationData(LocationName.BuyGunRefireRate50_506, RegionName.AF1),
    LocationData(LocationName.BuySilentFeet_902, RegionName.AF1),
    LocationData(LocationName.BuyGunSpeedx2_436, RegionName.AF1),
    LocationData(LocationName.BuyHealth_15_765, RegionName.RV),
    LocationData(LocationName.BuyHealth_16_457, RegionName.AF1),
    LocationData(LocationName.BuyHealth_17, RegionName.RH),
    LocationData(LocationName.BuyHealth_5, RegionName.FR),
    LocationData(LocationName.BuyHealthRegen2_695, RegionName.RV),
    LocationData(LocationName.BuyHealthRegenMax10_330, RegionName.RH),
    LocationData(LocationName.BuyHealthRegenMax5_1162, RegionName.CT),
    LocationData(LocationName.BuyShieldBreaker_1026, RegionName.SF),
    LocationData(LocationName.BuyShowProgress2_2, RegionName.FR),
    LocationData(LocationName.BuySmashdownDamage_33, RegionName.CT),
    LocationData(LocationName.BuySpeedx15_2, RegionName.RV),
    LocationData(LocationName.BuySpeedx2_206, RegionName.RV),
    LocationData(LocationName.BuyStats, RegionName.RV),
    LocationData(LocationName.BuySword2_2, RegionName.D3),
    LocationData(LocationName.BuySword_695, RegionName.Intro),
    LocationData(LocationName.BuySwordCriticalDamageChance2_2395, RegionName.SF),
    LocationData(LocationName.BuySwordCriticalDamageChance3_296, RegionName.CT),
    LocationData(LocationName.BuySwordCriticalDamageChance_1657, RegionName.FR),
    LocationData(LocationName.BuySwordDamage_11, RegionName.RV),
    LocationData(LocationName.BuySwordDamage_10_2, RegionName.RV),
    LocationData(LocationName.UpgradeSwordDamageX2_716, RegionName.AF1),
    LocationData(LocationName.BuyTranslocator_7, RegionName.GC),
    LocationData(LocationName.BuyTripleJump2, RegionName.BV),
    LocationData(LocationName.BuyTripleJump_877, RegionName.RV),
    LocationData(LocationName.BuyUpgradeChestNum, RegionName.RV),
    LocationData(LocationName.BuyWalletx15, RegionName.AF1),
    LocationData(LocationName.BuyWalletx16, RegionName.FR),
    LocationData(LocationName.BuyWalletx17_426, RegionName.CT),
    LocationData(LocationName.BuyWallet_50_737, RegionName.RV),
    LocationData(LocationName.BuyWallet_51, RegionName.RV),
    LocationData(LocationName.BuyWalletx2_986, RegionName.D2),
    LocationData(LocationName.Chest100_2221, RegionName.BF_PC),
    LocationData(LocationName.Chest101_2025, RegionName.BF_PC),
    LocationData(LocationName.Chest102_2567, RegionName.CT),
    LocationData(LocationName.Chest103_3711, RegionName.BC),
    LocationData(LocationName.Chest104_6073, RegionName.AF4),
    LocationData(LocationName.Chest105_6706, RegionName.BC),
    LocationData(LocationName.Chest106_8060, RegionName.BC_AG),
    LocationData(LocationName.Chest107_9218, RegionName.AF2),
    LocationData(LocationName.Chest108_10670, RegionName.D2),
    LocationData(LocationName.Chest109, RegionName.RV),
    LocationData(LocationName.Chest110, RegionName.PC),
    LocationData(LocationName.Chest111_3, RegionName.BC_AG),
    LocationData(LocationName.Chest112, RegionName.RV),
    LocationData(LocationName.Chest113, RegionName.D1),
    LocationData(LocationName.Chest116, RegionName.SF),
    LocationData(LocationName.Chest117_2, RegionName.BV),
    LocationData(LocationName.Chest118_2, RegionName.GC),
    LocationData(LocationName.Chest119_2, RegionName.LV),
    LocationData(LocationName.Chest11_13130, RegionName.RV),
    LocationData(LocationName.Chest120_2, RegionName.LV),
    LocationData(LocationName.Chest121_2, RegionName.GC),
    LocationData(LocationName.Chest122_2, RegionName.BH_GC),
    LocationData(LocationName.Chest123_5, RegionName.BH_GC),
    LocationData(LocationName.Chest124_8, RegionName.GC),
    LocationData(LocationName.Chest125_2, RegionName.BH_GC),
    LocationData(LocationName.Chest126, RegionName.AF_RH),
    LocationData(LocationName.Chest12_686, RegionName.D1),
    LocationData(LocationName.Chest130, RegionName.BV),
    LocationData(LocationName.Chest133, RegionName.BH_GC),
    LocationData(LocationName.Chest134_13, RegionName.RC),
    LocationData(LocationName.Chest135, RegionName.BSF),
    LocationData(LocationName.Chest136_3, RegionName.RC),
    LocationData(LocationName.Chest137, RegionName.RC),
    LocationData(LocationName.Chest138_5, RegionName.D2),
    LocationData(LocationName.Chest139, RegionName.RH),
    LocationData(LocationName.Chest13_410, RegionName.D1),
    LocationData(LocationName.Chest142, RegionName.SF),
    LocationData(LocationName.Chest143, RegionName.AF1),
    LocationData(LocationName.Chest144, RegionName.BC_IN),
    LocationData(LocationName.Chest145_2, RegionName.BC_IN),
    LocationData(LocationName.Chest146_2, RegionName.LV),
    LocationData(LocationName.Chest147_2, RegionName.FR),
    LocationData(LocationName.Chest148_5, RegionName.SF),
    LocationData(LocationName.Chest149, RegionName.RV),
    LocationData(LocationName.Chest14_1121, RegionName.RC),
    LocationData(LocationName.Chest150, RegionName.BV),
    LocationData(LocationName.Chest151_3, RegionName.RC),
    LocationData(LocationName.Chest152_6, RegionName.BA),
    LocationData(LocationName.Chest154, RegionName.FR),
    LocationData(LocationName.Chest155_2, RegionName.RV),
    LocationData(LocationName.Chest156_2, RegionName.BC_AG),
    LocationData(LocationName.Chest157, RegionName.RV),
    LocationData(LocationName.Chest158, RegionName.BH_BV),
    LocationData(LocationName.Chest159_6, RegionName.CA),
    LocationData(LocationName.Chest160, RegionName.BFB1),
    LocationData(LocationName.Chest161_2, RegionName.BFB1),
    LocationData(LocationName.Chest162, RegionName.RV),
    LocationData(LocationName.Chest163, RegionName.FR),
    LocationData(LocationName.Chest164, RegionName.RC),
    LocationData(LocationName.Chest165, RegionName.BF_PC),
    LocationData(LocationName.Chest166, RegionName.BF_PC),
    LocationData(LocationName.Chest167, RegionName.AF_RH),
    LocationData(LocationName.Chest168, RegionName.BA),
    LocationData(LocationName.Chest169, RegionName.D2),
    LocationData(LocationName.Chest16_5090, RegionName.BSF),
    LocationData(LocationName.Chest170, RegionName.RC),
    LocationData(LocationName.Chest171_2, RegionName.BH_BV),
    LocationData(LocationName.Chest172, RegionName.D1),
    LocationData(LocationName.Chest17_812, RegionName.RC),
    LocationData(LocationName.Chest18_812, RegionName.RC),
    LocationData(LocationName.Chest19_6182, RegionName.RC),
    LocationData(LocationName.Chest2, RegionName.D2),
    LocationData(LocationName.Chest20_9041, RegionName.D1),
    LocationData(LocationName.Chest21_10208, RegionName.RC),
    LocationData(LocationName.Chest22_11777, RegionName.Intro),
    LocationData(LocationName.Chest23_14291, RegionName.RC),
    LocationData(LocationName.Chest24_16178, RegionName.RC),
    LocationData(LocationName.Chest25_692, RegionName.RC),
    LocationData(LocationName.Chest27_4172, RegionName.RV),
    LocationData(LocationName.Chest28_4997, RegionName.D3),
    LocationData(LocationName.Chest29_7214, RegionName.RC),
    LocationData(LocationName.Chest31_9005, RegionName.RC),
    LocationData(LocationName.Chest32_1454, RegionName.RV),
    LocationData(LocationName.Chest33_1094, RegionName.RV),
    LocationData(LocationName.Chest35_2137, RegionName.D2),
    LocationData(LocationName.Chest36_4639, RegionName.RC),
    LocationData(LocationName.Chest37_1815, RegionName.D1),
    LocationData(LocationName.Chest38_3995, RegionName.RC),
    LocationData(LocationName.Chest39_5860, RegionName.RV),
    LocationData(LocationName.Chest40_8, RegionName.RH),
    LocationData(LocationName.Chest41_2, RegionName.BFB2),
    LocationData(LocationName.Chest43, RegionName.RC),
    LocationData(LocationName.Chest44_2721, RegionName.AF4),
    LocationData(LocationName.Chest45_4075, RegionName.AF4),
    LocationData(LocationName.Chest46, RegionName.RV),
    LocationData(LocationName.Chest47, RegionName.AF4),
    LocationData(LocationName.Chest4_1544, RegionName.D1),
    LocationData(LocationName.Chest51_1360, RegionName.AF1),
    LocationData(LocationName.Chest53_1192, RegionName.BC_IN),
    LocationData(LocationName.Chest54_8402, RegionName.AF_RH),
    LocationData(LocationName.Chest55_3907, RegionName.AF3),
    LocationData(LocationName.Chest56_5023, RegionName.AF4),
    LocationData(LocationName.Chest57_1073, RegionName.SF),
    LocationData(LocationName.Chest58, RegionName.RV),
    LocationData(LocationName.Chest59, RegionName.RV),
    LocationData(LocationName.Chest5_1955, RegionName.D2),
    LocationData(LocationName.Chest60_2151, RegionName.RC),
    LocationData(LocationName.Chest61_2816, RegionName.SF),
    LocationData(LocationName.Chest62_3729, RegionName.SF),
    LocationData(LocationName.Chest63_1565, RegionName.BC_AG),
    LocationData(LocationName.Chest64_1416, RegionName.BC_IN),
    LocationData(LocationName.Chest65_5150, RegionName.BC_IN),
    LocationData(LocationName.Chest66_7106, RegionName.SF),
    LocationData(LocationName.Chest67, RegionName.D2),
    LocationData(LocationName.Chest68, RegionName.AF3),
    LocationData(LocationName.Chest6_710, RegionName.RC),
    LocationData(LocationName.Chest70, RegionName.BC_IN),
    LocationData(LocationName.Chest71, RegionName.D1),
    LocationData(LocationName.Chest72_2, RegionName.RC),
    LocationData(LocationName.Chest73_1605, RegionName.RH),
    LocationData(LocationName.Chest74, RegionName.Intro),
    LocationData(LocationName.Chest75, RegionName.RC),
    LocationData(LocationName.Chest76, RegionName.Intro),
    LocationData(LocationName.Chest77_4, RegionName.PC),
    LocationData(LocationName.Chest78_7640, RegionName.BC_IN),
    LocationData(LocationName.Chest79_2, RegionName.FR),
    LocationData(LocationName.Chest7_818, RegionName.D2),
    LocationData(LocationName.Chest80_1332, RegionName.BF_PC),
    LocationData(LocationName.Chest81, RegionName.PC),
    LocationData(LocationName.Chest82_4377, RegionName.AF_RH),
    LocationData(LocationName.Chest83_1920, RegionName.CT),
    LocationData(LocationName.Chest84_3197, RegionName.AF_RH),
    LocationData(LocationName.Chest86_2441, RegionName.BV),
    LocationData(LocationName.Chest87, RegionName.SF),
    LocationData(LocationName.Chest88_1696, RegionName.CT),
    LocationData(LocationName.Chest89_3036, RegionName.CT),
    LocationData(LocationName.Chest8_878, RegionName.D2),
    LocationData(LocationName.Chest90_2137, RegionName.PC),
    LocationData(LocationName.Chest91, RegionName.AF1),
    LocationData(LocationName.Chest92, RegionName.RH),
    LocationData(LocationName.Chest93_3307, RegionName.RC),
    LocationData(LocationName.Chest94, RegionName.AF3),
    LocationData(LocationName.Chest95_6394, RegionName.BC_AG),
    LocationData(LocationName.Chest96_8035, RegionName.BC_AG),
    LocationData(LocationName.Chest97_9186, RegionName.CT),
    LocationData(LocationName.Chest98_10407, RegionName.CT),
    LocationData(LocationName.Chest99_2116, RegionName.CT),
    LocationData(LocationName.UpgradeHappiness2_2, RegionName.RV),
    LocationData(LocationName.Juicer2, RegionName.FR),
    LocationData(LocationName.Juicer3, RegionName.RV),
    LocationData(LocationName.Juicer_286, RegionName.CT),
    LocationData(LocationName.Shell13_3781, RegionName.RC),
    LocationData(LocationName.Shell16_5895, RegionName.RC),
    LocationData(LocationName.Shell2_1957, RegionName.RC),
    LocationData(LocationName.Shell5_1015, RegionName.RC),
    LocationData(LocationName.Shell9_2044, RegionName.RC),
    LocationData(LocationName.Shell_1483, RegionName.RC),
    LocationData(LocationName.DeadHero2Austin, RegionName.AF2),
    LocationData(LocationName.DeadHero2Link, RegionName.D2),
    LocationData(LocationName.DeadHero3Heman, RegionName.D3),
    LocationData(LocationName.DeadHero3Pokemon, RegionName.BC_IN),
    LocationData(LocationName.DeadHero4Picard, RegionName.AF2),
    LocationData(LocationName.DeadHero4Santa, RegionName.BF_PC),
    LocationData(LocationName.DeadHero4Santa2, RegionName.BF_PC),
    LocationData(LocationName.DeadHero4Santa3, RegionName.BA),
    LocationData(LocationName.DeadHero_3, RegionName.BV),
    LocationData(LocationName.DeadHeroGoku, RegionName.LV),
    LocationData(LocationName.DeadHeroGuybrush, RegionName.SF),
    LocationData(LocationName.DeadHeroIndy, RegionName.RC),
)

location_table = {location.name.value: location for location in ALL_LOCATIONS}
location_name_to_id: dict[str, int] = {data.name.value: i for i, data in enumerate(ALL_LOCATIONS, start=BASE_ID)}