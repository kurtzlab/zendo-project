import random
from typing import Dict
from structure import Structure
from constants import MAX_QTY


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
            if structure == possible_unique_structure:
                is_unique = False
                break
    return possible_unique_structure