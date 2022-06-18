from __future__ import print_function

from abc import ABCMeta, abstractmethod

class BaseEnv:

    __metaclass__ = ABCMeta
    def __init__():
        reward = None

    @abstractmethod
    def env_init(self):
        reward = None
        observation = None
        termination = None
        self.reward_obs_term = (reward, observation, termination)
    
    @abstractmethod
    def env_start(self, env_info = {}):
        '''Env_start'''

    @abstractmethod
    def env_step(self,action):
        '''Env_step'''

    @abstractmethod
    def env_cleanup(self):
        '''Env_cleanup'''

    @abstractmethod
    def env_message(message):
        '''Env_message'''