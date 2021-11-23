import os
import random
import json
from typing import Dict
from structure import Structure
from constants import (
    MAX_QTY, MIN_QUANTITY, PRIORITY_QUEUE_OF_RULES_FILE_NAME, EXACTLY, AT_LEAST, PYRAMIDS, BLOCKS, RED, BLUE, YELLOW, WEDGES
)


def generate_test_structure(structures_in_play_dict: Dict) -> Structure:
    """
    Generate a random test structure that hasn't been seen before

    :param structures_in_play_dict: dictionary of all built structures and boolean if the structure abides by the moderator rule. {structure obj: boolean}
    :return: random structure object
    """
    is_unique = False
    possible_unique_structure = None
    while not is_unique:
        is_unique = True
        possible_unique_structure = Structure(
            num_red_pyramids=random.randrange(MIN_QUANTITY, MAX_QTY + 1),
            num_red_wedges=random.randrange(MIN_QUANTITY, MAX_QTY + 1),
            num_red_blocks=random.randrange(MIN_QUANTITY, MAX_QTY + 1),
            num_blue_pyramids=random.randrange(MIN_QUANTITY, MAX_QTY + 1),
            num_blue_wedges=random.randrange(MIN_QUANTITY, MAX_QTY + 1),
            num_blue_blocks=random.randrange(MIN_QUANTITY, MAX_QTY + 1),
            num_yellow_pyramids=random.randrange(MIN_QUANTITY, MAX_QTY + 1),
            num_yellow_wedges=random.randrange(MIN_QUANTITY, MAX_QTY + 1),
            num_yellow_blocks=random.randrange(MIN_QUANTITY, MAX_QTY + 1),
        )
        for structure in structures_in_play_dict:
            if structure == possible_unique_structure:
                is_unique = False
                break
    return possible_unique_structure


def load_rules() -> Dict[str, int]:
    """
    Load the priority queue of rules from a file

    :return: Dict of {string rule: rule value (based on how often it is the correct / incorrect rule)}
    """
    # if first run, create the initial file
    if not os.path.isfile(PRIORITY_QUEUE_OF_RULES_FILE_NAME):
        all_possible_rules = [
            f"{qty} {i} {color}" for qty in [EXACTLY, AT_LEAST] for i in range(MIN_QUANTITY, MAX_QTY + 1) for color in [RED, BLUE, YELLOW]
        ] + [
            f"{qty} {i} {shape}" for qty in [EXACTLY, AT_LEAST] for i in range(MIN_QUANTITY, MAX_QTY + 1) for shape in [PYRAMIDS, WEDGES, BLOCKS]
        ] + [
            f"{qty} {i} {color} {shape}" for qty in [EXACTLY, AT_LEAST] for i in range(MIN_QUANTITY, MAX_QTY + 1) for color in [RED, BLUE, YELLOW] for shape in [PYRAMIDS, WEDGES, BLOCKS]
        ]
        # 2 cols: rules, number of victories (defaults to 0)
        rules_to_vals_dict = {rule: 0 for rule in all_possible_rules}
        with open(PRIORITY_QUEUE_OF_RULES_FILE_NAME, "w") as file:
            file.write(json.dumps(rules_to_vals_dict))
    else:
        with open(PRIORITY_QUEUE_OF_RULES_FILE_NAME, "rb") as file:
            rules_to_vals_dict = json.loads(file.read())

    return rules_to_vals_dict


def save_rules_to_file(rules_dict) -> None:
    """
    Save the priority queue of rules

    :param rules_dict: Dict of {string rule: rule value (based on how often it is the correct / incorrect rule)}
    :return: None
    """
    with open(PRIORITY_QUEUE_OF_RULES_FILE_NAME, "w") as file:
        file.write(json.dumps(rules_dict))
