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
import numpy as np
import matplotlib.animation

# Start random seed and process timer 
random.seed(1)
strt_tm=time.process_time()

# Create a figure
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
#ax.set_autoscale_on(False)

    

agents=[]
num_agents=10
num_it=20
speed=3
neighbourhood=50

# Creating DEM environment from txt file 
reader = csv.reader(open('DEM.txt',newline=''),quoting=csv.QUOTE_NONNUMERIC)
environment=[]
for row in reader:
    rowlist=[]
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)


# Test case
test_coord=[[20,30],[50,40],[150,200],[40,240],[200,100],[250,200]]


test='N'

# Make the agents - each linked to an id number and the environment
if test=='Y':
    for i in range(0,len(test_coord)):
        agents.append(agentframework.Agent(len(agents),test_coord[i][0], test_coord[i][1],environment,agents))
        print(agents[i])
else:   
    for i in range(num_agents):
        x=random.randint(0,255)
        y=random.randint(0,255)
        agents.append(agentframework.Agent(len(agents),x, y,environment,agents))
num_agents = len(agents)


def update(frame_number):
    
    fig.clear()
    # Move the agents around and eat grass   

    x=[]
    y=[]      
    for i in range(num_agents):
        agents[i].move(speed)
        x.append(agents[i].getx())
        y.append(agents[i].gety())        
        agents[i].eat()
        
# Perform sharing
    share=[0]*num_agents # Blank list to add in the share of each agent going to other agents
    for i in range(num_agents):
        test = agents[i].share_with_neighbours(neighbourhood)
        #print(test)
        share=np.add(share,test)
        #print(share)
    for i in range(num_agents):
        agents[i].store=share[i]
    #print(share)
    
    plt.xlim(0, 255)
    plt.ylim(0, 255)
    plt.imshow(environment)
    
    for i in range(num_agents):
        plt.scatter(agents[i].getx(),agents[i].gety())
        print(agents[i])
        #print(agents[i][0],agents[i][1])
        
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_it)
plt.show()       
# =============================================================================
# # Plot position of agents   
#     plt.xlim(0, 255)
#     plt.ylim(0, 255)
#     plt.imshow(environment)
#     for i in range(num_agents):
#         plt.scatter(agents[i].getx(),agents[i].gety())
#     plt.show()
# =============================================================================
    
    
# Display run time
end_tm=time.process_time()
print("Run time="+str(end_tm-strt_tm))


f=open('environment.csv','w',newline='')
writer=csv.writer(f,delimiter=',')
for row in environment:
    writer.writerow(row)
f.close()



for i in range(num_agents):
    print(agents[i])

