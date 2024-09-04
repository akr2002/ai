import numpy as np
import random


# Define the environment
class GridWorld:
    def __init__(
        self,
        width,
        height,
        start,
        goal,
        obstacles,
        reward_goal=1,
        reward_obstacle=-1,
        reward_default=-0.04,
    ):
        self.width = width
        self.height = height
        self.start = start
        self.goal = goal
        self.obstacles = obstacles
        self.reward_goal = reward_goal
        self.reward_obstacle = reward_obstacle
        self.reward_default = reward_default
        self.state = start

    def is_terminal(self, state):
        return state == self.goal

    def get_actions(self):
        return ["up", "down", "left", "right"]

    def get_next_state(self, state, action):
        if self.is_terminal(state):
            return state

        x, y = state
        if action == "up":
            y -= 1
        elif action == "down":
            y += 1
        elif action == "left":
            x -= 1
        elif action == "right":
            x += 1

        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return state  # No change if out of bounds

        return (x, y)

    def get_reward(self, state):
        if state == self.goal:
            return self.reward_goal
        if state in self.obstacles:
            return self.reward_obstacle
        return self.reward_default

    def reset(self):
        self.state = self.start
        return self.state

    def step(self, action):
        next_state = self.get_next_state(self.state, action)
        reward = self.get_reward(next_state)
        self.state = next_state
        return next_state, reward


# Define Q-learning parameters
def q_learning(env, episodes=1000, alpha=0.1, gamma=0.9, epsilon=0.1):
    q_table = {}
    for x in range(env.width):
        for y in range(env.height):
            q_table[(x, y)] = {action: 0 for action in env.get_actions()}

    for episode in range(episodes):
        state = env.reset()

        while not env.is_terminal(state):
            if random.uniform(0, 1) < epsilon:
                action = random.choice(env.get_actions())
            else:
                action = max(q_table[state], key=q_table[state].get)

            next_state, reward = env.step(action)

            best_next_action = max(q_table[next_state], key=q_table[next_state].get)
            q_table[state][action] += alpha * (
                reward
                + gamma * q_table[next_state][best_next_action]
                - q_table[state][action]
            )

            state = next_state

    return q_table


# Example usage
if __name__ == "__main__":
    width, height = 5, 5
    start = (0, 0)
    goal = (4, 4)
    obstacles = [(1, 1), (2, 2), (3, 3)]

    env = GridWorld(width, height, start, goal, obstacles)
    q_table = q_learning(env, episodes=1000)

    # Print Q-table
    for state in sorted(q_table):
        print(f"State {state}: {q_table[state]}")
