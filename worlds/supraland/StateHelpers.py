import dataclasses
from enum import Enum
from typing import TYPE_CHECKING, Iterable, Any
from typing_extensions import override
from BaseClasses import CollectionState
from NetUtils import JSONMessagePart
from .constants import GAME_NAME
from rule_builder import Has, HasAny, Rule, TWorld, OptionFilter, HasAll, HasAllCounts
from .items import FillerItem, ProgressionItem, TrapItem, UsefulItem


if TYPE_CHECKING:
    from world import SupralandWorld

HeightTable = {
    ProgressionItem.ProgTrans: [3, 5], #base, shot force
    ProgressionItem.ProgSpeedJump: [1, 1, 2, 3], #speed inc 1.5x, 2x, double jump, triple jump
    ProgressionItem.ProgCube: [2, 2, 2],
#    ProgressionItem.Happiness: [100]
}
wallet_sizes = [30, 45, 67, 101, 151, 227, 455, 911, 1822, 3645, 7290]


def as_str(value: Enum | str) -> str:
    return str(value.value) if isinstance(value, Enum) else value


@dataclasses.dataclass()
class CanReachHeight(Rule["SupralandWorld"], game=GAME_NAME):

    TargetHeight: int = 1

    def __init__(self, TargetHeight: int, options: Iterable[OptionFilter[Any]] = ()) -> None:
        super().__init__(options=options)
        self.TargetHeight = TargetHeight

    @override
    def _instantiate(self, world: TWorld) -> Rule.Resolved:
        if self.TargetHeight == 0:
            return world.true_rule
        return self.Resolved(self.TargetHeight, player=world.player, caching_enabled=world.rule_caching_enabled)


    class Resolved(Rule.Resolved):
        target_height: int

        def _evaluate(self, state: CollectionState) -> bool:
            return sum([HeightTable[item][min(state.count(item, self.player)-1, len(HeightTable[item]))] for item in
                        HeightTable.keys()]) >= self.target_height

        @override
        def explain_json(self, state: CollectionState | None = None) -> list[JSONMessagePart]:
            if state is None:
                verb = "Can afford"
            elif self(state):
                verb = "Afforded"
            else:
                verb = "Cannot afford"
            return [
                {"type": "text", "text": f"{verb} height"},
                {"type": "color", "color": "yellow", "text": str(self.target_height)},
            ]

        @override
        def explain_str(self, state: CollectionState | None = None) -> str:
            if state is None:
                return str(self)
            prefix = "Reached" if self(state) else "Cannot reach"
            return f"{prefix} height {self.target_height}"

        @override
        def __str__(self) -> str:
            return f"Can reach height {self.target_height}"


@dataclasses.dataclass()
class CanAfford(Rule["SupralandWorld"], game=GAME_NAME):

    cost: int = 1

    def __init__(self, cost: int, options: Iterable[OptionFilter[Any]] = ()) -> None:
        super().__init__(options=options)
        self.cost = cost

    @override
    def _instantiate(self, world: TWorld) -> Rule.Resolved:
        if self.cost <= 30:
            return world.true_rule
        return self.Resolved(self.cost, player=world.player, caching_enabled=world.rule_caching_enabled)


    class Resolved(Rule.Resolved):
        cost: int

        @override
        def _evaluate(self, state: CollectionState) -> bool:
            return wallet_sizes[state.count(ProgressionItem.Wallet2+ProgressionItem.Wallet15, self.player)] > self.cost

        @override
        def explain_json(self, state: CollectionState | None = None) -> list[JSONMessagePart]:
            if state is None:
                verb = "Can afford"
            elif self(state):
                verb = "Afforded"
            else:
                verb = "Cannot afford"
            return [
                {"type": "text", "text": f"{verb}"},
                {"type": "color", "color": "yellow", "text": str(self.cost)},
                {"type": "text", "text": f"coins"}
            ]

        @override
        def explain_str(self, state: CollectionState | None = None) -> str:
            if state is None:
                return str(self)
            prefix = "Afforded" if self(state) else "Cannot afford"
            return f"{prefix} {self.cost} coins"

        @override
        def __str__(self) -> str:
            return f"Can afford {self.cost} coins"

