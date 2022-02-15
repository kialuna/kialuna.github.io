# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 16:42:12 2022

@author: kia
"""
import random
import matplotlib.pyplot as plt
import csv
import time
import agentframework

random.seed(0)
strt_tm=time.process_time()

def pyth_dist(agent_a,agent_b):
    """
    Calculates the distance between two x,y coordinates.

    Parameters
    ----------
    agent_a, agent_b : Two x,y coordiantes.


    Returns
    -------
    Distance.

    """
    return(((agent_a.getx()-agent_b.getx())**2+(agent_a.gety()-agent_b.gety())**2)**0.5)
    

agents=[]
num_agents=10
num_it=10
dists=[]
speed=3

# Creating DEM environment from txt file 
reader = csv.reader(open('DEM.txt',newline=''),quoting=csv.QUOTE_NONNUMERIC)
environment=[]
for row in reader:
    rowlist=[]
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)


# Make the agents - each linked to an id number and the environment
for i in range(num_agents):
    agents.append(agentframework.Agent(i,environment))
    
# Move the agents around and eat grass   
for j in range(0,num_it,1):
    for i in range(num_agents):
        agents[i].move(speed)
        agents[i].eat()
        
# For each iteration, plot the agents in the environment         
    plt.xlim(0, 255)
    plt.ylim(0, 255)
    plt.imshow(environment)
    for i in range(num_agents):
        plt.scatter(agents[i].getx(),agents[i].gety())
    plt.show()
    

# Calculate distances between all agents 

for i in range(len(agents)):
    agent_a = agents[i]
    for j in range(i+1,len(agents)):
            agent_b = agents[j]
            if i<j:
                dists.append(pyth_dist(agent_a, agent_b))
                
#print(dists)

end_tm=time.process_time()
# 
print("Run time="+str(end_tm-strt_tm))

# =============================================================================
# for i in range(num_agents):
#     print(agents[i])
# =============================================================================
