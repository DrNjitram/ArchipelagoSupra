from typing import TYPE_CHECKING, Dict
from .locations import location_table
from ..generic.Rules import set_rule

if TYPE_CHECKING:
    from . import SupralandWorld
    from BaseClasses import CollectionState, Location

starting_wallet = 30

def can_access_location(state: "CollectionState", player: int, loc: Dict) -> bool:
    return True

def set_location_rule(world: "SupralandWorld", player: int, loc: str):
    set_rule(world.get_location(loc), lambda state: can_access_location(state, player, loc))

def set_rules(supraland_world: "SupralandWorld"):
    player = supraland_world.player
    gravesanity = supraland_world.options.gravesanity.value
    coinsanity = supraland_world.options.coinsanity.value
    coinsanity_types = ["Coin_C", "CoinBig_C", "Coin:Chest_C"]
    gravesanity_types = ["EnemySpawn1_C", "EnemySpawn2_C", "EnemySpawn3_C"]
    for location_name, location_data in location_table.items():
        if (not gravesanity and location_data["item"] in gravesanity_types) or (
                not coinsanity and location_data["item"] in coinsanity_types):
            continue
        set_location_rule(supraland_world, player, location_name)

    supraland_world.multiworld.completion_condition[player] = lambda state: state.has("Victory", player)