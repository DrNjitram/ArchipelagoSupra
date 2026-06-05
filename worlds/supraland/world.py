import logging

from typing import Any, Dict, List, ClassVar
from typing_extensions import override
from BaseClasses import Tutorial, Region, ItemClassification, Item, LocationProgressType

from .constants import GAME_NAME
from .items import (
    Events,
    item_name_to_id,
    item_table,
    SupralandItem, FillerItem, ProgressionItem, TheftItem
)
from .locations import (
    SupralandLocation,
    LocationGroup,
    LocationName,
    location_name_groups,
    location_name_to_id,
    location_table,
)
from .entrances import ENTRANCE_RULES, PIPE_RULES
from .main_campaign import COMPLETION_RULE,  MAIN_LOCATION_RULES
from worlds.generic.Rules import set_rule
from .StateHelpers import CanAfford
from . import options
from .options import SupralandOptions
from .regions import supraland_regions
from .tracker import SupralandUTWorld
from worlds.AutoWorld import WebWorld, World

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


def create_entrance(region, exit_region, rule):
    region.connect(exit_region, rule=rule)


class SupralandWorld(SupralandUTWorld, World):
    """
     A mix between Portal, Zelda and Metroid. Exploration, puzzles, terrible combat, secret upgrades and new abilities that help you reach new places.
    """

    game = GAME_NAME
    web = SupralandWeb()

    options_dataclass = SupralandOptions
    options: SupralandOptions  # pyright: ignore[reportIncompatibleVariableOverride]

    #item_name_groups: ClassVar[dict[str, set[str]]] = item_name_groups
    location_name_groups: ClassVar[dict[str, set[str]]] = location_name_groups
    item_name_to_id: ClassVar[dict[str, int]] = item_name_to_id
    location_name_to_id = location_name_to_id

    explicit_indirect_conditions = False
    rule_caching_enabled: ClassVar[bool] = False

    required_client_version = (0, 6, 7)


    origin_region_name = "Introduction"

    coinsanity_types = [FillerItem.Coin, FillerItem.BigCoin]
    gravesanity_types = [FillerItem.EnemySpawn1, FillerItem.EnemySpawn2, FillerItem.EnemySpawn3]

    @override
    def create_location(self, name: str) -> SupralandLocation:
        location_name = LocationName(name)
        data = location_table[name]
        region = self.get_region(data.region.value)
        location = SupralandLocation(self.player, name, location_name_to_id.get(name), region)
        rule = MAIN_LOCATION_RULES.get(location_name)

        if rule is not None:
            if data.cost:
                rule = (rule & CanAfford(data.cost)).resolve(self)
                set_rule(location, rule)
            else:
                rule = rule.resolve(self)
                set_rule(location, rule)

            #self.register_rule_dependencies(rule)
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
                if rule is None:
                    raise Exception(f"No matching rules for {region_name.value} -> {exit_region_name.value}")
                else:
                    rule = rule.resolve(self)
                    create_entrance(region, exit_region, rule)


            if region_data.pipes is not None:
                for pipe_region_name in region_data.pipes:
                    pipe_region = self.get_region(pipe_region_name.value)
                    region_pair = (region_name, pipe_region_name)
                    rule = PIPE_RULES.get(region_pair)

                    if rule is None:
                        raise Exception(f"No matching rules for {region_name.value} -> {pipe_region_name.value}")
                    else:
                        rule = rule.resolve(self)
                        create_entrance(region, pipe_region, rule)


        for group, location_names in location_name_groups.items():
            if group == LocationGroup.E:
                continue
            if (not self.options.gravesanity.value and group in [LocationGroup.C, LocationGroup.BC]) or (
                    not self.options.coinsanity.value and group == LocationGroup.G):
                continue
            for location_name in sorted(location_names):
                # if location_name == LocationName.UpgradeHappiness2_2 and self.options.shufflehappiness:
                #     continue

                self.create_location(location_name)

        self.get_location(LocationName.Chest157).progress_type = LocationProgressType.EXCLUDED


        self.create_event(Events.RH, LocationName.RH)
        self.create_event(Events.MB, LocationName.MB)


        rule = COMPLETION_RULE.resolve(self)
        self.multiworld.completion_condition[self.player] = rule
        #self.register_rule_dependencies(rule)

    def pre_fill(self) -> None:
        pass

    def fill_slot_data(self) -> Dict[str, Any]:
        return {
            "coinsanity": self.options.coinsanity.value,
            "gravesanity": self.options.gravesanity.value,
            "enemy_trap": self.options.enemy_trap.value,
            "deathlink": self.options.deathlink.value,
            "bluetheft": self.options.theftskip.value
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
        filler_pool: List[Item] = []

        for data in item_table.values():
            if (not self.options.gravesanity.value and data.name in self.gravesanity_types) or (not self.options.coinsanity.value and data.name in self.coinsanity_types):
                continue
            if self.options.theftskip and data.name in TheftItem:
                continue
            for _ in range(data.count):
                pool.append(self.create_item(str(data.name.value)))

        self.multiworld.itempool += pool

        if not self.options.shufflehappiness:
            item = self.create_item(ProgressionItem.Happiness)
            self.multiworld.push_item(self.get_location(LocationName.UpgradeHappiness2_2), item,False)
            self.multiworld.itempool.remove(item)
            pool.remove(item)

        if not self.options.deadheroes:
            for loc, item in [(LocationName.DeadHero2Austin, FillerItem.HeroAustin),
                              (LocationName.DeadHero2Link, FillerItem.HeroLink),
                              (LocationName.DeadHero3Heman, FillerItem.HeroHeman),
                              (LocationName.DeadHero3Pokemon, FillerItem.HeroAsh),
                              (LocationName.DeadHero4Picard, FillerItem.HeroPicard),
                              (LocationName.DeadHero4Santa, FillerItem.HeroSanta),
                              (LocationName.DeadHero4Santa2, FillerItem.HeroVault),
                              (LocationName.DeadHero4Santa3, FillerItem.HeroStar),
                              (LocationName.DeadHero_3, FillerItem.HeroMagic),
                              (LocationName.DeadHeroGoku, FillerItem.HeroGoku),
                              (LocationName.DeadHeroGuybrush, FillerItem.HeroGuy),
                              (LocationName.DeadHeroIndy, FillerItem.HeroIndy)]:
                item = self.create_item(item.value)
                self.multiworld.push_item(self.get_location(loc), item, False)
                self.multiworld.itempool.remove(item)
                pool.remove(item)


        if not self.options.theftskip:
            for loc, item in [(LocationName.BuyBelt2_2, TheftItem.StolenBuckle),
                              (LocationName.BuyDoubleJump2, TheftItem.StolenJump2),
                              (LocationName.BuyTripleJump2, TheftItem.StolenJump3),
                              (LocationName.BuyForceBlock3, TheftItem.StolenCube),
                              (LocationName.BuyGun2_2, TheftItem.StolenGun),
                              (LocationName.Chest114, TheftItem.StolenCoins)]:
                item = self.create_item(item.value)
                self.multiworld.push_item(self.get_location(loc), item, False)
                self.multiworld.itempool.remove(item)
                pool.remove(item)

        if self.options.earlyplank.value:
            choice = str(self.multiworld.random.choice([ProgressionItem.ProgSword, ProgressionItem.ProgTrans, ProgressionItem.ProgGun]).value)
            item = self.create_item(choice)
            self.multiworld.push_item(self.get_location(LocationName.BuySword_695), item, False)
            self.multiworld.itempool.remove(item)
            pool.remove(item)
        if self.options.earlyspeed:
            item = self.create_item(ProgressionItem.ProgSpeedJump.value)
            pool.remove(item)
            if self.options.earlyspeed == 1: # Sphere 1
                state = self.multiworld.state.copy()
                state.add_item(ProgressionItem.ProgSword, 1, 1)
                loc = self.multiworld.random.choice(self.multiworld.get_reachable_locations(state, 1))
                self.multiworld.push_item(loc, item, False)
                self.multiworld.itempool.remove(item)
            else: # self.option.earlyspeed == 2: # Start With
                self.push_precollected(item)



        total_locations = len(self.multiworld.get_unfilled_locations(self.player))

        while len(pool) + len(filler_pool) < total_locations:
            filler_pool.append(self.create_filler())

        self.multiworld.itempool += filler_pool

    @override
    def set_rules(self) -> None:
        pass
        #self.register_dependencies()


    @override
    def get_filler_item_name(self) -> str:
        return FillerItem.Coin.value

    # def get_trap_item_name(self) -> str:
    #     return self.random.choice(trap_items)


