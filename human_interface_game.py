"""
Zendo game with human observer and computer moderator
"""
import sys
from zendo_moderator import ZendoModerator
from structure import Structure
from rule import Rule
from constants import (
    RED, BLUE, YELLOW, EXACTLY, AT_LEAST, PYRAMIDS, WEDGES, BLOCKS
)


class ZendoHumanGame:
    """
    Play the role of observer in Zendo.
    """

    def __init__(self, difficulty="easy") -> None:
        assert difficulty in ["easy", "medium", "hard"]
        self._moderator = ZendoModerator(difficulty=difficulty)
        print(f"The base structures are:\n{self._moderator.base_structures[0]}\n{self._moderator.base_structures[1]}\n")
        self.play_zendo()


    def play_zendo(self):
        """
        Plays zendo
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
                print(f"\nDoes your structure fit the rule? {self._moderator.does_test_structure_fit_moderator_rule(tmp_structure)}")
            elif command == valid_commands[2].lower():
                rule = input("Enter guess:\n")
                if self._moderator.guess_rule(rule):
                    print("You won!")
                else:
                    print(f"Incorrect, the rule was: {self._moderator.rule}")
                break
            elif command == valid_commands[3].lower():
                print(self._moderator.rule)
            elif command != valid_commands[0].lower():
                print("Invalid command")
            print("\n")


if __name__ == "__main__":
    diff = sys.argv[1]
    ZendoHumanGame(difficulty=diff)
