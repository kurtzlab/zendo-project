**Instructions to play:**

 1. Install python 3 - https://www.python.org/downloads/
 2. Clone the repo - `git clone https://github.com/kurtzlab/zendo-project.git`
 3. CD into the root - `cd zendo-project/`
 4. Run human_interface_game.py - `python3 human_interface_game.py easy` where you can set the difficulty to `easy` `medium` or `hard`.

**Notes Regarding Zendo:**

 1. There are two roles - moderator and observer. You are playing the role of the observer. The moderator (computer) will generate a rule and two base structures. From there you must generate test structures to see if they fit the rule or not, as well as guess the rule.
 2. Upper / Lower case doesn't matter.
 3. Rules should be in the format `QTY_TYPE QTY COLOR SHAPE`. `QTY TYPE` and `QTY` are required. At least one of `COLOR` or `SHAPE` is required. `QTY_TYPE` can be either `EXACTLY` or `AT_LEAST`. `QTY` is an integer >= 0.
