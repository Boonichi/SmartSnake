from __future__ import print_function

from abc import ABCMeta, abstractmethod

class BaseSnake:

    __metaclass__ = ABCMeta
    def __int__(self):
        pass

    @abstractmethod
    def agent_init(self, agent_info = {}):
        '''Agent_init'''

    @abstractmethod
    def agent_start(self, observation):
        '''Agent_start'''
    
    @abstractmethod
    def agent_step(self, reward, observation):
        '''Agent_step'''

    @abstractmethod
    def agent_end(self, reward):
        '''Agent_end'''

    @abstractmethod
    def agent_cleanup(self):
        '''Agent_cleanup'''

    @abstractmethod
    def agent_message(self):
        '''Agent_message'''
    
    