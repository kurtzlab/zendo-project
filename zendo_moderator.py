"""
Zendo moderator
"""
import random
from structure import Structure
from rule import Rule
from constants import (
    MAX_QTY, MIN_QUANTITY, RED, BLUE, YELLOW, EXACTLY, AT_LEAST, PYRAMIDS, WEDGES, BLOCKS
)


class ZendoModerator:
    """
    Play the role of moderator in Zendo.
    """

    def __init__(self, difficulty : str = "easy") -> None:
        """
        Create base example structures

        :param difficulty: string moderator difficulty. Can be 'easy', 'medium', or 'hard'
        :return: None
        """
        self.rule = self.gen_rule()
        self.base_structures = []
        num_base_structures = 2
        for _ in range(num_base_structures):
            self.base_structures.append(
                self.generate_random_structure_according_to_rule(
                    rule=self.rule,
                    difficulty=difficulty,
                )
            )


    def gen_rule(self) -> Rule:
        """
        Generates and returns a random rule

        :return: Rule object
        """
        color_options = [RED, BLUE, YELLOW]
        number_type_options = [EXACTLY, AT_LEAST]
        number_options = list(
            range(MIN_QUANTITY, MAX_QTY + 1)
        )
        block_type_options = [PYRAMIDS, WEDGES, BLOCKS]
        color_block_combo_options = ["both", "only_color", "only_block"]

        rule_string = f"{random.choice(number_type_options)} {str(random.choice(number_options))} "  # extra space at end to add color/block type
        color_block_combo = random.choice(color_block_combo_options)
        if color_block_combo == "both":
            rule_string += f"{random.choice(color_options)} {random.choice(block_type_options)}"
        elif color_block_combo == "only_color":
            rule_string += random.choice(color_options)
        elif color_block_combo == "only_block":
            rule_string += random.choice(block_type_options)

        return Rule(rule_string)

    @staticmethod
    def generate_random_structure_according_to_rule(
        rule: Rule = None,
        difficulty: str = "easy"
    ):
        """
        Create and return structures that abide by the rule

        :param rule: rule object to fit structure to
        :param difficulty: string difficulty. Can be "easy", "medium", or "hard"
        """
        if not rule:
            return None

        # for AT_LEAST add up to 3 extra qty
        at_least_extra_qty = 0
        if rule.is_at_least:
            at_least_extra_qty = random.choice(list(range(4)))

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
        if rule.color and rule.shape: target_indexes = structure_attribute_to_index_dict[rule.color + rule.shape]
        elif rule.color: target_indexes = structure_attribute_to_index_dict[rule.color]
        elif rule.shape: target_indexes = structure_attribute_to_index_dict[rule.shape]

        # add random components
        for _ in range(rule.quantity + at_least_extra_qty):
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

        :param structure: structure obj to test against rule
        :return: boolean whether or not structure fits rule
        """
        return self.rule.does_structure_fit_rule(structure)
