import numpy as np

class ReferenceSignal():
    def __init__(self, config):
        self.referenceSignalType = config.classifierRefSignal

        self.baseSignals = config.baseSignals
        self.phaseShifts = config.phaseShifts

    def createReferenceSignals(self) -> list:
        signalCount = len(self.baseSignals)*len(self.phaseShifts)
        refSignals = []

        for frequency in self.baseSignals:
            for shift in self.phaseShifts:
                refSignals.append(self.__createReferenceSignal__(frequency,shift))

        return refSignals

    def __createReferenceSignal__(self, baseSignal, phaseShift) -> float:
         refSignal = 2 * baseSignal * np.pi + phaseShift*np.pi
         return refSignal