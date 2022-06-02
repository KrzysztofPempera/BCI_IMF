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
#import screen as sc

#def main():


#    while True:
#        time.sleep(1)

#        try:
#            print(classifier.process())

#        except ValueError:
#            a_board.stop_streaming()

#    a_board.stop_streaming()

#def drawScreen():
#    activeScreen = sc.screen()
#    activeScreen.run()


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
            theWriter.writerow({'channel_1':dataList[0][i], 'channel_2':dataList[1][i],'channel_3':dataList[2][i],'channel_4':dataList[3][i],'channel_5':dataList[4][i],'channel_6':dataList[5][i],'channel_7':dataList[6][i],'channel_8':dataList[7][i]})


if __name__ == "__main__":

    settings = Config()

    activeBoard = br.Board(settings)

    activeBoard.start_streaming()

    data = [[] for i in range(8)]
    
    refSignalGen = rs(settings)

    refSignal = refSignalGen.createReferenceSignals()

    classifier = classic_CCA(1, 1, activeBoard, refSignal)

    times = 0

    while True: 
        
        times += 1
        
        
        print(classifier.process(data))
        time.sleep(1)

        if times == 10:
            break
    extract_data(data)
    activeBoard.stop_streaming()


    #screenDisplay = Process(target = drawScreen)
    #screenDisplay.start()


    #plot = lp.LivePlot(8,a_board)
    #plot.run()

    #classifier = classic_CCA(1, activeBoard, refSignal)