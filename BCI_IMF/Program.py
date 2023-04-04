import board as br
import live_plot as lp
import time
import matplotlib.pyplot as plt
import numpy as np
import random as rd
from classifiers import classic_CCA
from Settings import Config 
from ReferenceSignal import ReferenceSignal as rs
from multiprocessing import Process, Value, Event
import csv
import screen as sc


def drawScreen(start_program, quit_program, current_stimuli, last_stimuli, orderList, save_data):
    activeScreen = sc.screen()
    activeScreen.run(start_program, quit_program, current_stimuli, last_stimuli, orderList, save_data)

def calculate_accuracy(data):
    i = 0
    data = data.T
    for row in data:
        if row[1] == row[2]:
            i += 1
    accuracy = (i*100)/data.shape[0]
    return accuracy

def extract_data(dataList, name):
    with open(f'data_{name}.csv', 'w', newline='') as csvfile:
        label = ['channel_1','channel_2','channel_3','channel_4', 'stimuli_displayed']
        theWriter = csv.DictWriter(csvfile, fieldnames = label)
        theWriter.writeheader()
        for i in range(len(dataList[0])):
            theWriter.writerow({'channel_1':dataList[0][i], 'channel_2':dataList[1][i],'channel_3':dataList[2][i],'channel_4':dataList[3][i],'stimuli_displayed':dataList[4][i]})

def extract_data_classifier(dataClassifier, name):
    with open(f'dataClassifier_{name}.csv','w', newline='') as csvfile:
        label = ['rPearson', 'stimuli_predicted','stimuli_displayed']
        theWriter = csv.DictWriter(csvfile, fieldnames = label)
        theWriter.writeheader()
        for i in range(len(dataClassifier[0])):
            if dataClassifier[2][i] != 42:
                theWriter.writerow({'rPearson':dataClassifier[0][i],'stimuli_predicted':dataClassifier[1][i],'stimuli_displayed':dataClassifier[2][i]})

def extract_data_order_list(orderList, name):
    with open(f'dataOrderList_{name}.csv','w', newline='') as csvfile:
        theWriter = csv.writer(csvfile)
        theWriter.writerow(orderList)

def generate_order_list(name):
    order_list = [0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4]
    #order_list = [0,1,2,3,4]
    rd.shuffle(order_list)
    extract_data_order_list(order_list, name)
    order_list.insert(0,42)
    print(order_list)
    return order_list

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

    settings = Config()

    name = "data_krzysztof_5S_test"

    orderList = generate_order_list(name)

    activeBoard = br.Board(settings)

    activeBoard.start_streaming()

    dataClassifier = [[] for i in range(3)]
    boardData = np.array([[],[],[],[],[],[],[],[],[]])
    currentData = np.array([])

    start_program = Event()
    quit_program = Event()
    save_data = Event()
    current_stimuli = Value('d',42)
    last_stimuli = Value('d', 42)
    
    classifier = classic_CCA(1, 5, activeBoard)

    first = True


    screenDisplay = Process(target = drawScreen, args = (start_program, quit_program, current_stimuli, last_stimuli, orderList, save_data, ))
    screenDisplay.start()

    temp = 0

    while True: 
        if start_program.is_set():
            if first:
                dataDump = activeBoard.active_board.get_board_data()
                time.sleep(5.5)
                first = False
            
            if save_data.is_set():
                save_data.clear()
                currentData = activeBoard.get_streaming_data(30)
                appendedData = append_displayed_stimuli(currentData, current_stimuli.value)
                print(current_stimuli.value, appendedData.shape)
                boardData = append_data_list(boardData, appendedData)
                
            temp += 1
            result = classifier.process()

            dataClassifier[0].append(result[0])
            dataClassifier[1].append(result[1])
            dataClassifier[2].append(current_stimuli.value)
            if (result[1] == str(currentStimuli)):
                nAccuracy += 1



            if quit_program.is_set():
                screenDisplay.terminate()
                screenDisplay.join()
                break

    extract_data(boardData,name)
    print(boardData.shape)
    extract_data_classifier(dataClassifier,name)
    activeBoard.stop_streaming()

    accuracy = (nAccuracy*100)/len(dataClassifier[1])
    print(accuracy)
