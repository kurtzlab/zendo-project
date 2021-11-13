"""
Class to represent a zendo rules. Specifications can be found here:
https://www.looneylabs.com/sites/default/files/literature/Zendo%20Rules%20Book%201.pdf
To simplify the code, we've limited rules to only consist of quantities, colors, and shapes.
"""

from structure import Structure
from constants import (
    RED, BLUE, YELLOW, EXACTLY, AT_LEAST, PYRAMIDS, WEDGES, BLOCKS
)

class Rule:
    """
    Rules can be compromised of color, quantity, and shape.
    Rules must be in all caps, space separated, and follow the spelling conventions found in constants.py
    """

    def __init__(self, rule: str) -> None:
        """
        :param rule: a string rule. Must be in format: quantity color and/or shape

        Examples:
        EXACTLY 2 RED BLOCKS
        EXACTLY 0 YELLOW
        AT_LEAST 3 PYRAMIDS
        """
        self._str_rule = rule
        self.is_exactly = False
        self.is_at_least = False
        self.quantity = None
        self.color = None
        self.shape = None

        try:
            rule_list = rule.upper().split(" ")

            # parse quantity
            if rule_list[0] not in [EXACTLY, AT_LEAST]:
                raise ValueError("Rules must begin with a quantity")
            if rule_list[0] == EXACTLY:
                self.is_exactly = True
            elif rule_list[0] == AT_LEAST:
                self.is_at_least = True
            self.quantity = int(rule_list[1])

            # parse the color and shape
            if rule_list[2] in [RED, BLUE, YELLOW]:
                self.color = rule_list[2]
                if len(rule_list) == 4:
                    self.shape = rule_list[3]
            elif rule_list[2] in [PYRAMIDS, WEDGES, BLOCKS]:
                self.shape = rule_list[2]
        except Exception:
            raise ValueError("Invalid rule")

    def does_structure_fit_rule(self, structure: Structure) -> bool:
        """
        Returns a boolean whether a structure matches the rule

        :param structure: Structure object to check against rule
        :return: boolean if structure abides by the rule
        """
        structure_qty = 0

        # only specifies a color
        if self.color and not self.shape:
            if self.color == RED: structure_qty = structure.num_red
            elif self.color == BLUE: structure_qty = structure.num_blue
            elif self.color == YELLOW: structure_qty = structure.num_yellow

        # only specifies a shape
        elif self.shape and not self.color:
            if self.shape == PYRAMIDS: structure_qty = structure.num_pyramids
            elif self.shape == WEDGES: structure_qty = structure.num_wedges
            elif self.shape == BLOCKS: structure_qty = structure.num_blocks

        # both color and shape are given
        else:
            if self.shape == PYRAMIDS:
                if self.color == RED: structure_qty = structure.num_red_pyramids
                elif self.color == BLUE: structure_qty = structure.num_blue_pyramids
                elif self.color == YELLOW: structure_qty = structure.num_yellow_pyramids
            elif self.shape == WEDGES:
                if self.color == RED: structure_qty = structure.num_red_wedges
                elif self.color == BLUE: structure_qty = structure.num_blue_wedges
                elif self.color == YELLOW: structure_qty = structure.num_yellow_wedges
            elif self.shape == BLOCKS:
                if self.color == RED: structure_qty = structure.num_red_blocks
                elif self.color == BLUE: structure_qty = structure.num_blue_blocks
                elif self.color == YELLOW: structure_qty = structure.num_yellow_blocks

        # validate quantity
        if (self.is_exactly and structure_qty != self.quantity) or \
            (self.is_at_least and structure_qty < self.quantity): return False
        return True

    def __str__(self):
        return self._str_rule

    def __eq__(self, o: object) -> bool:
        return self.is_exactly == o.is_exactly and \
            self.is_at_least == o.is_at_least and \
            self.quantity == o.quantity and \
            self.color == o.color and \
            self.shape == o.shape
