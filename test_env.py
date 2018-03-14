import gym
import gym_sokoban
from gym_sokoban.envs.room_utils import ACTION_LOOKUP
import time
from scipy.misc import imsave
ts = time.time()
env = gym.make('Sokoban-v0')
#env = gym.make('CartPole-v0')
for i_episode in range(1):#20
    observation = env.reset()
    observation = env.render(mode='rgb_array')
    imsave('docs/run_{}_step_{}.png'.format(ts, -1), observation)
    for t in range(100):#100
        env.render()#mode='rgb_array')
        time.sleep(1)
        #print(observation)
        action = env.action_space.sample()
        #env.step(0)
        action = input('Select action')
        try:
            action = int(action)
        except:
            action = 0
        observation, reward, done, info = env.step(action)
        imsave('docs/run_{}_step_{}.png'.format(ts, t), observation)
        print(ACTION_LOOKUP[action], reward, done, info)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            env.render()
            break

time.sleep(10)