"""
Unittests for zendo project
"""
from zendo_moderator import ZendoModerator
from constants import BLOCKS, PYRAMIDS, RED, YELLOW
import unittest

from structure import Structure
from rule import Rule


class TestStructure(unittest.TestCase):

    def test_creating_structures(self):
        """
        Tests creating a structure with various parameters
        """
        structure = Structure(
            num_red_pyramids=1,
            num_red_wedges=2,
            num_red_blocks=3,
            num_blue_pyramids=4,
            num_blue_wedges=5,
            num_blue_blocks=6,
            num_yellow_pyramids=7,
            num_yellow_wedges=8,
            num_yellow_blocks=9,
        )
        self.assertEqual(structure.num_red_pyramids, 1)
        self.assertEqual(structure.num_red_wedges, 2)
        self.assertEqual(structure.num_red_blocks, 3)
        self.assertEqual(structure.num_blue_pyramids, 4)
        self.assertEqual(structure.num_blue_wedges, 5)
        self.assertEqual(structure.num_blue_blocks, 6)
        self.assertEqual(structure.num_yellow_pyramids, 7)
        self.assertEqual(structure.num_yellow_wedges, 8)
        self.assertEqual(structure.num_yellow_blocks, 9)
        self.assertEqual(structure.num_red, 6)
        self.assertEqual(structure.num_blue, 15)
        self.assertEqual(structure.num_yellow, 24)
        self.assertEqual(structure.num_pyramids, 12)
        self.assertEqual(structure.num_wedges, 15)
        self.assertEqual(structure.num_blocks, 18)


class TestRule(unittest.TestCase):

    def test_creating_rules(self):
        """
        Test creating valid rules
        """
        rule1 = Rule(rule="EXACTLY 2 RED BLOCKS")
        rule2 = Rule(rule="EXACTLY 1 YELLOW")
        rule3 = Rule(rule="AT_LEAST 3 PYRAMIDS")

        self.assertEqual(rule1.is_exactly, True)
        self.assertEqual(rule2.is_exactly, True)
        self.assertEqual(rule3.is_exactly, False)

        self.assertEqual(rule1.is_at_least, False)
        self.assertEqual(rule2.is_at_least, False)
        self.assertEqual(rule3.is_at_least, True)

        self.assertEqual(rule1.quantity, 2)
        self.assertEqual(rule2.quantity, 1)
        self.assertEqual(rule3.quantity, 3)

        self.assertEqual(rule1.color, RED)
        self.assertEqual(rule2.color, YELLOW)
        self.assertEqual(rule3.color, None)

        self.assertEqual(rule1.shape, BLOCKS)
        self.assertEqual(rule2.shape, None)
        self.assertEqual(rule3.shape, PYRAMIDS)

    def test_creating_invalid_rules(self):
        """
        Test creating invalid rules
        """
        with self.assertRaises(ValueError):
            Rule(rule="EXACTLY TWO RED BLOCKS")

        with self.assertRaises(ValueError):
            Rule(rule="INVALID 2 RED BLOCKS")

        with self.assertRaises(ValueError):
            Rule(rule="EXACTLY 0 YELLOW")

    def test_does_structure_fit_rule(self):
        """
        Test if structures match a rule
        """
        rule1 = Rule("AT_LEAST 2 BLOCKS")
        structure1 = Structure(
            num_red_blocks=0,
            num_blue_blocks=1,
            num_yellow_blocks=1,
        )
        structure2 = Structure(
            num_red_pyramids=5,
            num_red_blocks=1
        )
        self.assertTrue(rule1.does_structure_fit_rule(structure1))
        self.assertFalse(rule1.does_structure_fit_rule(structure2))

        rule2 = Rule("EXACTLY 4 BLUE")
        structure3 = Structure(
            num_blue_pyramids=3,
            num_blue_wedges=1,
            num_blue_blocks=0,
        )
        structure4 = Structure(
            num_blue_blocks=5,
        )
        self.assertTrue(rule2.does_structure_fit_rule(structure3))
        self.assertFalse(rule2.does_structure_fit_rule(structure4))

        rule3 = Rule("EXACTLY 1 RED PYRAMIDS")
        structure5 = Structure(
            num_red_pyramids=1,
            num_red_blocks=5,
            num_blue_pyramids=3,
        )
        structure6 = Structure()
        self.assertTrue(rule3.does_structure_fit_rule(structure5))
        self.assertFalse(rule3.does_structure_fit_rule(structure6))


class TestZendoModerator(unittest.TestCase):

    def test_base_structures_abide_by_rule(self):
        """
        Tests creating a moderator and assert the base rule and structures generated
        """
        mod_easy = ZendoModerator()
        for base_structure in mod_easy.base_structures:
            self.assertTrue(mod_easy.does_test_structure_fit_moderator_rule(base_structure))

        mod_medium = ZendoModerator(difficulty="medium")
        for base_structure in mod_medium.base_structures:
            self.assertTrue(mod_medium.does_test_structure_fit_moderator_rule(base_structure))

        mod_hard = ZendoModerator(difficulty="hard")
        for base_structure in mod_hard.base_structures:
            self.assertTrue(mod_hard.does_test_structure_fit_moderator_rule(base_structure))
