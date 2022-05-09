import board as br
import live_plot as lp
import time
import matplotlib.pyplot as plt
import numpy as np
from classifiers import classic_CCA
from Settings import Config

def main():

    ref_signal = [2 * np.pi * 10, 2 * np.pi * 10 + 0.5*np.pi, 2 * np.pi * 10 + 1*np.pi]

    a_board = br.Board(0,'COM3') 

    a_board.start_streaming()


    #plot = lp.LivePlot(8,a_board)

    #plot.run()

    classifier = classic_CCA(1, a_board, ref_signal)

    while True:
        time.sleep(1)

        try:
            print(classifier.process())

        except ValueError:
            a_board.stop_streaming()

    a_board.stop_streaming()



if __name__ == "__main__":
    main()