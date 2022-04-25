# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 16:16:11 2022

@author: kia
"""
import random 
import myfunctions
import math

class Agent: 
    
    # Initialise agent with starting parameters
    def __init__(self,ia,x, y,environment,agents,grass,wolf):
        self.environment=environment
        self.store=0
        self.id=ia
        self.x=x
        self.y=y
        self.agents=agents
        self.grass=grass
        self.status="Alive"
        self.wolf=wolf

        
    def __str__(self):
        return "id="+str(self.id)+", x="+str(self.x)+", y="+str(self.y)+", store="+str(self.store)+", Status="+str(self.status)
    
    
    # Eat grass
    def eat(self):
        # Eat random amount between 0 and 10
        portion=random.randint(0,10) 
        # If the portion chosen to eat is greater than the amount of grass left, they just eat the remaining grass
        if portion > self.grass[self.y][self.x]: 
            self.grass[self.y][self.x] = 0
            self.store += self.grass[self.y][self.x]
        else: 
            self.grass[self.y][self.x] -= portion
            self.store += portion
        #If they eat too much, they sick it all up    
        if self.store>100: 
            self.store=0
            
            
            
            
    # Move randomly by some amount less than 'speed'
    def rand_move(self,speed):
        # A third of the time they don't move at all 
        if random.random()>0.33:
            self.x+=random.randint(-speed,speed)
            self.y+=random.randint(-speed,speed)
            self.x,self.y=myfunctions.constrain(self)
   
            
    # Running from the wolf 
    def flee_move(self,speed):
        # Find direction of wolf in radians 
        wolf_dir=myfunctions.direction(self,self.wolf)     
        # Find relative amounts of x and y to move by to run away from wolf 
        self.x-= round(math.cos(wolf_dir)*speed)
        self.y-=round(math.sin(wolf_dir)*speed)
        # If out of the fields constrains, gets put back in 
        self.x,self.y=myfunctions.constrain(self)
                
    def move(self,eat_speed,run_speed):
        """
        Chooses whether to move normally or flee from wolf
        
        Parameters: n is the speed of movement for normal move()

        """

        wolf_dist=myfunctions.distance(self,self.wolf)
        # If wolf 50 cells or less distance from agent, agent flees
        if wolf_dist>50:
            self.rand_move(eat_speed)
        else:
            self.flee_move(run_speed)
            
        
        
        
    
    def share_with_neighbours(self, neighbourhood): 
        """
        Function which calculates for a given agent how much to share with 
        every other agent.

        Parameters
        ----------
        neighbourhood : Distance below which agent will share with other agents.

        Returns
        -------
        List of how much to share with each other agent. List shares the same index as agents list, 
        so that first item is amount shared with agent[1] etc. 

        """
    
        nb=[] # Blank neighbours list 
        for agent in self.agents: # For each other agent
            dist = myfunctions.distance(self,agent)  # Calculate distance to said agent          
            if dist <= neighbourhood: #if it's in it's neighbourhood
                nb.append(1) # Add a 1 or 0 list if neighbour or not neighbour 
            else:  
                nb.append(0) 
        portion=self.store/sum(nb) # portion is share of agent's store going to each neighbour and itself
        nb_share=[n*portion for n in nb] # multiply nb list by portion to get list of portion going to each other agent
    
        return(nb_share)
            
        
