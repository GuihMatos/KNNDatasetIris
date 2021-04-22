# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 09:29:56 2021

@author: Guilherme Matos
"""

import csv
import math
import random
import operator

with open("C:\\Users\\Comp\\Documents\\GUILHERME\\INTELIGENCIA_ARTIFICIAL\\iris.data", "rt") as csvfile:
    lines = csv.reader(csvfile)
    for row in lines:
        print(', '.join(row))
        
def loadDataset(filename, split, trainingSet=[], testSet=[]):
    with open(filename, 'rt') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset) - 1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])
                
                
trainingSet = []
testSet = []
loadDataset('iris.data', 0.66, trainingSet, testSet)
print('Train: ' + repr(len(trainingSet)))
print('Test: ' + repr(len(testSet)))

def euclidianDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
        return math.sqrt(distance)

data1 = [2, 2, 2, 2,'a']
data2 = [4, 5, 4, 5, 'b']
distance = euclidianDistance(data1, data2, 3)
print('Distance: ' + repr(distance))

def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance) - 1
    for x in range(len(trainingSet)):
        dist = euclidianDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
        
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors

trainSet = [[2,2,2,2, 'a'], [4,5,4,5, 'b']]
testInstance = [5,5,5]
k = 1
neighbors = getNeighbors(trainSet, testInstance, k)
print(neighbors)

def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]

neighbors = [[1,1,1, 'a'], [2,2,2, 'a'], [3,3,3, 'b']]
response = getResponse(neighbors)
print(response)

def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
            
    return (correct/float(len(testSet))) * 100.0

testSet = [[1,1,1, 'a'], [2,2,2, 'a'], [3,3,3, 'a']]
predictions = ['a', 'a', 'a']
accuracy = getAccuracy(testSet, predictions)
print(accuracy)

def main():
    #preparo de dados
    trainingSet=[]
    testSet=[]
    split=0.66
    loadDataset('iris.data', split, trainingSet, testSet)
    print('TrainSet: ' + repr(len(trainingSet)))
    print('TrainSet: ' + repr(len(testSet)))
    
    # classificação
    predictions = []
    k = 3
    for x in range(len(testSet)):
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        result = getResponse(neighbors)
        predictons.append(result)
        print('> predicted=' + repr(result) + ', actual=' + repr(tesSet[x][-1]))
        accuracy = getAccuracy(testSet, predictions)
        print('Accuracy: ' + repr(accuracy) + '% ')
