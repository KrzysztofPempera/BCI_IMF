import live_plot as lp
import time
import numpy as np
import random as rd
from classifiers import classic_CCA
from Settings import Config 
from ReferenceSignal import ReferenceSignal as rs
import csv

def import_data():
    data = np.loadtxt(open("data_data_krzysztof_5S_test.csv", "rb"), delimiter=',', skiprows=1)
    return data.T

def calculate_accuracy(data):
    i = 0
    data = data.T
    for row in data:
        if row[1] == row[2]:
            i += 1
    accuracy = (i*100)/data.shape[0]
    return accuracy


def extract_data_classifier(dataClassifier, name, accuracy):
    with open(f'dataClassifier_{name}.csv','w', newline='') as csvfile:
        label = ['rPearson', 'stimuli_predicted','stimuli_displayed']
        theWriter = csv.DictWriter(csvfile, fieldnames = label)
        theWriter.writeheader()
        for i in range(len(dataClassifier[0])):
            if dataClassifier[2][i] != 42:
                theWriter.writerow({'rPearson':dataClassifier[0][i],'stimuli_predicted':dataClassifier[1][i],'stimuli_displayed':dataClassifier[2][i]})
        theWriter.writerow({'rPearson':accuracy})

def extract_data_order_list(orderList, name):
    with open(f'dataOrderList_{name}.csv','w', newline='') as csvfile:
        theWriter = csv.writer(csvfile)
        theWriter.writerow(orderList)


def append_displayed_stimuli(data, stimuli):
    y = data.shape[1]
    stimuliList = np.array([stimuli]*y)
    print(len(stimuliList))
    appendedList = np.vstack((data, stimuliList))
    return appendedList

def append_data_list(data, currentData):
    newData = []
    for i in range (currentData.shape[0]):
        dataTemp = np.append(data[i],currentData[i])
        newData.append(dataTemp)

    newData = np.array(newData)
    return newData

if __name__ == "__main__":

 
    name = "R1_50"

    data = import_data()

    dataClassifier = [[] for i in range(3)]
    classifier = classic_CCA(1, 1)

    maxIt = data.shape[1]-200

    nAccuracy = 0

    for i in range(0, maxIt, 50):
        dataArray = []
        for array in data:
            dataArray.append(array[i:200+i])
        dataArray = np.array(dataArray)
        currentStimuli = dataArray[4][1]
        dataArray = dataArray[:-1]

        result = classifier.process(dataArray)
        dataClassifier[0].append(result[0])
        dataClassifier[1].append(result[1])
        dataClassifier[2].append(currentStimuli)

        if (result[1] == str(currentStimuli)):
            nAccuracy += 1

        print(i)

    accuracy = (nAccuracy*100)/len(dataClassifier[1])
    print(accuracy)
    extract_data_classifier(dataClassifier, name, accuracy)


