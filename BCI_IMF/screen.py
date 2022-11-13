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
        self.screen_freq = 60
        self.classifier_timeframe = 1
        self.stimuli_colour = [-1,1,-1]

    def __modulate_stimuli_opacity__(self, stimuli, frame, freq, refresh_rate, phase_shift):
        time = frame/refresh_rate
        stimuli.setOpacity((1 + sin(2 * pi * freq * time + phase_shift*pi))/2)
        stimuli.draw()

    def __modulate_stimuli_colour__(self, stimuli, frame, freq, refresh_rate, phase_shift):
        time = frame/refresh_rate
        stimuli.setColor([-1,(1 + sin(2 * pi * freq * time + phase_shift*pi))/2,-1])
        stimuli.draw()

    def __set_start__(self, stim1,stim2,stim3,window):
        stim1.draw()
        stim2.draw()
        stim3.draw()

        window.flip()

    def run(self, start_program, quit_program, current_stimuli):

        window = visual.Window([self.width,self.height], monitor = "testMonitor", units = 'pix', fullscr = False, color = [-1,-1,-1])

        stimuli1 = visual.Rect(win = window, size = 200, units = 'pix', fillColor = self.stimuli_colour, pos =(-600, 300))
        stimuli2 = visual.Rect(win = window, size = 200, units = 'pix', fillColor = self.stimuli_colour, pos =(0, 0))
        stimuli3 = visual.Rect(win = window, size = 200, units = 'pix', fillColor = self.stimuli_colour, pos =(600, -300))

        marker1 = visual.Rect(win = window, size = 30, units = 'pix', fillColor = [1,1,1], pos =(-600, 0))
        marker2 = visual.Rect(win = window, size = 30, units = 'pix', fillColor = [1,1,1], pos =(0, 300))
        marker3 = visual.Rect(win = window, size = 30, units = 'pix', fillColor = [1,1,1], pos =(600, 0))

        welcomeText = visual.TextStim(win = window, text = "Podczas badania wyświetlone zostanie 5 migających kwadratów. Twoim zadaniem będzie skupienie wzroku, na kwardracie oznaczonym przez biały marker. Całość badania trwa 10 minut i jest podzielona na trzy ok. 3minutowe części. Po każdej z cześci nastąpi 3 minutowa przerwa. Naciśnij spację, aby rozpocząć.", height = 20)
        breakText = visual.TextStim(win = window, text = "Przerwa. Aby kontynuować, naciśnij spację.", height = 20)
        endText = visual.TextStim(win = window, text = "To koniec. Dziękujemy za udział w badaniu.", height = 20)
        
        first = False
        breakTime = False

        while True:

            self.frame += 1

            if start_program.is_set() == False and self.start_frame < 1:
                welcomeText.draw()

            if breakTime == True:
                start_program.clear()
                if start_program.is_set() == False:
                    breakText.draw()
                

            window.flip()

            for key in event.getKeys():
                if key in ['escape']:
                    core.quit()

                if key in ['space']:
                    start_program.set()
                    first = True
                    breakTime = False

            if start_program.is_set() and breakTime == False:
                if first == True:
                    self.__set_start__(stimuli1,stimuli2,stimuli3,window)

                self.start_frame += 1

                self.__modulate_stimuli_opacity__(stimuli1, self.start_frame, 7.5, self.screen_freq, 0)
                self.__modulate_stimuli_opacity__(stimuli2, self.start_frame, 12, self.screen_freq, 0)
                self.__modulate_stimuli_opacity__(stimuli3, self.start_frame, 14, self.screen_freq, 0)

                if self.start_frame >= self.screen_freq*5 and self.start_frame <= self.screen_freq*30:
                    if self.start_frame >= self.screen_freq*5 + self.classifier_timeframe*self.screen_freq:
                        current_stimuli.value = 7.5
                    marker1.draw()

                elif self.start_frame == self.screen_freq*31:
                    breakTime = True
                    current_stimuli.value = 42

                elif self.start_frame < self.screen_freq*35:
                    current_stimuli.value = 42

                elif self.start_frame >= self.screen_freq*35 and self.start_frame <= self.screen_freq*65:
                    if self.start_frame >= self.screen_freq*35 + self.classifier_timeframe*self.screen_freq:
                        current_stimuli.value = 12
                    marker2.draw()

                elif self.start_frame <= self.screen_freq*70:
                    current_stimuli.value = 42

                elif self.start_frame >= self.screen_freq*70 and self.start_frame <= self.screen_freq*100:
                    if self.start_frame >= self.screen_freq*70 + self.classifier_timeframe*self.screen_freq:
                        current_stimuli.value = 14
                    marker3.draw()

                elif self.start_frame <= self.screen_freq*105:
                    current_stimuli.value = 42


                elif self.start_frame > self.screen_freq*105:
                    quit_program.set()
                    core.quit()
                    break
                



