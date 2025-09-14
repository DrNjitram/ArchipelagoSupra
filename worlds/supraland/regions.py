from dataclasses import dataclass
from enum import Enum

from worlds.hk.Extractor import region_name


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
            RegionName.SF,)
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
            RegionName.AF1,
        )
    ),
    RegionName.D3: RegionData(
        exits=(
            RegionName.D2,
            RegionName.BV,
            RegionName.RC,
            RegionName.FR,
            RegionName.RH,
            RegionName.BFB1,
            RegionName.GC,
        )
    ),
    RegionName.RC: RegionData(
        exits=(
            RegionName.D1,
            RegionName.D2,
            RegionName.D3,
            RegionName.LV,
        )
    ),
    RegionName.LV: RegionData(
        exits=(
            RegionName.RC,
            RegionName.GC,
        )
    ),
    RegionName.GC: RegionData(
        exits=(

        )
    ),
    RegionName.BH_GC: RegionData(
        exits=(

        )
    ),
    RegionName.FR: RegionData(
        exits=(

        )
    ),
    RegionName.BC: RegionData(
        exits=(

        )
    ),
    RegionName.AF1: RegionData(
        exits=(

        )
    ),
    RegionName.AF2: RegionData(
        exits=(

        )
    ),
    RegionName.AF3: RegionData(
        exits=(

        )
    ),
    RegionName.AF4: RegionData(
        exits=(

        )
    ),
    RegionName.SF: RegionData(
        exits=(

        )
    ),
    RegionName.BSF: RegionData(
        exits=(

        )
    ),
    RegionName.BC_BG: RegionData(
        exits=(

        )
    ),
    RegionName.BC_AG: RegionData(
        exits=(

        )
    ),
    RegionName.BC_IN: RegionData(
        exits=(

        )
    ),
    RegionName.RH: RegionData(
        exits=(

        )
    ),
    RegionName.AF_RH: RegionData(
        exits=(

        )
    ),
    RegionName.BF_PC: RegionData(
        exits=(

        )
    ),
    RegionName.PC: RegionData(
        exits=(

        )
    ),
    RegionName.CT: RegionData(
        exits=(

        )
    ),
    RegionName.BV: RegionData(
        exits=(

        )
    ),
    RegionName.BH_BV: RegionData(
        exits=(

        )
    ),
    RegionName.BFB1: RegionData(
        exits=(

        )
    ),
    RegionName.BFB2: RegionData(
        exits=(

        )
    ),
    RegionName.BFB3: RegionData(
        exits=(

        )
    ),
    RegionName.BA: RegionData(
        exits=(

        )
    ),
}

