#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 18:11:41 2017

@author: tymarking
"""
import phenotype, fitnessFunctions, selectionFunctions, crossoverFunctions, mutators
import pylab

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


def evolve(popSize, generations, Phenotype, fitnessF, selectionF, standardDiv, crossoverF, mutateF, muteProb):
    #origin pop
    pop = []
    valAtPop = []
    for i in range(popSize):
        pop.append(Phenotype.getRandomPhenotype())
#        pop.append(phenotype.KnapsackPhenotype([0,1,1,1,1]))
#        pop.append(phenotype.KnapsackPhenotype([0,1,1,1,0]))
#        pop.append(phenotype.KnapsackPhenotype([0,0,1,0,0]))
#        pop.append(phenotype.KnapsackPhenotype([1,1,1,1,1]))
        
    #print(pop)
    #print("Hello")
    
    popWValue = fitnessF(pop)
    
    #for pheno in popWValue:
        #print(str(pheno[1]) + " : " + str(pheno[0].itemsIn))
    
    #loop
    for g in range(generations):
        #evaluate fitness
        popWValue = fitnessF(pop)
        #selection
        valAtPop.append(popWValue[0][1])
        parents = selectionF(popWValue, standardDiv)
        #crossover
        children = crossoverF(parents, popSize)
        #mutate
        children = mutateF(children, muteProb)
        
        pop = children
        #if (g%25 == 24):
            #print("Generation "+str(g+1)+" completed")
        
        
        
    popWValue = fitnessF(pop)
    valAtPop.append(popWValue[0][1])
    #for pheno in popWValue:
        #print(str(pheno[1]) + " : " + str(pheno[0].itemsIn))
    
    #print(popWValue[0][1])
    #print(str(popWValue[0][1]) + " : " + str(popWValue[0][0].itemsIn))
    return valAtPop
#evolve(1000, 1000, phenotype.KnapsackPhenotype, fitnessFunctions.knapsackFitness, selectionFunctions.gradiant25, crossoverFunctions.triCross, mutators.probMutate, 0.10 )

#mutates = [.001, .005, .01, .02, .03, .04, .05, .06, .07, .08, .09, .10, .11, .12, .13, .14, .15, .16, .17, .18, .19, .2]
#selectors = [selectionFunctions.top6, selectionFunctions.top6th, selectionFunctions.gradiant25]
standardDivs = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
vals = []
gens = [100,200,300,400,500,600,700,800,900,1000]
counter = 0
"""for gen in gens:
    testVals = []
    for i in range(10):
        testVals.append(evolve(1000, gen, phenotype.KnapsackPhenotype, fitnessFunctions.knapsackFitness, selectionFunctions.gradiant25, 400, crossoverFunctions.triCross, mutators.probMutate, 0.17 ))
        counter += 1
        print(str(counter) +"% done")
    vals.append(sum(testVals)/len(testVals))
    print("Gen " + str(gen) + " Complete")
    """
vals = []
mins = []
maxes = []
for i in range(100):
    vals.append(evolve(500, 500, phenotype.KnapsackPhenotype, fitnessFunctions.knapsackFitness, selectionFunctions.carryWithGradiant25, 400, crossoverFunctions.triCross, mutators.probMutate, 0.17 ))
for i in range(len(vals[0])):
    mins.append(vals[0][i])
    maxes.append(vals[0][i])

avgVals = []
for i in range(len(vals[0])):
    sumVal = 0
    for val in vals:
        sumVal += val[i]
        if val[i] < mins[i]:
            mins[i] = val[i]
        if val[i] > maxes[i]:
            maxes[i] = val[i]
    avgVals.append(sumVal/len(vals))
    

pylab.plot(range(len(avgVals)), mins, '-r', label = "Min Value")
pylab.plot(range(len(avgVals)), maxes, '-g', label = "Max Value")
pylab.plot(range(len(avgVals)), avgVals, '-b', label = "Average Value")
pylab.legend(loc='lower right')
pylab.title("Knapsack Problem: 500 phenotypes")
pylab.xlabel("Generation")
pylab.ylabel("Value")
pylab.show()
