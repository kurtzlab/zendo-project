# priority queue of rules. test new rules until find one that matches. then try to disprove.
import random
from constants import MAX_QTY
from structure import Structure
from rule import Rule

class Rulex:

    def __init__(self, priority_queue_of_rules=[]) -> None:
        """
        :param priority_queue_of_rules: list of rules ordered from least complex to most complex  [least --> most]
        """
        self.priority_queue_of_rules = priority_queue_of_rules
        self.current_rule_idx = 0
        self.num_structures_check_for_guess = 1000

    def find_next_working_rule(self, structures_in_play_dict):
        """
        Iterates through possible rules until one is found that fits all structures currently in play.
        If not more rules exist, raises ValueError
        """
        if not self.priority_queue_of_rules:
            raise ValueError("No rules were provided")

        fits_all_structures = False
        rule = None
        while not fits_all_structures and self.current_rule_idx < len(self.priority_queue_of_rules):
            fits_all_structures = True
            for structure, does_structure_fit_rule in structures_in_play_dict.items():
                rule = Rule(self.priority_queue_of_rules[self.current_rule_idx])
                if rule.does_structure_fit_rule(structure) != does_structure_fit_rule:
                    fits_all_structures = False
                    break
            self.current_rule_idx += 1

        if not fits_all_structures:
            raise ValueError("No remaining rules. Could not find a valid rule")
        return rule

    def find_rule(self, structures_in_play_dict, moderator_rule):
        """
        Get the next rule candidate. Create test candidate structure that does not fit this rule and test if the moderator rule agrees.
        """
        next_rule = self.find_next_working_rule(structures_in_play_dict)
        count = 0
        while count < self.num_structures_check_for_guess:
            test_structure = self.generate_test_structure(structures_in_play_dict, moderator_rule)
            structures_in_play_dict[test_structure] = moderator_rule.does_structure_fit_rule(test_structure)
            if next_rule.does_structure_fit_rule(test_structure) == structures_in_play_dict[test_structure]:
                count += 1
            else:
                next_rule = self.find_next_working_rule(structures_in_play_dict)
                count = 0
        return next_rule

    def generate_test_structure(self, structures_in_play_dict, moderator_rule):
        possible_next = None
        is_unique = False
        while not possible_next and not is_unique:
            is_unique = True
            possible_next = Structure(
                num_red_pyramids=random.randrange(0, MAX_QTY + 1),
                num_red_wedges=random.randrange(0, MAX_QTY + 1),
                num_red_blocks=random.randrange(0, MAX_QTY + 1),
                num_blue_pyramids=random.randrange(0, MAX_QTY + 1),
                num_blue_wedges=random.randrange(0, MAX_QTY + 1),
                num_blue_blocks=random.randrange(0, MAX_QTY + 1),
                num_yellow_pyramids=random.randrange(0, MAX_QTY + 1),
                num_yellow_wedges=random.randrange(0, MAX_QTY + 1),
                num_yellow_blocks=random.randrange(0, MAX_QTY + 1),
            )
            for structure in structures_in_play_dict:
                if structure == possible_next:
                    is_unique = False
                    break
        structures_in_play_dict[possible_next] = moderator_rule.does_structure_fit_rule(possible_next)
        return possible_next