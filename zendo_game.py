"""
Zendo game play computer vs. computer
"""
import logging
from zendo_moderator import ZendoModerator
from zendo_observer import ZendoObserver


class ZendoGame:
    """
    Play a game of zendo
    """

    def __init__(self, difficulty : str = "easy") -> None:
        """
        Create moderator and observer

        :param difficulty: string moderator difficulty. Can be 'easy', 'medium', or 'hard'
        :return: None
        """
        self._moderator = ZendoModerator(difficulty=difficulty)
        self._observer = ZendoObserver(self._moderator)


    def play_zendo(self, verbose : bool = False) -> bool:
        """
        Plays zendo

        :param verbose: when true, logs incorrect guesses to help improve AI
        :return: boolean if guessed the correct rule
        """
        observer_guess = self._observer.play()
        did_ai_win = self._moderator.rule == observer_guess
        if verbose and not did_ai_win:
            logging.warning(f"Incorrect guess: {observer_guess}. Correct rule was {self._moderator.rule}")
        return did_ai_win

if __name__ == '__main__':
    # simulate 1000 games to get a win %
    num_games = 1000
    wins = 0
    for i in range(num_games):
        logging.info(f"Game {i} of {num_games}")
        zg = ZendoGame()
        wins += 1 if zg.play_zendo() else 0
    logging.info(f"{wins} wins from {num_games} games. {float(wins) / num_games}% win rate")