@dataclasses.dataclass()
class CanDefeatCombat(Rule["SupralandWorld"], game=GAME_NAME):
    # currently just counts all health once, and all combat twice
    # 21x Health (2x 2, 16x 5, 3x 15)
    # 21x Regen (1x base, 3x speed, 16x 5, 1x 10)
    # 22x SwordDamage (9x 1, 6x 2, 7x 3)
    # 14x GunDamage (4x 1, 9x 5, 1x 15)
    # 8x ComboDamage (8x 25)
    # 10x SwordCritical
    # max is 150
    combat : int = 1

    def __init__(self, combat: int, options: Iterable[OptionFilter[Any]] = ()) -> None:
        super().__init__(options=options)
        self.combat = combat

    @override
    def _instantiate(self, world: TWorld) -> Rule.Resolved:
        if self.combat == 0:
            return world.true_rule
        return self.Resolved(self.combat, player=world.player, caching_enabled=world.rule_caching_enabled)


    class Resolved(Rule.Resolved):
        combat: int

        @override
        def _evaluate(self, state: CollectionState) -> bool:
            return ((state.count(UsefulItem.Health15, self.player)+state.count(UsefulItem.Health5, self.player)+state.count(UsefulItem.Health2, self.player)+state.count(UsefulItem.Health1, self.player))+
                    state.count(UsefulItem.ProgHealthRegen, self.player) +
                    (state.count(UsefulItem.GunDamage15, self.player)+state.count(UsefulItem.GunDamage5, self.player)+state.count(UsefulItem.GunDamage1, self.player)) * 2 +
                    (state.count(UsefulItem.SwordDamage1, self.player)+state.count(UsefulItem.SwordDamage2, self.player)+state.count(UsefulItem.SwordDamage3, self.player)) * 2 +
                    state.count(UsefulItem.GunComboDamage, self.player) * 2 +
                    state.count(UsefulItem.SwordCritical, self.player) +
                    (state.count(ProgressionItem.ProgSword, self.player)-1)*10) >= self.combat

        @override
        def explain_json(self, state: CollectionState | None = None) -> list[JSONMessagePart]:
            if state is None:
                verb = "Can Defeat"
            elif self(state):
                verb = "Defeated"
            else:
                verb = "Cannot defeat"
            return [
                {"type": "text", "text": f"{verb} level"},
                {"type": "color", "color": "yellow", "text": str(self.combat)},
            ]

        @override
        def explain_str(self, state: CollectionState | None = None) -> str:
            if state is None:
                return str(self)
            prefix = "Defeated" if self(state) else "Cannot defeat"
            return f"{prefix} level {self.combat}"

        @override
        def __str__(self) -> str:
            return f"Can defeat level {self.combat}"

@dataclasses.dataclass()
class HasLocationGroup(Rule["SupralandWorld"], game=GAME_NAME):

    location_name_group: str
    """The name of the item group containing the items"""

    count: int = 1
    """The number of items the player needs to have"""

    def __init__(self, location_name_group: str, count: int, options: Iterable[OptionFilter[Any]] = ()) -> None:
        super().__init__(options=options)
        self.location_name_group = location_name_group
        self.count = count

    @override
    def _instantiate(self, world: TWorld) -> Rule.Resolved:
        location_names = tuple(sorted(world.location_name_groups[self.location_name_group]))
        return self.Resolved(
            self.location_name_group,
            location_names,
            self.count,
            player=world.player,
            caching_enabled=world.rule_caching_enabled,
        )

    class Resolved(Rule.Resolved):
        location_name_group: str
        location_names: tuple[str, ...]
        count: int = 1

        @override
        def _evaluate(self, state: CollectionState) -> bool:
            # implementation based on state.has_group
            found = 0

            for location_name in self.location_names:
                found += state.can_reach_location(location_name, self.player)
                if found >= self.count:
                    return True
            return False

        @override
        def explain_json(self, state: CollectionState | None = None) -> list[JSONMessagePart]:
            if state is None:
                verb = "Can reach"
            elif self(state):
                verb = "Reached"
            else:
                verb = "Cannot reach"
            return [
                {"type": "text", "text": f"{verb}"},
                {"type": "color", "color": "yellow", "text": str(self.count)},
                {"type": "color", "color": "cyan", "text": self.location_name_group},
                {"type": "text", "text": f" locations"}
            ]

        @override
        def explain_str(self, state: CollectionState | None = None) -> str:
            if state is None:
                return str(self)
            prefix = "Reached" if self(state) else "Cannot reach"
            return f"{prefix} {self.count} {self.location_name_group} locations"

        @override
        def __str__(self) -> str:
            return f"Can reach {self.count} {self.location_name_group} locations"

can_destroy_red_planks = HasAny(ProgressionItem.ProgSword, ProgressionItem.ProgGun, ProgressionItem.ProgTrans)

can_defeat_meatbag = HasAllCounts({ProgressionItem.Buckle : 1, ProgressionItem.ProgForceBeam: 3}) & can_destroy_red_planks
can_melt_metal = HasAllCounts({ProgressionItem.GunAltDamage: 5, ProgressionItem.ProgGun: 2})
can_destroy_wood_grave = HasAny(UsefulItem.ProgGraveGun, UsefulItem.ProgGraveSword)
can_destroy_stone_grave = (HasAllCounts({UsefulItem.ProgGraveSword: 2,ProgressionItem.ProgSword: 1})) | (HasAllCounts({UsefulItem.ProgGraveGun: 2,ProgressionItem.ProgGun: 1}))
can_break_stone = HasAll(ProgressionItem.Strong, ProgressionItem.ProgSword)
reach_upper_red_crystal = CanReachHeight(4) & Has(ProgressionItem.ProgCube)
reach_post_lockerroom = can_destroy_red_planks & Has(ProgressionItem.ProgGun)
can_beam_cube = HasAllCounts({ProgressionItem.ProgCube: 1, ProgressionItem.ProgForceBeam: 3})

can_defeat_rattlehag = CanDefeatCombat(20)
can_defeat_gauntlet = CanDefeatCombat(100)

