import brainflow
from brainflow.board_shim import BoardShim, BrainFlowInputParams
from brainflow.data_filter import DataFilter, FilterTypes
import time

class Board():
    def __init__(self, board_id, serial_port):
        
        params = BrainFlowInputParams()
        params.serial_port = serial_port
        self.active_board = BoardShim(board_id, params)
        self.sampling_rate = self.active_board.get_sampling_rate(board_id)
        self.channels = self.active_board.get_eeg_channels(board_id)
        self.channels2 = self.active_board.get_exg_channels(board_id)
        self.timeframe = 1


    def start_streaming(self):
        self.active_board.prepare_session()
        self.active_board.start_stream(45000)
        time.sleep(2)

    def stop_streaming(self):
        self.active_board.stop_stream()
        self.active_board.release_session()

    def filter_data(self, data):
        for dat in data:
            DataFilter.perform_bandstop(dat, self.sampling_rate, 50, 2, 2, FilterTypes.BUTTERWORTH.value, 0)
            DataFilter.perform_bandpass(dat, self.sampling_rate, 51, 100, 2, FilterTypes.BUTTERWORTH.value, 0)

        return data

    def get_streaming_data(self):
        data = self.active_board.get_current_board_data(self.sampling_rate*self.timeframe)
        data = data[1:9,:]

        return data
        