# mdp.py
# ------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import random

class MarkovDecisionProcess:
    '''
    MarkovDecisionProcess class: get the state s/s', action, R(s,a,s'), T(s,a,s') and check whether terminal
    '''

    def getStates(self):# return all states in MDP
        """
        Return a list of all states in the MDP.
        Not generally possible for large MDPs.
        """
        abstract

    def getStartState(self): # get start state
        """
        Return the start state of the MDP.
        """
        abstract

    def getPossibleActions(self, state): # get all the action a that agent can take from state s
        """
        Return list of possible actions from 'state'.
        """
        abstract

    def getTransitionStatesAndProbs(self, state, action): # get all the possible T and s' with current state s and action a
        """
        Returns list of (nextState, prob) pairs
        representing the states reachable
        from 'state' by taking 'action' along
        with their transition probabilities.

        Note that in Q-Learning and reinforcment
        learning in general, we do not know these
        probabilities nor do we directly model them.
        """
        abstract

    def getReward(self, state, action, nextState): # get reward R(s,a,s') with current s,a,s'
        """
        Get the reward for the state, action, nextState transition.

        Not available in reinforcement learning.
        """
        abstract

    def isTerminal(self, state): # check whether terminal, normally return with R=0 and no action a. Or action a = 'pass' with R=0
        """
        Returns true if the current state is a terminal state.  By convention,
        a terminal state has zero future rewards.  Sometimes the terminal state(s)
        may have no possible actions.  It is also common to think of the terminal
        state as having a self-loop action 'pass' with zero reward; the formulations
        are equivalent.
        """
        abstract
