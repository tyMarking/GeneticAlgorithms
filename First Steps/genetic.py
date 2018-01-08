#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 18:11:41 2017

@author: tymarking
"""
import phenotype, fitnessFunctions, selectionFunctions, crossoverFunctions, mutators

def evolve(popSize, generations, Phenotype, fitnessF, selectionF, crossoverF, mutateF, muteProb):
    #origin pop
    pop = []
    for i in range(popSize):
        pop.append(Phenotype.getRandomPhenotype())
#        pop.append(phenotype.KnapsackPhenotype([0,1,1,1,1]))
#        pop.append(phenotype.KnapsackPhenotype([0,1,1,1,0]))
#        pop.append(phenotype.KnapsackPhenotype([0,0,1,0,0]))
#        pop.append(phenotype.KnapsackPhenotype([1,1,1,1,1]))
        
    print(pop)
    print("Hello")
    
    popWValue = fitnessF(pop)
    
    for pheno in popWValue:
        print(str(pheno[1]) + " : " + str(pheno[0].itemsIn))
    
    #loop
    for g in range(generations):
        #evaluate fitness
        popWValue = fitnessF(pop)
        #selection
        parents = selectionF(popWValue)
        #crossover
        children = crossoverF(parents, popSize)
        #mutate
        children = mutateF(children, muteProb)
        
        pop = children
        print("Generation "+str(g+1)+" completed")
        
    popWValue = fitnessF(pop)
    
    for pheno in popWValue:
        print(str(pheno[1]) + " : " + str(pheno[0].itemsIn))
    
    print(popWValue[0][0].value)
evolve(20, 100, phenotype.KnapsackPhenotype, fitnessFunctions.knapsackFitness, selectionFunctions.top6, crossoverFunctions.triCross, mutators.probMutate, 0.05 )