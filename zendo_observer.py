"""
Zendo observer
"""
import random
from zendo_moderator import ZendoModerator
from structure import Structure
from rule import Rule
from constants import (
    RED, BLUE, YELLOW, EXACTLY, AT_LEAST, PYRAMIDS, WEDGES, BLOCKS, PRIORITY_QUEUE_OF_ALL_POSSIBLE_RULES
)
from rulex import Rulex


class ZendoObserver:
    """
    Play the role of observer in Zendo.
    """
    MAX_TEST_STRUCTURES = 100

    def __init__(self, moderator) -> None:
        self.moderator = moderator


    def gen_test_structure(self):
        """
        Generates and returns a test structure
        """
        pass

    def does_test_structure_fit_moderator_rule(self, structure: Structure, moderator: ZendoModerator) -> bool:
        """
        Returns a boolean whether a structure matches the rule
        """
        return moderator.does_test_structure_fit_moderator_rule(structure)

    def run_model(self, model_type="reinforcement"):
        """
        Run a model
        """
        if model_type == "reinforcement":
            pass

    def play(self):
        """
        Plays zendo
        """
        rulex_obj = Rulex(PRIORITY_QUEUE_OF_ALL_POSSIBLE_RULES)
        rules_dict = {}
        for i in self.moderator.base_structures:
            rules_dict[i] = True
        rulex_guess = rulex_obj.find_rule(rules_dict, self.moderator.rule)
        return rulex_guess

