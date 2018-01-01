#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 18:11:41 2017

@author: tymarking
"""
import phenotype, fitnessFunctions, selectionFunctions, crossoverFunctions

def evolve(popSize, generations, Phenotype, fitnessF, selectionF, crossoverF, mutateF):
    #origin pop
    pop = []
    for i in range(popSize):
        pop.append(Phenotype.getRandomPhenotype)
        
    print(pop)

#loop

#chek for completion

#evaluate fitness

#selection

#crossover

#mutate
    
evolve(10, 1, phenotype.KnapsackPhenotype, fitnessFunctions.knapsackFitness, selectionFunctions.top6, crossoverFunctions.triCross, 1)