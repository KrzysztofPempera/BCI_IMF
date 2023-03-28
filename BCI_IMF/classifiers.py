import numpy as np
import sklearn.cross_decomposition as sk
import sys
from brainflow.data_filter import DataFilter, FilterTypes

np.set_printoptions(threshold=sys.maxsize)

class classic_CCA():
    def __init__(self, n_components, timeframe, reference_signal = None):
        self.n_components = n_components
        self.reference_signal = reference_signal
        self.sampling_rate = 200
        self.frequecies = ["7.5", "12", "10", "8.6", "6.7"]
        self.timeframe = timeframe
        

    def generate_ref_signal(self, lenght):
        time = np.linspace(0, lenght/self.sampling_rate, self.timeframe*self.sampling_rate )
        ref_signal = []
        
        frequencies = [7.5,12,10,8.6,6.7]

        for freq in frequencies:
            temp_ref_signal = []
            temp_ref_signal.append(np.sin(2 * np.pi * freq * time))
            temp_ref_signal.append(np.cos(2 * np.pi * freq * time))
            temp_ref_signal.append(np.sin(2 * np.pi * freq * 2 * time))
            temp_ref_signal.append(np.cos(2 * np.pi * freq * 2 * time))
            
            ref_signal.append(np.array(temp_ref_signal))
        

        ref_signal = np.array(ref_signal)

        return ref_signal

    def calculate_correlations(self, data, reference_signal):
        cca = sk.CCA(self.n_components)

        correlations = np.zeros(reference_signal.shape[0])

        cca_data = np.array(data[:]).reshape(4,1000)

        for i in range(0,reference_signal.shape[0]):
            freq = np.squeeze(reference_signal[i,:,:]).T

            cca.fit(cca_data.T,freq)
            x,y = cca.transform(cca_data.T,freq)

            p_correlation = np.corrcoef(x[:,0],y[:,0])[0,1]

            correlations[i] = p_correlation

        return correlations

    def process(self, dataUn):

        data = self.filter_data(dataUn)

        ref_signal = self.generate_ref_signal(data.shape[1])
        
        correlations = self.calculate_correlations(data,ref_signal)

        max_correlation = max(correlations,key = float)
        frequency = self.frequecies[np.argmax(correlations)]



        return max_correlation, frequency

    def filter_data(self, data):
        for dat in data:
            DataFilter.perform_bandstop(dat, self.sampling_rate, 49, 51, 2, FilterTypes.BUTTERWORTH.value, 0)
            DataFilter.perform_bandpass(dat, self.sampling_rate, 7, 26, 2, FilterTypes.BUTTERWORTH.value, 0)

        

        return data