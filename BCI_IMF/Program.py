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


def drawScreen(start_program, quit_program, current_stimuli, orderList):
    activeScreen = sc.screen()
    activeScreen.run(start_program, quit_program, current_stimuli, orderList)

def extract_data(dataList, name):
    with open(f'data_{name}.csv', 'w', newline='') as csvfile:
        label = ['channel_1','channel_2','channel_3','channel_4','channel_5','channel_6','channel_7','channel_8']
        theWriter = csv.DictWriter(csvfile, fieldnames = label)
        theWriter.writeheader()
        for i in range(len(dataList[0])):
            theWriter.writerow({'channel_1':dataList[0][i], 'channel_2':dataList[1][i],'channel_3':dataList[2][i],'channel_4':dataList[3][i],'channel_5':dataList[4][i],'channel_6':dataList[5][i]})

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
    rd.shuffle(order_list)
    extract_data_order_list(order_list, name)
    return [1,2]


if __name__ == "__main__":

    settings = Config()

    name = "test2"

    orderList = generate_order_list(name)

    activeBoard = br.Board(settings)

    activeBoard.start_streaming()

    data = [[] for i in range(6)]
    dataClassifier = [[] for i in range(3)]

    start_program = Event()
    quit_program = Event()
    current_stimuli = Value('d',0.0)
    
    classifier = classic_CCA(1, 5, activeBoard)

    first = True


    screenDisplay = Process(target = drawScreen, args = (start_program, quit_program, current_stimuli, orderList))
    screenDisplay.start()

    temp = 0

    while True: 
        if start_program.is_set():
            if first:
                dataDump = activeBoard.active_board.get_board_data()
                time.sleep(5.5)
                first = False
        
            temp += 1
            result = classifier.process()

            dataClassifier[0].append(result[0])
            dataClassifier[1].append(result[1])
            dataClassifier[2].append(current_stimuli.value)
            print(result, current_stimuli.value)


            if quit_program.is_set():
                screenDisplay.terminate()
                screenDisplay.join()
                break

    dataTest= activeBoard.active_board.get_board_data()[1:7,:]
    extract_data(dataTest,name)
    extract_data_classifier(dataClassifier,name)
    activeBoard.stop_streaming()
    print(temp)
