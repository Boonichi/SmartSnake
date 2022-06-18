from __future__ import print_function

from Environment import BaseEnv

import numpy as np

class SnakeEnv(BaseEnv):
    def __init__(self):
        pass
    def env_init(self):
        ''''''
    def env_start(self,env_config):
        ''''''
    def env_step(self,reward,state):
        ''''''
    def env_end(self,state):
        ''''''
    def env_message(message):
        if message == 'get_sum_reward':
            return sum_reward
        else: raise Exception('UnexpectedIssue')