"""
Zendo moderator
"""
import random
from structure import Structure
from rule import Rule
from constants import (
    RED, BLUE, YELLOW, EXACTLY, AT_LEAST, PYRAMIDS, WEDGES, BLOCKS
)


class ZendoModerator:
    """
    Play the role of moderator in Zendo.
    """
    MAX_NUM_RANGE = 5

    def __init__(self, difficulty="easy") -> None:
        self._rule = self.gen_rule()
        self._base_structures = []
        num_base_structures = 2
        for _ in range(num_base_structures):
            self._base_structures.append(self.generate_random_structure_according_to_rule(rule=self._rule, difficulty=difficulty))


    def gen_rule(self):
        """
        Generates and returns a random rule
        """
        color_options = [RED, BLUE, YELLOW]
        number_type_options = [EXACTLY, AT_LEAST]
        number_options = list(range(ZendoModerator.MAX_NUM_RANGE))
        block_type_options = [PYRAMIDS, WEDGES, BLOCKS]
        color_block_combo_options = ["both", "only_color", "only_block"]

        rule_string = random.choice(number_type_options) + " " + str(random.choice(number_options)) + " "
        color_block_combo = random.choice(color_block_combo_options)
        if color_block_combo == "both":
            rule_string += random.choice(color_options) + " " + random.choice(block_type_options)
        if color_block_combo == "only_color":
            rule_string += random.choice(color_options)
        if color_block_combo == "only_block":
            rule_string += random.choice(block_type_options)

        return Rule(rule_string)

    @staticmethod
    def generate_random_structure_according_to_rule(
        rule: Rule = None,
        difficulty: str = "easy"
    ):
        """
        Create and return structures that abide by the rule
        """
        if not rule:
            return None

        rule_is_at_least = rule.is_at_least
        rule_color = rule.color
        rule_quantity = rule.quantity
        rule_shape = rule.shape

        # for AT_LEAST add up to 3 extra qty
        if rule_is_at_least:
            rule_quantity += random.choice(list(range(4)))

        # harder structures have more meaningless components
        extra_qty_for_difficulty = 0
        if difficulty == "medium": extra_qty_for_difficulty = 3
        elif difficulty == "hard": extra_qty_for_difficulty = 6

        # list where index 0-8 represents the folowing:
        # num_red_pyramids, num_red_wedges, num_red_blocks,
        # num_blue_pyramids, num_blue_wedges, num_blue_blocks,
        # num_yellow_pyramids, num_yellow_wedges, num_yellow_blocks
        structure_attribute_list = [0] * 9

        structure_attribute_to_index_dict = {
            RED+PYRAMIDS: [0],
            RED+WEDGES: [1],
            RED+BLOCKS: [2],
            BLUE+PYRAMIDS: [3],
            BLUE+WEDGES: [4],
            BLUE+BLOCKS: [5],
            YELLOW+PYRAMIDS: [6],
            YELLOW+WEDGES: [7],
            YELLOW+BLOCKS: [8],
            RED: [0, 1, 2],
            BLUE: [3, 4, 5],
            YELLOW: [6, 7, 8],
            PYRAMIDS: [0, 3, 6],
            WEDGES: [1, 4, 7],
            BLOCKS: [2, 5, 8]
        }

        target_indexes = []
        if rule_color and rule_shape: target_indexes = structure_attribute_to_index_dict[rule_color + rule_shape]
        elif rule_color: target_indexes = structure_attribute_to_index_dict[rule_color]
        elif rule_shape: target_indexes = structure_attribute_to_index_dict[rule_shape]

        for _ in range(rule_quantity):
            structure_attribute_list[random.choice(target_indexes)] += 1
        for _ in range(extra_qty_for_difficulty):
            structure_attribute_list[random.choice([i for i in range(0, 9) if i not in target_indexes])] += 1

        return Structure(
            num_red_pyramids=structure_attribute_list[0],
            num_red_wedges=structure_attribute_list[1],
            num_red_blocks=structure_attribute_list[2],
            num_blue_pyramids=structure_attribute_list[3],
            num_blue_wedges=structure_attribute_list[4],
            num_blue_blocks=structure_attribute_list[5],
            num_yellow_pyramids=structure_attribute_list[6],
            num_yellow_wedges=structure_attribute_list[7],
            num_yellow_blocks=structure_attribute_list[8],
        )

    def does_test_structure_fit_moderator_rule(self, structure: Structure) -> bool:
        """
        Returns a boolean whether a structure matches the rule
        """
        return self._rule.does_structure_fit_rule(structure)

    def guess_rule(self, rule: str) -> bool:
        """
        Returns a boolean whether a string matches the rule
        """
        return str(self._rule).lower() == rule.lower()

    @property
    def base_structures(self):
        return self._base_structures

    @property
    def rule(self):
        return self._rule
