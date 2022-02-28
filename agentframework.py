# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 16:16:11 2022

@author: kia
"""
import random 

class Agent: 
    

    def __init__(self,ia,environment):
        self.environment=environment
        self.store=0
        self._id=ia
        self._x=random.randint(0,255)
        self._y=random.randint(0,255)
        
    def __str__(self):
        return "id="+str(self._id)+", x="+str(self._x)+", y="+str(self._y)+", store="+str(self.store)
    
    def eat(self): # eating values off DEM 10 at a time
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10
        else:  # If remaining is less than 10, sheep eats all of what is left
            self.store+=self.environment[self._y][self._x]
            self.environment[self._y][self._x]=0
            
            
            
            
    
    def move_coord(self,coord,n):
        if random.random()<0.33:
            return coord
        if random.random()<0.5:
            coord=(coord+random.randint(0,n))%250
        else:
            coord=(coord-random.randint(0,n))%250
            
        return coord
    
    def move(self,n):
        """
        Moves x and y coordinates randomly by n step

        """
        self._x=self.move_coord(self._x,n)
        self._y=self.move_coord(self._y,n)
        
        
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
    