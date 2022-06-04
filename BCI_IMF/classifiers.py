import numpy as np
import sklearn.cross_decomposition as sk
import sys

np.set_printoptions(threshold=sys.maxsize)

class classic_CCA():
    def __init__(self, n_components, timeframe, board, reference_signal = None):
        self.board = board
        self.n_components = n_components
        self.reference_signal = reference_signal
        self.sampling_rate = self.board.sampling_rate
        self.frequecies = ["0", "0.5", "1"]
        self.timeframe = timeframe
        

    def generate_ref_signal(self, reference_signal, lenght):
        time = np.linspace(0, lenght/self.sampling_rate, self.timeframe*self.sampling_rate )
        ref_signal = []
        

        for signal in reference_signal:
            temp_ref_signal = []
            temp_ref_signal.append(np.sin(signal*time))
            temp_ref_signal.append(np.cos(signal*time))
            temp_ref_signal.append(np.sin(signal*2*time))
            temp_ref_signal.append(np.cos(signal*2*time))
            
            ref_signal.append( np.array(temp_ref_signal))
        

        ref_signal = np.array(ref_signal)

        return ref_signal

    def calculate_correlations(self, data, reference_signal):
        cca = sk.CCA(self.n_components)

        correlations = np.zeros(reference_signal.shape[0])

        for j in range(0,data.shape[0]):

            channel_data = data[j]
            channel_data = np.array(channel_data).reshape(tuple([1,250]))


            for i in range(0,reference_signal.shape[0]):
                freq = np.squeeze(reference_signal[i,:,:]).T

                cca.fit(channel_data.T,freq)
                x,y = cca.transform(channel_data.T,freq)

                p_correlation = np.corrcoef(x[:,0],y[:,0])[0,1]

                if correlations[i] < p_correlation:
                    correlations[i] = p_correlation

        return correlations

    def process(self, dataList):
        dataUn = self.board.get_streaming_data(self.timeframe)

        data = self.board.filter_data(dataUn)

        ref_signal = self.generate_ref_signal(self.reference_signal,data.shape[1])
        
        correlations = self.calculate_correlations(data,ref_signal)

        max_correlation = max(correlations,key = float)
        frequency = self.frequecies[np.argmax(correlations)]

        for i in range(len(dataList)):
            dataList[i].extend(dataUn[i])


        return max_correlation, frequency