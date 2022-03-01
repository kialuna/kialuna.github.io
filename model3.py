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
#from matplotlib.image import BboxImage
#from matplotlib.transforms import Bbox, TransformedBbox

#random.seed(1)
strt_tm=time.process_time()

#sheep = plt.imread('sheep.jpg')

# Create figure
#fig = plt.figure()
#ax = fig.add_subplot(111)

# =============================================================================
# def plotImage(xData, yData, im, en): #CITATION: https://stackoverflow.com/questions/25329583/matplotlib-using-image-for-points-on-plot
#     #ax.imshow(en)
#     
#     for x, y in zip(xData, yData):
#         bb = Bbox.from_bounds(x,y,10,15)  
#         bb2 = TransformedBbox(bb,ax.transData)
#         bbox_image = BboxImage(bb2,
#                             norm = None,
#                             origin=None,
#                             clip_on=False)
# 
#         bbox_image.set_data(im)
#         ax.add_artist(bbox_image)
#     plt.show()  
# =============================================================================
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
num_it=3
#dists=[]
speed=3
neighbourhood=20

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
    agents.append(agentframework.Agent(i,environment,agents))
    
# Move the agents around and eat grass   
for j in range(0,num_it,1):
    #fig = plt.figure()
    #ax = fig.add_subplot(111)
    #ax.imshow(environment)
    x=[]
    y=[]
    #ax.set_xlim(0, 260)
    #ax.set_ylim(0, 260)        
    for i in range(num_agents):
        agents[i].move(speed)
        x.append(agents[i].getx())
        y.append(agents[i].gety())        
        agents[i].eat()
    share=[0]*num_agents
    for i in range(num_agents):
        store1=agents[i].share_with_neighbours(neighbourhood)
        share=np.add(share,store1)
    print(share)
        

    #plotImage(x, y, sheep, environment)
    #plt.show()        
#For each iteration, plot the agents in the environment         

    plt.xlim(0, 255)
    plt.ylim(0, 255)
    plt.imshow(environment)
    for i in range(num_agents):
        plt.scatter(agents[i].getx(),agents[i].gety())
    plt.show()
    




# Calculate distances between all agents 

# =============================================================================
# for i in range(len(agents)):
#     agent_a = agents[i]
#     for j in range(i+1,len(agents)):
#             agent_b = agents[j]
#             if i<j:
#                 dists.append(pyth_dist(agent_a, agent_b))
#                 
# #print(dists)
# =============================================================================

end_tm=time.process_time()
# 
print("Run time="+str(end_tm-strt_tm))

#for i in range(len(agents)):

f=open('environment.csv','w',newline='')
writer=csv.writer(f,delimiter=',')
for row in environment:
    writer.writerow(row)
f.close()



for i in range(num_agents):
    print(agents[i])

