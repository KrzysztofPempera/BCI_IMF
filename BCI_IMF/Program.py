import board as br
import live_plot as lp
import time
import matplotlib.pyplot as plt
import numpy as np
from classifiers import classic_CCA
from Settings import Config 
from ReferenceSignal import ReferenceSignal as rs
from multiprocessing import Process
from screen import screen

def main():

    while True:
        time.sleep(1)

        try:
            print(classifier.process())

        except ValueError:
            a_board.stop_streaming()

    a_board.stop_streaming()



if __name__ == "__main__":
    settings = Config()

    refSignalGen = rs(settings)

    refSignal = refSignalGen.createReferenceSignals()

    #activeBoard = br.Board(settings)

    #boardStreaming = Process(target = activeBoard.start_streaming)

    activeScreen = screen()

    screenDisplay = Process(target = activeScreen.run())



    #plot = lp.LivePlot(8,a_board)

    #plot.run()

    classifier = classic_CCA(1, activeBoard, refSignal)
    main()