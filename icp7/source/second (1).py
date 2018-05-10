import gym
import numpy as np

EPISODES = 1000

if __name__ == "__main__":
    env = gym.make('CartPole-v1')
    state_size = env.observation_space.shape[0]
    action_size = env.action_space.n
    done = False
    batch_size = 32

    for e in range(EPISODES):
        state = env.reset()
        state = np.reshape(state, [1, state_size])
        for time in range(500):
            env.render()
            next_state, reward, done, _ = env.step(env.action_space.sample())
            reward = reward if not done else -10
            next_state = np.reshape(next_state, [1, state_size])
            state = next_state
            if done:
                print("episode: {}/{}, score: {}".format(e, EPISODES, time))
                break