from dataclasses import dataclass

from Options import Toggle, DeathLink, PerGameCommonOptions, Choice, DefaultOnToggle, Visibility


class CoinSanity(Toggle):
    """
    Include all coins in the world as items.
    Adds ~700 items to the pool and makes buying items difficult.
    """
    display_name = "Coinsanity"
    visibility = Visibility.none

class GraveSanity(Toggle):
    """
    Include destroying graves in the world as items.
    Adds junk items to the world.
    """
    display_name = "Gravesanity"
    visibility = Visibility.none

class Enemytrap(Toggle):
    """
    Add enemy traps to the item pool
    """
    display_name = "Enemy Traps"
    visibility = Visibility.none

class ShuffleHappiness(Toggle):
    """
    Put the Happiness item into the item pool
    """
    display_name = "Shuffle Happiness"

class SkipBluevilleTheft(Toggle):
    """
    Does not remove your items at the Blueville theft
    """
    display_name = "Skip Blueville Theft"

class IncludeHeroes(Toggle):
    """"
    Include the dead heroes into the shuffle
    """
    display_name = "Include Heroes"

class EarlySpeed(Choice):
    """
    Either vanilla, Sphere 1, or Start with
    Vanilla: Shuffle as usual
    Sphere 1: ensure a speed increase in sphere 1
    Start: Start with a speed increase
    """
    display_name = "Early Speed"
    default = 1
    option_vanilla = 0
    option_sphere = 1
    option_start = 2

class EarlyPlankBreak(DefaultOnToggle):
    """
    Be guaranteed to get an item to break planks in this sphere 0
    """
    display_name = "Early Plank Break"

class SupralandDeathLink(DeathLink):
    __doc__ = DeathLink.__doc__
    visibility = Visibility.none


@dataclass
class SupralandOptions(PerGameCommonOptions):
    coinsanity: CoinSanity
    gravesanity: GraveSanity
    enemy_trap: Enemytrap
    deathlink: DeathLink
    shufflehappiness: ShuffleHappiness
    theftskip: SkipBluevilleTheft
    deadheroes: IncludeHeroes
    earlyspeed: EarlySpeed
    earlyplank: EarlyPlankBreak

