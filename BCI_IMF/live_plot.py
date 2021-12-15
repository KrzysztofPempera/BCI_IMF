import random
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

class LivePlot():
    def __init__(self, channels, board):
        self.channels = channels
        self.figure = plt.figure() 
        self.axs = []
        self.lines = []
        self.board = board
        self.y_data = [[] for i in range(self.channels)]
        self.figure.set_figwidth(14)
        self.figure.set_figheight(10)
        plt.style.use('fivethirtyeight')
        plt.tight_layout()

        for i in range(channels):
            self.axs.append(self.figure.add_subplot(self.channels,1,(i+1)))
        

    def run(self):

        x = np.linspace(0,125,self.board.sampling_rate)

        for i in range(self.channels):
            line, = self.axs[i].plot(x, np.random.rand(self.board.sampling_rate))
            self.lines.append(line)

            self.axs[i].set_xlim(0,125)
            self.axs[i].set_ylim(-20000,20000)

        self.figure.show()
        
        while True:
            try:
                data = self.board.get_streaming_data()
                for i in range(len(self.lines)):
                    self.lines[i].set_ydata(data[i])
                self.figure.canvas.draw()
                self.figure.canvas.flush_events()
            except ValueError:
                self.board.stop_streaming()