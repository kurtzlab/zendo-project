"""
Class to represent a zendo rules. Specifications can be found here:
https://www.looneylabs.com/sites/default/files/literature/Zendo%20Rules%20Book%201.pdf
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
        :param rule: a string rule. Must be in format "quantity color and/or shape"

        Examples:
        EXACTLY 2 RED BLOCKS
        EXACTLY 0 YELLOW
        AT_LEAST 3 PYRAMIDS
        """
        self._str_rule = rule
        self._is_exactly = False
        self._is_at_least = False
        self._quantity = None
        self._color = None
        self._shape = None

        try:
            rule_list = rule.upper().split(" ")

            # parse quantity
            if rule_list[0] not in [EXACTLY, AT_LEAST]:
                raise ValueError("Rules must begin with a quantity")
            if rule_list[0] == EXACTLY: self._is_exactly = True
            elif rule_list[0] == AT_LEAST: self._is_at_least = True
            self._quantity = int(rule_list[1])

            # parse the color and shape
            if rule_list[2] in [RED, BLUE, YELLOW]:
                self._color = rule_list[2]
                if len(rule_list) == 4:
                    self._shape = rule_list[3]
            elif rule_list[2] in [PYRAMIDS, WEDGES, BLOCKS]:
                self._shape = rule_list[2]
        except Exception:
            raise ValueError("Invalid rule")

    @property
    def is_exactly(self):
        return self._is_exactly

    @property
    def is_at_least(self):
        return self._is_at_least

    @property
    def quantity(self):
        return self._quantity

    @property
    def color(self):
        return self._color

    @property
    def shape(self):
        return self._shape

    def does_structure_fit_rule(self, structure: Structure) -> bool:
        """
        Returns a boolean whether a structure matches the rule
        """
        structure_qty = 0

        # only specifies a color
        if self._color and not self._shape:
            if self._color == RED: structure_qty = structure.num_red
            elif self._color == BLUE: structure_qty = structure.num_blue
            elif self._color == YELLOW: structure_qty = structure.num_yellow

        # only specifies a shape
        elif self._shape and not self._color:
            if self._shape == PYRAMIDS: structure_qty = structure.num_pyramids
            elif self._shape == WEDGES: structure_qty = structure.num_wedges
            elif self._shape == BLOCKS: structure_qty = structure.num_blocks

        # both color and shape are given
        else:
            if self._shape == PYRAMIDS:
                if self._color == RED: structure_qty = structure.num_red_pyramids
                elif self._color == BLUE: structure_qty = structure.num_blue_pyramids
                elif self._color == YELLOW: structure_qty = structure.num_yellow_pyramids
            elif self._shape == WEDGES:
                if self._color == RED: structure_qty = structure.num_red_wedges
                elif self._color == BLUE: structure_qty = structure.num_blue_wedges
                elif self._color == YELLOW: structure_qty = structure.num_yellow_wedges
            elif self._shape == BLOCKS:
                if self._color == RED: structure_qty = structure.num_red_blocks
                elif self._color == BLUE: structure_qty = structure.num_blue_blocks
                elif self._color == YELLOW: structure_qty = structure.num_yellow_blocks

        # validate quantity
        if (self._is_exactly and structure_qty != self._quantity) or \
            (self._is_at_least and structure_qty < self._quantity): return False
        return True

    def __str__(self):
        return self._str_rule
