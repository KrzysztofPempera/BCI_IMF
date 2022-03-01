import random
from itertools import count
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

class LivePlot():
    def __init__(self, channels, board):
        self.channels = channels
        mpl.rcParams['toolbar'] = 'None'
        self.figure = plt.figure() 
        self.axs = []
        self.lines = []
        self.board = board
        self.y_data = [[] for i in range(self.channels)]
        self.figure.set_figwidth(14)
        self.figure.set_figheight(10)
        plt.style.use('fivethirtyeight')
        plt.rcParams.update({'font.size': 10})
        plt.subplots_adjust(left=0.07, bottom=0.07,top = 0.99,right = 0.99, wspace=0, hspace=0.1)

        for i in range(channels):
            self.axs.append(self.figure.add_subplot(self.channels,1,(i+1)))
            

    def run(self):

        x = np.linspace(-1,0,self.board.sampling_rate)

        for i in range(self.channels):
            line, = self.axs[i].plot(x, np.random.rand(self.board.sampling_rate), linewidth = 0.5)
            self.lines.append(line)

            #self.axs[i].set_xlim(0,125)
            #self.axs[i].set_ylim(-200,200)
            self.axs[i].set_ylabel('Channel {:}'.format(i+1))

        for i in range (len(self.axs)-1):
            self.axs[i].axes.xaxis.set_ticklabels([])

        self.figure.show()
        
        while True:
            try:
                data = self.board.get_streaming_data(1)
                
                data = self.board.filter_data(data)
                

                for i in range(len(self.lines)):
                    self.lines[i].set_ydata(data[i])
                    self.axs[i].relim()
                    self.axs[i].autoscale_view()
                self.figure.canvas.draw()
                self.figure.canvas.flush_events()
            except ValueError:
                self.board.stop_streaming()