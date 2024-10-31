# import gym
# from gym import spaces
import gymnasium as gym
from gymnasium import spaces
from gymnasium.wrappers import TimeLimit
import numpy as np
import stable_baselines3 as sb3
from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy

class SecretSequenceEnv(gym.Env):
    """
    A simple Gym environment where the agent needs to discover a secret sequence of actions.
    - Action space: N discrete actions (0 to N-1).
    - Observation: Number of correct actions taken in sequence so far (0 to L).
    - Reward: 1 when the entire sequence is correctly completed, else 0.
    """
    def __init__(self, N=5, L=3, seed=None):
        super().__init__()
        self.N = N  # Number of discrete actions
        self.L = L  # Length of the secret sequence

        # Define action and observation spaces
        self.action_space = spaces.Discrete(self.N)
        self.observation_space = spaces.Discrete(self.L + 1)

        # Initialize the secret sequence and the current step
        self.secret_sequence = np.random.randint(self.N, size=self.L)
        self.current_step = 0

    def reset(self, seed=None):
        """
        Resets the environment to an initial state and returns the initial observation.
        """
        
        super().reset(seed=seed)
        self.current_step = 0
        # self.secret_sequence = np.random.randint(self.N, size=self.L)
        info = {}
        return self.current_step, info

    def step(self, action):
        """
        Executes one time step within the environment.
        """
        reward = -1 # Default reward when the action is incorrect
        done = False
        truncated = False

        if action == self.secret_sequence[self.current_step]:
            reward = 0  # Correct action
            self.current_step += 1
            if self.current_step == self.L:
                reward = 1  # Sequence completed successfully
                done = True
        else:
            self.current_step = 0  # Incorrect action, reset progress

        observation = self.current_step
        info = {}
        return observation, reward, done, truncated, info


if __name__=="__main__":
    env = TimeLimit(SecretSequenceEnv(N=5, L=3), max_episode_steps=100)
    # env = TimeLimit(SecretSequenceEnv(N=10, L=10), max_episode_steps=100)
    
    model = PPO("MlpPolicy", env, verbose=1)
    mean_reward, std_reward = evaluate_policy(model, model.get_env(), n_eval_episodes=10)
    print(f"Mean reward: {mean_reward:.2f} +/- {std_reward:.2f}")
    
    model.learn(10_000)
    
    mean_reward, std_reward = evaluate_policy(model, model.get_env(), n_eval_episodes=10)
    print(f"Mean reward: {mean_reward:.2f} +/- {std_reward:.2f}")