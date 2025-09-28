from functools import cached_property
from typing import Any, Dict, List, ClassVar, override

from .StateHelpers import CanAfford
from .items import (
    Events,
    ItemGroup,
    item_name_to_id,
    item_table,
    SupralandItem, FillerItem
)
from . import options
from .locations import (
    SupralandLocation,
    LocationGroup,
    LocationName,
    location_name_groups,
    location_name_to_id,
    location_table,
)
from .regions import supraland_regions, RegionName
from BaseClasses import Tutorial, Region, ItemClassification, Item
from worlds.AutoWorld import WebWorld, World
from .constants import GAME_NAME
from rule_builder import RuleWorldMixin
from .main_campaign import COMPLETION_RULE,  MAIN_LOCATION_RULES
from .entrances import ENTRANCE_RULES
#from .tracker import UTMxin
import logging

logger = logging.getLogger(__name__)

class SupralandWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Subnautica randomizer connected to an Archipelago Multiworld",
        "English",
        "setup_en.md",
        "setup/en",
        ["Dr. Njitram", "Gummy"]
    )]

class SupralandWorld(RuleWorldMixin, World):
    """
     A mix between Portal, Zelda and Metroid. Exploration, puzzles, terrible combat, secret upgrades and new abilities that help you reach new places.
    """

    game: ClassVar[str] = GAME_NAME
    web: ClassVar[WebWorld] = SupralandWeb()

    #item_name_groups: ClassVar[dict[str, set[str]]] = item_name_groups
    location_name_groups: ClassVar[dict[str, set[str]]] = location_name_groups
    item_name_to_id: ClassVar[dict[str, int]] = item_name_to_id
    location_name_to_id = location_name_to_id
    rule_caching_enabled: ClassVar[bool] = True

    options_dataclass = options.SupralandOptions
    options: options.SupralandOptions
    required_client_version = (0, 6, 4)

    origin_region_name = "Introduction"

    coinsanity_types = ["Coin_C", "CoinBig_C", "Coin:Chest_C"]
    gravesanity_types = ["EnemySpawn1_C", "EnemySpawn2_C", "EnemySpawn3_C"]

    # @override
    # def generate_early(self) -> None:
    #     pass

    def create_location(self, name: str) -> SupralandLocation:
        location_name = LocationName(name)
        data = location_table[name]
        region = self.get_region(data.region.value)
        location = SupralandLocation(self.player, name, location_name_to_id.get(name), region)
        rule = MAIN_LOCATION_RULES.get(location_name)

        if rule is not None:
            if data.cost:
                self.set_rule(location, rule & CanAfford(data.cost))
            else:
                self.set_rule(location, rule)
        region.locations.append(location)
        return location

    @override
    def create_regions(self) -> None:
        for region_name in supraland_regions:
            region = Region(region_name.value, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        for region_name, region_data in supraland_regions.items():
            region = self.get_region(region_name.value)
            for exit_region_name in region_data.exits:
                exit_region = self.get_region(exit_region_name.value)
                region_pair = (region_name, exit_region_name)
                rule = ENTRANCE_RULES.get(region_pair)
                entrance = self.create_entrance(region, exit_region, rule)
                if not entrance:
                    logger.debug(f"No matching rules for {region_name.value} -> {exit_region_name.value}")

        # for group, location_names in location_name_groups.items():
        #     # if group not in logic_groups:
        #     #     continue
        #
        #     for location_name in sorted(location_names):
        #         # if location_name == LocationName.UpgradeHappiness2_2:
        #         #     continue
        for location_name in location_table:
            self.create_location(location_name)

        RH_item = SupralandItem(
            Events.RH.value,
            ItemClassification.progression_skip_balancing,
            None,
            self.player,
        )
        RH_region = self.get_region(RegionName.BA)
        RH_location = SupralandLocation(self.player, Events.RH.value, None, RH_region)
        RH_location.place_locked_item(RH_item)

        victory_region = self.get_region(RegionName.BA)
        victory_location = SupralandLocation(self.player, Events.MB.value, None, victory_region)
        victory_item = SupralandItem(
            Events.MB.value,
            ItemClassification.progression_skip_balancing,
            None,
            self.player,
        )
        victory_location.place_locked_item(victory_item)
        victory_region.locations.append(victory_location)
        self.set_completion_rule(COMPLETION_RULE)



    def fill_slot_data(self) -> Dict[str, Any]:
        return {
            "coinsanity": self.options.coinsanity.value,
            "gravesanity": self.options.gravesanity.value,
            "enemy_trap": self.options.enemy_trap.value,
            "deathlink": self.options.deathlink.value
        }

    @override
    def create_item(self, name: str) -> SupralandItem:

        item_data = item_table[name]
        classification: ItemClassification = item_data.classification

        return SupralandItem(name, classification, self.item_name_to_id[name], self.player)

    def create_event(self, event: Events, location_name: LocationName) -> None:
        item = SupralandItem(event.value, ItemClassification.progression_skip_balancing, None, self.player)
        location = self.create_location(location_name.value)
        location.address = None
        location.place_locked_item(item)

    # def create_trap(self) -> SupralandItem:
    #     return self.create_item(self.get_trap_item_name())

    def create_items(self) -> None:

        pool: List[Item] = []

        for data in item_table.values():
            # if (not self.options.gravesanity.value and data.type_name in self.gravesanity_types) or (not self.options.coinsanity.value and data.type_name in self.coinsanity_types):
            #     continue
            for _ in range(data.count):
                pool.append(self.create_item(data.name))

        self.multiworld.itempool += pool

    @override
    def set_rules(self) -> None:
        self.register_dependencies()

    @cached_property
    def filler_item_names(self) -> tuple[str, ...]:
        return FillerItem.Coin, FillerItem.BigCoin

    @override
    def get_filler_item_name(self) -> str:
        return self.random.choice(self.filler_item_names)

    # def get_trap_item_name(self) -> str:
    #     return self.random.choice(trap_items)


