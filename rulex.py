"""
Implimentation of RULEX model of AI hypothesis testing.
https://doi.org/10.1037/0033-295x.101.1.53
"""
from typing import Dict, List
from rule import Rule
from utils import generate_test_structure

class Rulex:
    """
    RULEX model
    """

    def __init__(self, dict_of_possible_rules_to_rule_values: Dict[str, int]) -> None:
        """
        :param dict_of_possible_rules_to_rule_values: Dict of {string rule: rule value (based on how often it is the correct / incorrect rule)}
        """
        self._dict_of_possible_rules_to_rule_values = dict_of_possible_rules_to_rule_values
        self._priority_queue_of_rules = [i[0] for i in sorted(dict_of_possible_rules_to_rule_values.items(), key=lambda x: x[1])]
        self._current_rule_idx = 0  # track where you are in priority queue
        self._num_structures_check_for_guess = 5  # number of structures the potential rule must fit correctly before making a guess

    def find_next_working_rule(self, structures_in_play_dict: Dict) -> Rule:
        """
        Used to find potential guesses for the rule.
        Iterates through possible rules until one is found that fits all structures currently in play.
        To "fit" all structures, the rule must fit structures that fit the moderator rule, and not fit the structures that don't fit the moderator rule.
        If no more rules exist, raises ValueError

        :param structures_in_play_dict: dictionary of all built structures and boolean if the structure abides by the moderator rule. {structure obj: boolean}
        :return: Rule object of next potential rule
        """
        if not self._priority_queue_of_rules:
            raise ValueError("No rules were provided")

        fits_all_structures = False
        rule = None

        # find a rule candidate
        while not fits_all_structures and self._current_rule_idx < len(self._priority_queue_of_rules):
            # create rule obj so we can check if structures fit
            rule = Rule(self._priority_queue_of_rules[self._current_rule_idx])

            fits_all_structures = True
            for structure, does_structure_fit_rule in structures_in_play_dict.items():
                if rule.does_structure_fit_rule(structure) != does_structure_fit_rule:
                    fits_all_structures = False
                    self._dict_of_possible_rules_to_rule_values[str(rule)] -= 1
                    self._current_rule_idx += 1
                    break

        if not fits_all_structures:
            raise ValueError("No remaining rules. Could not find a valid rule")
        self._dict_of_possible_rules_to_rule_values[str(rule)] += 1
        return rule

    def find_guess(self, structures_in_play_dict: Dict, moderator_rule: Rule) -> Rule:
        """
        Loops through potential rules until find one that agrees with the moderator rule on self._num_structures_check_for_guess number of structures

        :param structures_in_play_dict: dictionary of all built structures and boolean if the structure abides by the moderator rule. {structure obj: boolean}
        :param moderator_rule: the moderator rule object
        :return: rule object to make guess with
        """
        count = 0
        next_rule = self.find_next_working_rule(structures_in_play_dict)

        while count < self._num_structures_check_for_guess:
            test_structure = generate_test_structure(
                structures_in_play_dict=structures_in_play_dict,
            )
            # add the test to the structures in play
            structures_in_play_dict[test_structure] = moderator_rule.does_structure_fit_rule(test_structure)
            if next_rule.does_structure_fit_rule(test_structure) == structures_in_play_dict[test_structure]:
                count += 1
            else:
                next_rule = self.find_next_working_rule(structures_in_play_dict)
                count = 0
        return next_rule
