"""
Zendo game with human observer and computer moderator
"""
import sys
import logging
from rule import Rule
from zendo_moderator import ZendoModerator
from structure import Structure


class ZendoHumanGame:
    """
    Play the role of observer in Zendo.
    """

    def __init__(self, difficulty: str = "easy") -> None:
        assert difficulty in ["easy", "medium", "hard"]
        self._moderator = ZendoModerator(difficulty=difficulty)
        logging.info(f"The base structures are:\n{self._moderator.base_structures[0]}\n{self._moderator.base_structures[1]}\n")


    def play_zendo(self):
        """
        Plays zendo by asking for human input to play the role of the observer
        """
        valid_commands = ["Quit", "Create Structure", "Guess Rule", "Show Rule"]
        command = ""
        while command != valid_commands[0].lower():
            command = input(f"Enter a command: {valid_commands}\n").lower()
            if command == valid_commands[1].lower():
                num_red_pyramids = int(input(f"Enter num_red_pyramids: "))
                num_red_wedges = int(input(f"Enter num_red_wedges: "))
                num_red_blocks = int(input(f"Enter num_red_blocks: "))
                num_blue_pyramids = int(input(f"Enter num_blue_pyramids: "))
                num_blue_wedges = int(input(f"Enter num_blue_wedges: "))
                num_blue_blocks = int(input(f"Enter num_blue_blocks: "))
                num_yellow_pyramids = int(input(f"Enter num_yellow_pyramids: "))
                num_yellow_wedges = int(input(f"Enter num_yellow_wedges: "))
                num_yellow_blocks = int(input(f"Enter num_yellow_blocks: "))

                tmp_structure = Structure(
                    num_red_pyramids=num_red_pyramids,
                    num_red_wedges=num_red_wedges,
                    num_red_blocks=num_red_blocks,
                    num_blue_pyramids=num_blue_pyramids,
                    num_blue_wedges=num_blue_wedges,
                    num_blue_blocks=num_blue_blocks,
                    num_yellow_pyramids=num_yellow_pyramids,
                    num_yellow_wedges=num_yellow_wedges,
                    num_yellow_blocks=num_yellow_blocks
                )
                logging.info(f"\nDoes your structure fit the rule?: {self._moderator.does_test_structure_fit_moderator_rule(tmp_structure)}")
            elif command == valid_commands[2].lower():
                rule = input("Enter guess:\n")
                if Rule(rule) == self._moderator.rule:
                    logging.info("You won!")
                else:
                    logging.info(f"Incorrect, the rule was: {self._moderator.rule}")
                break
            elif command == valid_commands[3].lower():
                logging.info(self._moderator.rule)
            elif command != valid_commands[0].lower():
                logging.info("Invalid command")

            logging.info("\n")


if __name__ == "__main__":
    diff = sys.argv[1]
    zhg = ZendoHumanGame(difficulty=diff)
    zhg.play_zendo()
