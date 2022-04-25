# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 11:22:40 2022

@author: kia
"""


import math 

def distance(a,b):
    """
    Finds the euclidean distance between two 2-D agents using pythagoras theorem. 

    Parameters
    ----------
    Two agents with x and y parameters

    Returns
    -------
    Float distance between the points

    """
    return ((a.x-b.x)**2+(a.y-b.y)**2)**0.5

## Testing 'distance' function
## IMPORTANT: To use this test please first comment out line 8 (import myfunctions) from agentframework.py
# =============================================================================
# import agentframework
# test_coord=[[0,0],[4,3]] # Using pythagoras' theorem the distance between these points is 5
# test_agents=[]
# for i in range(0,len(test_coord)):
#      test_agents.append(agentframework.Agent(len(test_agents),test_coord[i][0], test_coord[i][1],[],[],[],[]))
# print("Distnace between test points:",distance(test_agents[0],test_agents[1]))
# =============================================================================

def direction(a,b):
    """
    Find the angle of direction between two agents in radians starting from zero at North and rotating clockwise.
    ----------
    Two agents with x and y parameters

    Returns
    -------
    direction 

    """
    dy=b.y-a.y
    dx=b.x-a.x
    if dx==0:
        direction=math.pi/2
    else:
        direction=math.atan(dy/dx)
        
    if dx<0 and dy>0:
        direction+=math.pi
    elif dx<=0 and dy<=0:
        direction+=math.pi
    elif dx>0 and dy<0:
        direction+=2*math.pi
        
    return direction


        
# Testing direction function
# IMPORTANT: To use this test please first comment out line 8 (import myfunctions) from agentframework.py
# =============================================================================
# import agentframework
# import matplotlib.pyplot as plt
# 
# 
# test_coord=[[0,0],[3,0],[2,2],[0,3],[-2,2],[-3,0],[-2,-2],[0,-3],[2,-2]]
# test_agents=[]
# plt.xlim(-5, 5)
# plt.ylim(-5, 5)
# 
# for i in range(0,len(test_coord)):
#     test_agents.append(agentframework.Agent(len(test_agents),test_coord[i][0], test_coord[i][1],[],[],[],[]))
#     plt.scatter(test_agents[i].x,test_agents[i].y)
# 
# plt.show()
# 
# for i in range(1,len(test_coord)):
#     print("Direction: ",direction(test_agents[0],test_agents[i])/math.pi,"pi")
# =============================================================================


def constrain(agent):
    """
    This function takes coordinates outside the field boundaries and places them back in the field.

    Parameters
    ----------
    agent : Agent to constrain.

    Returns
    -------
    agent.x : constrained x coord.
    
    agent.y : constrained y coord.

    """
    
    if agent.x>=255:
        agent.x=254
    if agent.x<=0:
        agent.x=1
        
    if agent.y>=255:
        agent.y=254
    if agent.y<=0:
        agent.y=1
        
    return agent.x, agent.y


## Testing for constrain function
## IMPORTANT: To use this test please first comment out line 8 (import myfunctions) from agentframework.py
# =============================================================================
# import agentframework
# test_coord=[[-1,-1],[256,256]]
# test_agents=[]
# for i in range(0,len(test_coord)):
#      test_agents.append(agentframework.Agent(len(test_agents),test_coord[i][0], test_coord[i][1],[],[],[],[]))
# for i in [0,1]:
#     print(constrain(test_agents[i]))
# =============================================================================

     
