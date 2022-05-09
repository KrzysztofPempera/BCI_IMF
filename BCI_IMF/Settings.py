import json

with open ('appsettings.json', 'r') as para:
    config = json.load(para)

class Config(config):

    def __init__(config):
        self.classifierType = config['classifier']['type']
        self.classifierRefSignal = config['classifer']['referenceSignal']
        self.classifierDataChunk = config['classifer']['dataChunk']

        self.baseSignals = config['referenceSignals']['baseSignal']
        self.phaseShifts = config['referenceSignal']['phaseShift']