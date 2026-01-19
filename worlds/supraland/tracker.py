# pyright: reportUninitializedInstanceVariable=false

from functools import cached_property
from typing import Any, ClassVar, TYPE_CHECKING

from typing_extensions import override

from BaseClasses import CollectionState, Entrance, Location, Region
from NetUtils import JSONMessagePart
from Options import Option
from .rule_builder.rules import Rule
from Utils import get_intended_text  # pyright: ignore[reportUnknownVariableType]
from worlds.generic.Rules import CollectionRule


if TYPE_CHECKING:
    from worlds.AutoWorld import World
else:
    World = object


# from.bases import SupralandWorldBase


def rule_to_json(rule: CollectionRule | None, state: CollectionState) -> list[JSONMessagePart]:
    if isinstance(rule, Rule.Resolved):
        return [
            {"type": "text", "text": "    "},
            *rule.explain_json(state),
        ]
    return [
        {"type": "text", "text": "    "},
        {"type": "color", "color": "green", "text": "True"},
    ]


class SupralandUTWorld(World):
    ut_can_gen_without_yaml: ClassVar[bool] = True


    # if TYPE_CHECKING:
    #     starting_characters: list[Character]
    #     extra_gold_eyes: int

    @cached_property
    def is_ut(self) -> bool:
        return getattr(self.multiworld, "generation_is_fake", False)

    @override
    def generate_early(self) -> None:
        re_gen_passthrough = getattr(self.multiworld, "re_gen_passthrough", {})
        if re_gen_passthrough and self.game in re_gen_passthrough:
            slot_data: dict[str, Any] = re_gen_passthrough[self.game]

            slot_options: dict[str, Any] = slot_data.get("options", {})
            for key, value in slot_options.items():
                opt: Option[Any] | None = getattr(self.options, key, None)
                if opt is not None:
                    setattr(self.options, key, opt.from_any(value))


    def get_logical_path(self, dest_name: str, state: CollectionState) -> list[JSONMessagePart]:
        if not dest_name:
            return [{"type": "text", "text": "Provide a location or region to route to using /route [name]"}]

        goal_location: Location | None = None
        goal_region: Region | None = None
        region_name = ""
        location_name, usable, response = get_intended_text(dest_name, [loc.name for loc in self.get_locations()])
        if usable:
            try:
                goal_location = self.get_location(location_name)
            except KeyError:
                return [{"type": "text", "text": f"Location {location_name} not found in this multiworld"}]
            goal_region = goal_location.parent_region
            if not goal_region:
                return [{"type": "text", "text": f"Location {location_name} has no parent region"}]
        else:
            region_name, usable, _ = get_intended_text(
                dest_name,
                [reg.name for reg in self.get_regions()],
            )
            if usable:
                goal_region = self.get_region(region_name)
            else:
                return [{"type": "text", "text": response}]

        if goal_location and not goal_location.can_reach(state):
            return [{"type": "text", "text": f"Location {goal_location.name} cannot be reached"}]
        if goal_region and goal_region not in state.path:
            return [{"type": "text", "text": f"Region {goal_region.name} cannot be reached"}]

        path: list[Entrance] = []
        name, connection = state.path[goal_region]
        while connection != ("Menu", None) and connection is not None:
            name, connection = connection
            if "->" in name and "Menu" not in name:
                path.append(self.get_entrance(name))

        messages: list[JSONMessagePart] = []
        path.reverse()
        for p in path:
            messages.extend(
                [
                    {"type": "entrance_name", "text": p.name, "player": self.player},
                    {"type": "text", "text": "\n"},
                    *rule_to_json(p.access_rule, state),
                    {"type": "text", "text": "\n"},
                ]
            )

        if goal_location:
            messages.extend(
                [
                    {"type": "text", "text": "-> "},
                    {
                        "type": "location_name",
                        "text": goal_location.name,
                        "player": self.player,
                    },
                    {"type": "text", "text": "\n"},
                    *rule_to_json(goal_location.access_rule, state),
                ]
            )

        return messages