from dataclasses import dataclass
from enum import Enum

class RegionName(str, Enum):
    Intro = "Introduction"
    RV = "Redville"
    D1 = "Desert North"
    D2 = "Desert Middle"
    D3 = "Desert South"
    RC = "Red Crystal"
    LV = "Lavafield"
    GC = "Green Crystal"
    BH_GC = "Behind Green Crystal"
    FR = "Farm"
    BC = "Before Chapel"
    AF1 = "After Chapel 1"
    AF2 = "After Chapel 2"
    AF3 = "After Chapel 3"
    AF4 = "After Chapel 4"
    SF = "Suprafield"
    BSF = "Behind Suprafield"
    BC_BG = "Blue Crystal - Before Gate"
    BC_AG = "Blue Crystal - After Gate"
    BC_IN = "Blue Crystal - Inside"
    RH = "Rattlehag"
    AF_RH = "After Rattlehag"
    BF_PC = "Before Purple Crystal"
    PC = "Purple Crystal"
    CT = "Carrot Town"
    BV = "Blueville"
    BH_BV = "Behind Blueville"
    BFB1 = "Before Boss 1"
    BFB2 = "Before Boss 2"
    BFB3 = "Before Boss 3"
    BA = "Boss Arena"
    CA = "Cactus"

@dataclass(frozen=True)
class RegionData:
    exits: tuple[RegionName, ...] = ()
    pipes: tuple[RegionName, ...] = None

supraland_regions: dict[RegionName, RegionData] = {
    RegionName.Intro: RegionData(exits=(RegionName.RV,)),
    RegionName.RV: RegionData(
        exits=(
            RegionName.Intro,
            RegionName.D1,
            #RegionName.SF,
        )
    ),
    RegionName.D1: RegionData(
        exits=(
            RegionName.RV,
            RegionName.D2,
            RegionName.RC,
        )
    ),
    RegionName.D2: RegionData(
        exits=(
            RegionName.D1,
            RegionName.D3,
            RegionName.RC,
            #RegionName.AF1,
        ),
        pipes=(
            #RegionName.RC,
            RegionName.AF3,
        )
    ),
    RegionName.D3: RegionData(
        exits=(
            RegionName.D2,
            RegionName.BV,
            RegionName.RC,
            RegionName.FR,
            RegionName.RH,
            #RegionName.BFB1,
            RegionName.GC,
        )
    ),
    RegionName.RC: RegionData(
        exits=(
            RegionName.D1,
            RegionName.D2,
            RegionName.D3,
            RegionName.LV,
        ),
        pipes=(
            #RegionName.D2,
        )
    ),
    RegionName.LV: RegionData(
        exits=(
            RegionName.RC,
            RegionName.GC,
            RegionName.D3
        )
    ),
    RegionName.GC: RegionData(
        exits=(
            RegionName.LV,
            RegionName.BH_GC,
            RegionName.D3,
        )
    ),
    RegionName.BH_GC: RegionData(
        exits=(
            RegionName.GC,
            RegionName.BFB1,
        )
    ),
    RegionName.FR: RegionData(
        exits=(
            RegionName.D3,
            #RegionName.BC,
        ),
        pipes=(
            RegionName.BC,
            #RegionName.AF_RH
        )
    ),
    RegionName.BC: RegionData(
        exits=(
            #RegionName.FR,
            RegionName.AF1,
        ),
        pipes=(
            RegionName.FR,
        )
    ),
    RegionName.AF1: RegionData(
        exits=(
            #RegionName.BC,
            RegionName.CT,
            RegionName.D2,
            RegionName.AF2,
            RegionName.AF4,
            #RegionName.SF,
        )
    ),
    RegionName.AF2: RegionData(
        exits=(
            RegionName.AF1,
            RegionName.AF3,
            RegionName.AF4,
            RegionName.SF,
        )
    ),
    RegionName.AF3: RegionData(
        exits=(
            RegionName.AF2,
        ),
        pipes=(
            RegionName.D2,
        )
    ),
    RegionName.AF4: RegionData(
        exits=(
            RegionName.AF1,
            RegionName.AF2,
            #RegionName.BSF,
        )
    ),
    RegionName.SF: RegionData(
        exits=(
            RegionName.AF1,
            RegionName.AF2,
            RegionName.RV,
            RegionName.BSF
        )
    ),
    RegionName.BSF: RegionData(
        exits=(
            RegionName.AF4,
            RegionName.SF,
            RegionName.BC_BG,
        )
    ),
    RegionName.BC_BG: RegionData(
        exits=(
            #RegionName.BSF,
            RegionName.BC_AG,
        )
    ),
    RegionName.BC_AG: RegionData(
        exits=(
            RegionName.BC_BG,
            RegionName.BC_IN,
        )
    ),
    RegionName.BC_IN: RegionData(
        exits=(
            RegionName.BC_BG,
        )
    ),
    RegionName.RH: RegionData(
        exits=(
            RegionName.D3,
            RegionName.AF_RH,
            RegionName.BV,
        ),
        pipes=(
            RegionName.BH_BV,
        )
    ),
    RegionName.AF_RH: RegionData(
        exits=(
            RegionName.RH,
            RegionName.BF_PC,
        ),
        pipes=(
            RegionName.FR,
            RegionName.CA,
        )
    ),
    RegionName.BF_PC: RegionData(
        exits=(
            #RegionName.AF_RH,
            RegionName.PC,
            RegionName.CT,
        ),
        pipes=(
            RegionName.AF_RH,
            #RegionName.PC,
            RegionName.CA,
        )
    ),
    RegionName.PC: RegionData(
        exits=(
            RegionName.CT,
        )
    ),
    RegionName.CT: RegionData(
        exits=(
            #RegionName.AF1,
            #RegionName.PC,
            RegionName.BF_PC,
        ),
        pipes=(
            #RegionName.CT,
        )
    ),
    RegionName.BV: RegionData(
        exits=(
            RegionName.D3,
            RegionName.RH,
            RegionName.BH_BV,
            #RegionName.BFB1,
        )
    ),
    RegionName.BH_BV: RegionData(
        exits=(
            RegionName.BV,
        ),
        pipes=(
            RegionName.RH,
        )
    ),
    RegionName.BFB1: RegionData(
        exits=(
            RegionName.BH_GC,
            RegionName.BV,
            RegionName.D3,
            RegionName.BFB2,
        ),
        pipes=(
            RegionName.BA,
        )
    ),
    RegionName.BFB2: RegionData(
        exits=(
            #RegionName.BFB1,
            RegionName.BFB3,
        )
    ),
    RegionName.BFB3: RegionData(
        exits=(
            #RegionName.BFB2,
            RegionName.BA,
        )
    ),
    RegionName.BA: RegionData(
        exits=(
            #RegionName.BFB3,
            RegionName.LV,
            RegionName.GC,
        ),
        pipes=(
            RegionName.BFB1,
        )
    ),
    RegionName.CA: RegionData(
        exits=(),
        pipes=(
            #RegionName.AF_RH,
        )
    )
}

# print("Normal Connections")
# for k, v in supraland_regions.items():
#     for e in v.exits:
#         print(f"({k}, {e}): True,")
# print("Pipes")
# for k, v in supraland_regions.items():
#
#     if v.pipes is not None:
#         for p in v.pipes:
#             print(f"({k}, {p}): True,")


