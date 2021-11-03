import random
# state all towers on table. actions are diff structures to make
# 2 seed towers, all labeled towers are. state of positive
# hypergrid. each tower is 1 piece. grid color x shape. fits or no. generalize to tower
# environment contains every single possible structure. only need structures accessible by action. neighbors
class QLearningAgent:
    """
    Q-Learning Agent
    """
    def __init__(self, epsilon=0.5):
        self.Q = {}
        self.epsilon = epsilon

    def get_q_val(self, state, action):
        """
        Returns q val
        """
        return self.Q.get((state, action), None) or 0.0

    def get_next_action(self, state):
        """
        Get next action
        """
        actions = self.get_actions_from_state(state)
        if not actions: return None
        action = None
        if random.random() < self.epsilon:
          action = random.choice(actions)
        else:
          action = self.getPolicy(state)

        return action

    def update(self, state, action, nextState, reward):
        """
          The parent class calls this to observe a
          state = action => nextState and reward transition.
          You should do your Q-Value update here

          NOTE: You should never call this function,
          it will be called on your behalf
        """
        "*** YOUR CODE HERE ***"
        q_val = self.get_q_val(state, action)
        next_val = self.getValue(nextState)
        next_q_val = q_val + self.alpha * (reward + self.discount * next_val - q_val)
        self.Q[(state, action)] = next_q_val
        

    def getPolicy(self, state):
        """
        Return best action to take from state
        """
        actions = self.get_actions_from_state(state)
        if not actions: return None
        return [action for action in actions if self.getValue(state) == self.get_q_val(state, action)][0]

    def getValue(self, state):
        """
        Return max q val based on a given state
        """
        actions = self.get_actions_from_state(state)
        if not actions: return 0.0
        return max([self.get_q_val(state, action) for action in actions])

    def get_actions_from_state(self, state):
        pass