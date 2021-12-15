import board as br
import live_plot as lp
import time
import matplotlib.pyplot as plt
import numpy as np

def main():

    a_board = br.Board(2,'COM3') 

    a_board.start_streaming()


    plot = lp.LivePlot(8,a_board)

    plot.run()

    a_board.stop_streaming()


if __name__ == "__main__":
    main()