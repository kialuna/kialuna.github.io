# -*- coding: utf-8 -*-
"""
Assignment 1. 

The wolf's framework. 

Student no: 201578549
    
"""

#import random
import myfunctions
import math


class wolf: 
    

    def __init__(self,x, y,environment,agents):
        self.environment=environment
        #self.store=0
        self.x=x
        self.y=y
        self.agents=agents


        
    def __str__(self):
        return "WOLF! x="+str(self.x)+", y="+str(self.y)
    
    def hunt(self,speed):
        """
        This function finds the closest sheep to the wolf, labels the sheep as
        "hunted", chases the sheep and kills the sheep if it's within 6 cells distance.

        Parameters
        ----------
        speed : Speed of the wolf 

        """
        
        dists=[]  # Blank list to store the distance to all the sheep in 
        for agent in self.agents:
            # Add distance to each sheep to 'dists'
            dists.append(myfunctions.distance(self,agent))   
            # Set "Hunted" sheep back to "Alive" just in case there's a closer sheep which the wolf can hunt
            if agent.status=="Hunted":                
                agent.status="Alive"
        # Find index of closest sheep and set it's status as "hunted"
        prey_index=dists.index(min(dists))  
        self.agents[prey_index].status="Hunted"                # Sets sheep's status to "hunted" 
        prey_distance=dists[prey_index]
        # If prey is within 6 cells distance, the wolf moves to catch it, and it's status is set to "Dead"
        if prey_distance<6:
            self.agents[prey_index].status="Dead" 
            self.x=self.agents[prey_index].x
            self.y=self.agents[prey_index].y         
            
        # Otherwise, wolf moves in the direction of the prey using speed
        else:
            direction=myfunctions.direction(self,self.agents[prey_index])        
            self.x+=round(math.cos(direction)*speed)
            self.y+=round(math.sin(direction)*speed)
            self.x,self.y=myfunctions.constrain(self)
            
