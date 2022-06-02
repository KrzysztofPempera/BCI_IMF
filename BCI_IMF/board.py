import brainflow
from brainflow.board_shim import BoardShim, BrainFlowInputParams
from brainflow.data_filter import DataFilter, FilterTypes
import time

class Board():
    def __init__(self, settings):
        
        params = BrainFlowInputParams()
        params.serial_port = settings.boardPort
        self.active_board = BoardShim(settings.boardID, params)
        self.sampling_rate = self.active_board.get_sampling_rate(settings.boardID)
        self.channels = self.active_board.get_eeg_channels(settings.boardID)
        self.channels2 = self.active_board.get_exg_channels(settings.boardID)   


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

    def get_streaming_data(self, timeframe):
        data = self.active_board.get_current_board_data(self.sampling_rate*timeframe)
        data = data[1:9,:]

        return data
        