# from typing import ClassVar
#
# from BaseClasses import MultiWorld
# from .rule_builder.cached_world import CachedRuleBuilderWorld
#
# from .items import EarlyItems
# from .options import SupralandOptions
#
#
#
# class SupralandWorldBase(CachedRuleBuilderWorld):
#     options_dataclass = SupralandOptions
#
#     options: SupralandOptions  # pyright: ignore[reportIncompatibleVariableOverride]
#     early_items: EarlyItems
#
#
#     def __init__(self, multiworld: MultiWorld, player: int) -> None:
#         super().__init__(multiworld, player)
#         self.early_items = EarlyItems()