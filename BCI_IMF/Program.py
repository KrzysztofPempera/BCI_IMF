import board as br
import live_plot as lp
import time
import matplotlib.pyplot as plt
import numpy as np
from classifiers import classic_CCA
from Settings import Config 
from ReferenceSignal import ReferenceSignal as rs
from multiprocessing import Process, Queue, Event
import DataService as ds
import csv
import screen as sc

#def main():


#    while True:
#        time.sleep(1)

#        try:
#            print(classifier.process())

#        except ValueError:
#            a_board.stop_streaming()

#    a_board.stop_streaming()

def drawScreen(start_program):
    activeScreen = sc.screen()
    activeScreen.run(start_program)


#def gatherData(dataService, dataList, activeBoard):
#    dataService.get_data(dataList, activeBoard)

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
        label = ['rPearson', 'stimuli']
        theWriter = csv.DictWriter(csvfile, fieldnames = label)
        for i in range(len(dataClassifier[0])):
            theWriter.writerow({'rPearson':dataClassifier[0][i],'stimuli':dataClassifier[1][i]})

if __name__ == "__main__":

    settings = Config()

    activeBoard = br.Board(settings)

    activeBoard.start_streaming()

    data = [[] for i in range(6)]
    dataClassifier = [[] for i in range(2)]

    start_program = Event() 
    
    #refSignalGen = rs(settings)

    #refSignal = refSignalGen.createReferenceSignals() 

    classifier = classic_CCA(1, 5, activeBoard)

    times = 0

    screenDisplay = Process(target = drawScreen, args = (start_program,))
    screenDisplay.start()

    while True: 
        if start_program.is_set():
            times += 1
        
        
            result = classifier.process(data)

            dataClassifier[0].append(result[0])
            dataClassifier[1].append(result[1])
            print(result)

            time.sleep(1)

            if times == 91:
                screenDisplay.terminate()
                screenDisplay.join()
                break

    extract_data(data)
    extract_data_classifier(dataClassifier)
    activeBoard.stop_streaming()





    #plot = lp.LivePlot(8,a_board)
    #plot.run()
