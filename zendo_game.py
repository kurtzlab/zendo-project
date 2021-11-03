"""
Zendo game play
"""
import random
from zendo_moderator import ZendoModerator
from zendo_observer import ZendoObserver
from structure import Structure
from rule import Rule
from constants import (
    RED, BLUE, YELLOW, EXACTLY, AT_LEAST, PYRAMIDS, WEDGES, BLOCKS
)


class ZendoGame:
    """
    Play the role of observer in Zendo.
    """

    def __init__(self, difficulty="easy") -> None:
        self._moderator = ZendoModerator(difficulty=difficulty)
        self._observer = ZendoObserver(self._moderator)


    def play_zendo(self):
        """
        Plays zendo
        """
        observer_guess = self._observer.play()
        #print(f"Moderator Rule: {self._moderator.rule}\nObserver Guess: {observer_guess}\nWin?: {self._moderator.rule == observer_guess}")
        return self._moderator.rule == observer_guess

if __name__ == '__main__':
    wins = 0
    num_games = 1000
    for i in range(num_games):
        print(i)
        zg = ZendoGame()
        win = zg.play_zendo()
        if win: wins += 1
    print(f"{wins} wins from {num_games} games. {float(wins) / num_games}% win rate")