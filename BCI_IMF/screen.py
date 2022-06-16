from psychopy import visual, core, event
from numpy import sin, pi
import random

class screen():
    def __init__(self):
        self.height = 900
        self.width = 1600
        self.frame = 0
        self.start_frame = 0
        self.freq = 10
        self.stimuli_colour = [-1,1,-1]


    def run(self, start_program, quit_program, current_stimuli):

        window = visual.Window([self.width,self.height], monitor = "testMonitor", units = 'pix', fullscr = False, color = [-1,-1,-1])

        stimuli1 = visual.Rect(win = window, size = 200, units = 'pix', fillColor = self.stimuli_colour, pos =(-600, 300))
        stimuli2 = visual.Rect(win = window, size = 200, units = 'pix', fillColor = self.stimuli_colour, pos =(0, 0))
        stimuli3 = visual.Rect(win = window, size = 200, units = 'pix', fillColor = self.stimuli_colour, pos =(600, -300))

        marker1 = visual.Rect(win = window, size = 30, units = 'pix', fillColor = [1,1,1], pos =(-600, 0))
        marker2 = visual.Rect(win = window, size = 30, units = 'pix', fillColor = [1,1,1], pos =(0, 300))
        marker3 = visual.Rect(win = window, size = 30, units = 'pix', fillColor = [1,1,1], pos =(600, 0))

        stimuli1.draw()
        stimuli2.draw()
        stimuli3.draw()

        window.flip()

        while True:

            self.frame += 1

            self.__modulate_stimuli_opacity__(stimuli1, self.frame, self.freq, 60, 0)
            self.__modulate_stimuli_opacity__(stimuli2, self.frame, self.freq, 60, 0.35)
            self.__modulate_stimuli_opacity__(stimuli3, self.frame, self.freq, 60, 1.65)

            window.flip()

            for key in event.getKeys():
                if key in ['escape']:
                    core.quit()

                if key in ['space']:
                    start_program.set()

            if start_program.is_set():
                self.start_frame += 1

                if self.start_frame >= 300 and self.start_frame <= 1200:
                    current_stimuli.value = 0.0
                    marker1.draw()

                elif self.start_frame <= 1320:
                    current_stimuli.value = 42

                elif self.start_frame >=1320 and self.start_frame <= 2220:
                    current_stimuli.value = 0.35
                    marker2.draw()

                elif self.start_frame <= 2340:
                    current_stimuli.value = 42

                elif self.start_frame >= 2340 and self.start_frame <= 3240:
                    current_stimuli.value = 1.65
                    marker3.draw()

                elif self.start_frame <= 3300:
                    current_stimuli.value = 42


                elif self.start_frame > 3300:
                    quit_program.set()
                    core.quit()
                    break


    def __modulate_stimuli_opacity__(self, stimuli, frame, freq, refresh_rate, phase_shift):
        time = frame/refresh_rate
        stimuli.setOpacity((1 + sin(2 * pi * freq * time + phase_shift*pi))/2)
        stimuli.draw()

    def __modulate_stimuli_colour__(self, stimuli, frame, freq, refresh_rate, phase_shift):
        time = frame/refresh_rate
        stimuli.setColor([-1,(1 + sin(2 * pi * freq * time + phase_shift*pi))/2,-1])
        stimuli.draw()
