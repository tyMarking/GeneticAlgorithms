#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 18:12:26 2017

@author: tymarking
"""
import random

globalItems = [(4,12),(2,2),(2,1),(1,1),(10,4),(10000,1)]

class KnapsackPhenotype(object):
    
    itemsIn = [0]*len(globalItems)
    weight = 0
    value = 0
    
    def __init__(self, items):
        self.itemsIn = items
        self.weight = 0
        self.value = 0
        for i in range(5):
            if self.itemsIn[i] == 1:
                self.weight += globalItems[i][1]
                self.value += globalItems[i][0]
        
    @classmethod
    def getRandomPhenotype(cls):
        newItems = []
        for i in range(len(globalItems)):
            newItems.append(random.randint(0,1))
        return KnapsackPhenotype(newItems)