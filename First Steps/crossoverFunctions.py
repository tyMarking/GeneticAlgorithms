#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 18:13:14 2017

@author: tymarking
"""
import random
import phenotype

def triCross(parents, popSize):
    children = []
    for i in range(popSize):
        par1 = random.choice(parents)
        par2 = random.choice(parents)
        par1 = random.choice(parents)
        
        newItems = []
        for j in range(len(par1.itemsIn)):
            itemSum = par1.itemsIn[j] + par1.itemsIn[j] + par1.itemsIn[j]
            if itemSum >= 2:
                newItems.append(1)
            else:
                newItems.append(0)
        children.append(phenotype.KnapsackPhenotype(newItems))
        
    return children