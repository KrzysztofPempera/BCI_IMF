import json
import mypy

with open ('appsettings.json', 'r') as para:
    config = json.load(para)

class Config(config):

    def __init__(self, config):
        self.classifierType:str = config['classifier']['type']
        self.classifierRefSignal:str = config['classifer']['referenceSignal']
        self.classifierDataChunk:int = config['classifer']['dataChunk']

        self.baseSignals:list = config['referenceSignals']['baseSignal']
        self.phaseShifts:list = config['referenceSignal']['phaseShift']

        self.boardID:int = config['eegBoard']['ID']
        self.boardPort:str = config['eegBoard']['port']

        self.stimuliCount:int = config['stimuli']['count']
        self.stimuliColour:str = config['stimuli']['colour']