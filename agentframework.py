# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 16:16:11 2022

@author: kia
"""
import random 

class Agent: 
    

    def __init__(self,ia):
        self._id=ia
        self._x=random.randint(0,99)
        self._y=random.randint(0,99)
        
    def __str__(self):
        return "id="+str(self._id)+", x="+str(self._x)+", y="+str(self._y)
    
    def move_coord(self,coord,n):
        if random.random()<0.33:
            return coord
        if random.random()<0.5:
            coord=(coord+random.randint(0,n))%100
        else:
            coord=(coord-random.randint(0,n))%100
            
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
    