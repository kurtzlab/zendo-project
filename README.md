**Zendo Research Project**
The purpose of this codebase is to play the board game Zendo. https://www.looneylabs.com/games/zendo
We are writing transparent code to demonstrate robust Artificial Intelligence in the domain of Zendo. This project is intended to illustry cognitive decision making ability in machines.

Zendo consists of two players: a moderator and observer. The moderator picks a random rule and builds two base case structures that adhere to the rule. Then, the observer can either guess what the rule is, or build additional structures, to which the moderator states whether or not these additional structures adhere to the rule.

There are two ways to play in this repo:

 1. Human Observer vs. Computer Moderator (human_interface_game.py)
 2. Computer Observer vs. Computer Moderator (zendo_game.py)

**Instructions to play human vs. computer:**

 1. Install python 3 - https://www.python.org/downloads/
 2. Clone the repo - `git clone https://github.com/kurtzlab/zendo-project.git`
 3. CD into the root - `cd zendo-project/`
 4. Run human_interface_game.py with a difficulty - `python3 human_interface_game.py easy`. Difficulty defaults to easy; options are `easy`, `medium`, `hard`.