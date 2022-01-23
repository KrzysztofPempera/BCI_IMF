from psychopy import visual, core, event
from numpy import sin, pi
import random

height = 720
width = 1280

frame = 0
freq = 10
stimuli_colour = [-1,1,-1]

window = visual.Window([width,height], monitor = "testMonitor", units = 'pix', fullscr = False, color = [-1,-1,-1])


stimuli1 = visual.Rect(win = window, size = 300, units = 'pix', fillColor = stimuli_colour, pos =(-400, 0))
stimuli2 = visual.Rect(win = window, size = 300, units = 'pix', fillColor = stimuli_colour, pos =(0, 0))
stimuli3 = visual.Rect(win = window, size = 300, units = 'pix', fillColor = stimuli_colour, pos =(400, 0))
n = 0


stimuli1.draw()
stimuli2.draw()
stimuli3.draw()
window.flip()

def modulate_stimuli_opacity(stimuli, frame, freq, refresh_rate, phase_shift):
    time = frame/refresh_rate
    stimuli.setOpacity((1 + sin(2 * pi * freq * time + phase_shift))/2)
    stimuli.draw()

def modulate_stimuli_colour(stimuli, frame, freq, refresh_rate, phase_shift):
    time = frame/refresh_rate
    stimuli.setColor([-1,(1 + sin(2 * pi * freq * time + phase_shift))/2,-1])
    stimuli.draw()


while True:
    

    frame += 1

    modulate_stimuli_colour(stimuli1,frame,freq,window.monitorFramePeriod,0)
    modulate_stimuli_colour(stimuli2,frame,freq,window.monitorFramePeriod,0.5)
    modulate_stimuli_colour(stimuli3,frame,freq,window.monitorFramePeriod,1)

    window.flip()

    for key in event.getKeys():
        if key in ['escape']:
            core.quit()



