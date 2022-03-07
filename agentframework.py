# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 16:16:11 2022

@author: kia
"""
import random 

class Agent: 
    

    def __init__(self,ia,x, y,environment,agents):
        self.environment=environment
        self.store=0
        self._id=ia
        self._x=x
        self._y=y
        #self._x=random.randint(0,255)
        #self._y=random.randint(0,255)
        self.agents=agents

        
    def __str__(self):
        return "id="+str(self._id)+", x="+str(self._x)+", y="+str(self._y)+", store="+str(self.store)
    
    def eat(self): # eating values off DEM 
        if self.environment[self._y][self._x] > 10:
            portion=random.randint(0,10)
            self.environment[self._y][self._x] -= portion
            self.store += portion
        else:  # If remaining is less than 10, sheep eats all of what is left
            self.store+=self.environment[self._y][self._x]
            self.environment[self._y][self._x]=0
        
            
            
            
            
    
    def move_coord(self,coord,n):
        if random.random()<0.33:
            return coord
        if random.random()<0.5:
            coord=(coord+random.randint(0,n))%255
        else:
            coord=(coord-random.randint(0,n))%255
            
        return coord
    
    def move(self,n):
        """
        Moves x and y coordinates randomly by n step

        """
        
        self._x=self.move_coord(self._x,n)
        self._y=self.move_coord(self._y,n)
        
    
    def share_with_neighbours(self, neighbourhood): #Sharing fairly!
        nb=[] # Blank neighbours list 
        for agent in self.agents: # For each other agent
            dist = self.distance_between(agent)  # Calculate distance to said agent          
            if dist <= neighbourhood: #if it's in it's neighbourhood
                nb.append(1) # Add a 1 to 0 list if neighbour or not neighbour 
            else:  
                nb.append(0) 
        portion=self.store/sum(nb) # portion is share of agent's store going to each neighbour and itself
        nb_share=[n*portion for n in nb] # multiply nb list by portion to get list of portion going to each other agent
    
        return(nb_share)
            
        

    def distance_between(self, agent):
        return (((self.getx() - agent.getx())**2) + ((self.gety() - agent.gety())**2))**0.5 
        
        
        
        
    def getid(self):
        """
        Returns coordinate id.

        """
        return self._id   
    
    def getx(self):
        """
        Returns x coordinate.

        """
        return self._x
    
    def gety(self):
        """
        Returns y coordinate

        """
        return self._y
    