"""
Zendo observer
"""
from rule import Rule
from zendo_moderator import ZendoModerator
from structure import Structure
from rulex import Rulex


class ZendoObserver:
    """
    Computer playing the role of observer in Zendo.
    """
    MAX_TEST_STRUCTURES = 100

    def __init__(self, moderator: ZendoModerator) -> None:
        """
        Define the zendo moderator so we can access base structures and rule

        :param moderator: ZendoModerator obj
        :return: None
        """
        self.moderator = moderator

    def does_test_structure_fit_moderator_rule(self, structure: Structure, moderator: ZendoModerator) -> bool:
        """
        Returns a boolean whether a structure matches the rule

        :param structure: Structure obj to test against moderator rule
        :param moderator: ZendoModerator obj
        :return: boolean whether or not structure abides by moderator's rule
        """
        return moderator.does_test_structure_fit_moderator_rule(structure)

    def play(self, dict_of_possible_rules_to_rule_values) -> Rule:
        """
        Plays zendo

        :param dict_of_possible_rules_to_rule_values: Dict of {string rule: rule value (based on how often it is the correct / incorrect rule)}
        :return: rule object to make guess with
        """
        rulex_obj = Rulex(
            dict_of_possible_rules_to_rule_values=dict_of_possible_rules_to_rule_values,
        )
        structures_dict = dict(
            zip(
                self.moderator.base_structures,
                [True] * len(self.moderator.base_structures)
            )
        )
        rulex_guess = rulex_obj.find_guess(
            structures_in_play_dict=structures_dict,
            moderator_rule=self.moderator.rule
        )
        return rulex_guess

