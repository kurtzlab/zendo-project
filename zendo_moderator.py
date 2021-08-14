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

        if rule_is_at_least:
            if random.choice([0, 1]) == 1:
                rule_quantity += random.choice(list(range(1, 5)))

        extra_qty_for_difficulty = 0
        if difficulty == "medium": extra_qty_for_difficulty = 3
        elif difficulty == "hard": extra_qty_for_difficulty = 5

        # list where index 0-8 represents the folowing:
        # num_red_pyramids, num_red_wedges, num_red_blocks,
        # num_blue_pyramids, num_blue_wedges, num_blue_blocks,
        # num_yellow_pyramids, num_yellow_wedges, num_yellow_blocks
        structure_attribute_list = [0] * 9

        if rule_color and rule_shape:
            if rule_shape == PYRAMIDS:
                if rule_color == RED: structure_attribute_list[0] = rule_quantity
                elif rule_color == BLUE: structure_attribute_list[3] = rule_quantity
                elif rule_color == YELLOW: structure_attribute_list[6] = rule_quantity
            elif rule_shape == WEDGES:
                if rule_color == RED: structure_attribute_list[1] = rule_quantity
                elif rule_color == BLUE: structure_attribute_list[4] = rule_quantity
                elif rule_color == YELLOW: structure_attribute_list[7] = rule_quantity
            elif rule_shape == BLOCKS:
                if rule_color == RED: structure_attribute_list[2] = rule_quantity
                elif rule_color == BLUE: structure_attribute_list[5] = rule_quantity
                elif rule_color == YELLOW: structure_attribute_list[8] = rule_quantity
            extra_difficulty_count = 0
            while extra_difficulty_count < extra_qty_for_difficulty:
                index = random.choice([i for i in range(3, 9)])
                if structure_attribute_list[index] == 0:
                    structure_attribute_list[index] += 1
                    extra_difficulty_count += 1
        elif rule_color:
            if rule_color == RED:
                for _ in range(rule_quantity):
                    structure_attribute_list[random.choice([i for i in range(0, 3)])] += 1
                for _ in range(extra_qty_for_difficulty):
                    structure_attribute_list[random.choice([i for i in range(3, 9)])] += 1
            elif rule_color == BLUE:
                for _ in range(rule_quantity):
                    structure_attribute_list[random.choice([i for i in range(3, 6)])] += 1
                for _ in range(extra_qty_for_difficulty):
                    structure_attribute_list[random.choice([i for i in range(0, 3)] + [i for i in range(6, 9)])] += 1
            elif rule_color == YELLOW:
                for _ in range(rule_quantity):
                    structure_attribute_list[random.choice([i for i in range(6, 9)])] += 1
                for _ in range(extra_qty_for_difficulty):
                    structure_attribute_list[random.choice([i for i in range(0, 6)])] += 1
        elif rule_shape:
            if rule_shape == PYRAMIDS:
                for _ in range(rule_quantity):
                    structure_attribute_list[random.choice([0, 3, 6])] += 1
                for _ in range(extra_qty_for_difficulty):
                    structure_attribute_list[random.choice([1, 2, 4, 5, 7, 8])] += 1
            elif rule_shape == WEDGES:
                for _ in range(rule_quantity):
                    structure_attribute_list[random.choice([1, 4, 7])] += 1
                for _ in range(extra_qty_for_difficulty):
                    structure_attribute_list[random.choice([0, 2, 3, 5, 6, 8])] += 1
            elif rule_shape == BLOCKS:
                for _ in range(rule_quantity):
                    structure_attribute_list[random.choice([2, 5, 8])] += 1
                for _ in range(extra_qty_for_difficulty):
                    structure_attribute_list[random.choice([0, 1, 3, 4, 6, 7])] += 1

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

    @property
    def base_structures(self):
        return self._base_structures
