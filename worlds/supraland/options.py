from dataclasses import dataclass

from Options import Toggle, DeathLink, PerGameCommonOptions


class CoinSanity(Toggle):
    """
    Include all coins in the world as items.
    Adds ~700 items to the pool and makes buying items difficult.
    """

class GraveSanity(Toggle):
    """
    Include destroying graves in the world as items.
    Adds junk items to the world.
    """

class Enemytrap(Toggle):
    """
    Add enemy traps to the item pool
    """

class SupralandDeathLink(DeathLink):
    __doc__ = DeathLink.__doc__


@dataclass
class SupralandOptions(PerGameCommonOptions):
    coinsanity: CoinSanity
    gravesanity: GraveSanity
    enemy_trap: Enemytrap
    deathlink: DeathLink

