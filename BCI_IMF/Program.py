import board as br
import live_plot as lp
import time
import matplotlib.pyplot as plt
import numpy as np
from classifiers import classic_CCA
from Settings import Config 
from ReferenceSignal import ReferenceSignal as rs
from multiprocessing import Process, Value, Event
import DataService as ds
import csv
import screen as sc


def drawScreen(start_program, quit_program, current_stimuli):
    activeScreen = sc.screen()
    activeScreen.run(start_program, quit_program, current_stimuli)


def gatherData(dataService, dataList, activeBoard):
    dataService.get_data(dataList, activeBoard)

def drawHello():
    while True:
        print('hello')

def extract_data(dataList):
    with open('data.csv', 'w', newline='') as csvfile:
        label = ['channel_1','channel_2','channel_3','channel_4','channel_5','channel_6','channel_7','channel_8']
        theWriter = csv.DictWriter(csvfile, fieldnames = label)
        for i in range(len(dataList[0])):
            theWriter.writerow({'channel_1':dataList[0][i], 'channel_2':dataList[1][i],'channel_3':dataList[2][i],'channel_4':dataList[3][i],'channel_5':dataList[4][i],'channel_6':dataList[5][i]})

def extract_data_classifier(dataClassifier):
    with open('dataClassifier.csv','w', newline='') as csvfile:
        label = ['rPearson', 'stimuli_predicted','stimuli']
        theWriter = csv.DictWriter(csvfile, fieldnames = label)
        for i in range(len(dataClassifier[0])):
            theWriter.writerow({'rPearson':dataClassifier[0][i],'stimuli_predicted':dataClassifier[1][i],'stimuli':dataClassifier[2][i]})

if __name__ == "__main__":

    settings = Config()

    activeBoard = br.Board(settings)

    activeBoard.start_streaming()

    data = [[] for i in range(6)]
    dataClassifier = [[] for i in range(3)]

    start_program = Event()
    quit_program = Event()
    current_stimuli = Value('d',0.0)
    
    #refSignalGen = rs(settings)

    #refSignal = refSignalGen.createReferenceSignals() 

    classifier = classic_CCA(1, 5, activeBoard)

    first = True


    screenDisplay = Process(target = drawScreen, args = (start_program, quit_program, current_stimuli,))
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
    extract_data(dataTest)
    extract_data_classifier(dataClassifier)
    activeBoard.stop_streaming()
    print(temp)




    #plot = lp.LivePlot(8,a_board)
    #plot.run()
