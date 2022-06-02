import csv
import time


class DataService():
    def __init__(self, activeBoard):
        self.activeBoard = activeBoard
    
    

    def get_data(self, dataList, quit_program):

        self.activeBoard.start_streaming()
        time.sleep(2)
        print('streaming started')
        
        while not quit_program.is_set():

            data = self.activeBoard.get_streaming_data(1)
            print(data)

            for i in range(len(dataList)):
                dataList[i].put(data[i])
            time.sleep(1)

