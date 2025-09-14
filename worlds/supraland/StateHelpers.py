from BaseClasses import CollectionState

HeightTable = {
    "Prog:Translocator": [3, 5], #base, shot force
    "Prog:SpeedJump": [1, 2, 3], #speed inc, double jump, triple jump
    "Prog:Cube": [2, 2, 2],
    "Happiness": [100]
}
wallet_sizes = [30, 45, 67, 101, 151, 227, 455, 911, 1822, 3645, 7290]

def has_sword(state: CollectionState, player: int, level=1) -> bool:
    return state.count("Prog:Sword", player) >= level

def has_gun(state: CollectionState, player: int, level=1) -> bool:
    return state.count("Prog:Sword", player) >= level

def can_destroy_graves1(state: CollectionState, player: int) -> bool:
    return ((has_sword(state, player) and state.has("Prog:GraveSword", player))
            or (has_gun(state, player) and state.has("Prog:GraveGun", player)))

def can_destroy_graves2(state: CollectionState, player: int) -> bool:
    return ((has_sword(state, player) and state.count("Prog:GraveSword", player) >= 2)
            or (has_gun(state, player) and state.count("Prog:GraveGun", player)) >= 2)

def can_destroy_graves3(state: CollectionState, player: int) -> bool:
    return state.count("Prog:Cube", player) >= 3 and state.has("StompShoes", player)

def can_reach_height(state: CollectionState, player: int, height: int) -> bool:
    # Has some awkward handling of more items than we expect
    return sum([HeightTable[item][min(state.count(item, player), len(HeightTable[item]))] for item in HeightTable.keys()]) >= height

def can_afford(state: CollectionState, player: int, cost: int) -> bool:
    return wallet_sizes[state.count("PRog:WalletIncrease", player)] > cost

def can_destroy_metal(state: CollectionState, player: int) -> bool:
    return state.count("BuyGunAltDamagex2_C", player) >= 5

def can_break_planks(state: CollectionState, player: int) -> bool:
    return (state.has("Prog:Sword", player)
            or state.has("Prog:Translocator", player)
            or state.has("Prog:Gun", player))


def can_defeat_meatbag(state: CollectionState, player: int) -> bool:
    return (state.has("FloatBuckle", player)
            and can_break_planks(state, player)
            and state.count("Prog:ForceBeam", player) >= 3)

def combat_level(state: CollectionState, player: int, level: int) -> bool:
    # currently just counts all health once, and all combat twice
    # 21x Health (2x 2, 16x 5, 3x 15)
    # 21x Regen (1x base, 3x speed, 16x 5, 1x 10)
    # 22x SwordDamage (9x 1, 6x 2, 7x 3)
    # 14x GunDamage (4x 1, 9x 5, 1x 15)
    # 8x ComboDamage (8x 25)
    # 10x SwordCritical
    # max is 150
    return (state.count("Prog:Health", player) + state.count("Prog:Regen", player) +
            state.count("GunDamage", player) * 2 + state.count("SwordDamage", player) * 2 +
            state.count("ComboDamage", player) * 2 + state.count("SwordCritical", player) +
            (state.count("Prog:Sword")-1)*10) >= level

def can_defeat_rattlehag(state: CollectionState, player: int) -> bool:
    # 20 is arbitrary for now, but allows for difficulty levels
    return combat_level(state, player, 20)

def can_defeat_gauntlet(state: CollectionState, player: int) -> bool:
    # 20 is arbitrary for now, but allows for difficulty levels
    return combat_level(state, player, 100)