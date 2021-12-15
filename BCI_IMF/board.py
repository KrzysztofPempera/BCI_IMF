import brainflow
from brainflow.board_shim import BoardShim, BrainFlowInputParams

class Board():
    def __init__(self, board_id, serial_port):
        
        params = BrainFlowInputParams()
        params.serial_port = serial_port
        self.active_board = BoardShim(board_id, params)
        self.sampling_rate = BoardShim.get_sampling_rate
        self.channels = 8
        self.timeframe = 5


        def start_stream(self):
            self.active_board.prepare_session()
            self.active_board.start_stream(45000)

        def stop_stream(self):
            self.active_board.stop_stream()
            self.active_board.release_session()

        def get_streaming_data(self):
            data = self.active_board.get_current_board_data(self.sampling_rate * self.timeframe)
            return data