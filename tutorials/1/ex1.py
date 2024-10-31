import gym

env = gym.make('CartPole-v1')
print('Observation space:', env.observation_space)
print('Action space:', env.action_space)

for _ in range(10):
    obs = env.reset()
    done = False
    tot_rwd = 0
    n_steps = 0
    while not done:
        env.render()
        action = env.action_space.sample()
        obs, reward, done, info = env.step(action)
        tot_rwd += reward
        n_steps += 1
        
    print('Episode done! Total reward:', tot_rwd, 'Number of steps:', n_steps)