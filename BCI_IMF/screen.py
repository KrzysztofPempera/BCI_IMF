from psychopy import visual, core, event
from numpy import sin, pi
import random

class screen():
    def __init__(self):
        self.height = 720
        self.width = 1280
        self.frame = 0
        self.freq = 10
        self.stimuli_colour = [-1,1,-1]
        self.window = visual.Window([width,height], monitor = "testMonitor", units = 'pix', fullscr = False, color = [-1,-1,-1])

        self.stimuli1 = visual.Rect(win = window, size = 300, units = 'pix', fillColor = stimuli_colour, pos =(-400, 0))
        self.stimuli2 = visual.Rect(win = window, size = 300, units = 'pix', fillColor = stimuli_colour, pos =(0, 0))
        self.stimuli3 = visual.Rect(win = window, size = 300, units = 'pix', fillColor = stimuli_colour, pos =(400, 0))

        def __modulate_stimuli_opacity__(self, stimuli, frame, freq, refresh_rate, phase_shift):
            time = frame/refresh_rate
            stimuli.setOpacity((1 + sin(2 * pi * freq * time + phase_shift*pi))/2)
            stimuli.draw()

        def __modulate_stimuli_colour__(self, stimuli, frame, freq, refresh_rate, phase_shift):
            time = frame/refresh_rate
            stimuli.setColor([-1,(1 + sin(2 * pi * freq * time + phase_shift*pi))/2,-1])
            stimuli.draw()

        def run(self):

            self.stimuli1.draw()
            self.stimuli2.draw()
            self.stimuli3.draw()

            self.window.flip()

            while True:

                self.frame += 1

                self.__modulate_stimuli_opacity__(self.stimuli1, self.frame, self.freq, 60, 0)
                self.__modulate_stimuli_opacity__(self.stimuli2, self.frame, self.freq, 60, 0.5)
                self.__modulate_stimuli_opacity__(self.stimuli3, self.frame, self.freq, 60, 0.5)

                self.window.flip()

                for key in event.getKeys():
                    if key in ['escape']:
                        core.quit()