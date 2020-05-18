#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.3),
on Fri 27 Sep 2019 03:45:12 PM CEST
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019)
    PsychoPy2: Experiments in behavior made easy Behav Res 51: 195.
    https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)

from random import choice, shuffle
from collections import defaultdict
from numpy.random import randint, normal, shuffle
import random
import os  # handy system and path functions
import sys  # to get file system encoding
import pandas as pd


from psychopy.hardware import keyboard

wait_between_images = 1 # time of empty screen between images
text_after_image = 2 # the nominalization appears after this many seconds the stimulus was shown
press_time = 8 # time spent waiting for input

# reading datafile which will be used when creating iterable object

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.3'
expName = 'Zimmerertest'  # from the Builder filename that created this script

expInfo = {'participant': '', 'session': '001',
           'date': data.getDateStr(), 'list_name': '1', 'random_seed': int(data.getDateStr()[-4:])}



dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK is False:
    core.quit()  # user pressed cancel
    expInfo['date'] = data.getDateStr()  # add a simple timestamp
    expInfo['expName'] = expName
    expInfo['psychopyVersion'] = psychopyVersion

print(f'list is {expInfo["list_name"]}')
rand_seed = expInfo['random_seed']
print(f'random seed is {rand_seed}')
np.random.seed(expInfo['random_seed'])

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
                                 extraInfo=expInfo, runtimeInfo=None,
                                 originPath='/home/levai/ELTE_notes/Neuro/Zimmerer/project_WIP/click_to_advance.py',
                                 savePickle=True, saveWideText=True,
                                 dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation


# Setup the Window
win = visual.Window(
    size=(1366, 768), fullscr=True, screen=0,
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='height', waitBlanking=False)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] is not None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Some useful functions


def shuffle_title(string, updown, leftright):
    # 1 is up and left, it says nom1's position, nom2 ios diagonal to that
    nom1, nom2 = string.split('#')
    if updown == 1 and leftright == 1:
        formatted_string = f"⅄:  {nom1}\n{' '*len(nom1)*2}Ɔ:  {nom2}"
    if updown == 0 and leftright == 1:
        formatted_string = f"{' '*len(nom1)*2}⅄: {nom2}\nƆ:  {nom1}"
    if updown == 1 and leftright == 0:
        formatted_string = f"{' '*len(nom2)*2}⅄: {nom1}\nƆ:  {nom2}"
    if updown == 0 and leftright == 0:
        formatted_string = f"⅄:  {nom2}\n{' '*len(nom2)*2}Ɔ:  {nom1}"
    
    return(formatted_string)

#print(images_dict)
#print(sentences_dict)

_nom1order = np.random.randint(2, size=4)
_nom2order = np.random.randint(2, size=4)

nomin_orders = list(zip(_nom1order, _nom2order))

images = []
key_responses = []
directions = []
nominalizations = []
# helps = []
instructions = []

blocks = [ 'image', 'sentence']

# raise(BaseException)

stimulus_data = ['Figyelmeztetes.png', 'Emlekeztetes.png', 'Józsi üti Bélát.', 'Mari nézi Julit.']
nom_data = ['a hölgy figyelmeztetése#az úr figyelmeztetése', 'a lány emlékeztetése#a férfi emlékeztetése', 'Józsi ütése#Béla ütése', 'Juli nézése#Mari nézése']

fixations = []
stimuli = []
instruction_keypresses = []
start_and_end = []

nom_position = (8/9-0.05, -0.4)
# TODO hardcoded stuff
for iteration_index, i in enumerate([1, 2, 3, 4]):
    
    x_order, y_order = nomin_orders[iteration_index]
    #nominalizations += [create_textstim(f, 
    #                          , ), 
    #                          pos = , )]

    nominalizations += [visual.TextStim(
        alignHoriz='right',
        win=win,
        name="title_{i}",
        font='Noto Sans',
        text=shuffle_title(nom_data[iteration_index], x_order, y_order),
        pos=nom_position,
        height=0.04,
        wrapWidth=1.4)]

    #fixations += [create_textstim(, '?', size = 0.15, , pos = nom_position)]
    
    fixations += [visual.TextStim(
        alignHoriz='right',
        win=win,
        name=f'fix_{i}',
        font='Noto Sans Mono',
        text='?',
        pos=nom_position,
        # color = color,
        height=0.15,
        wrapWidth=1.4)]

    current_block = blocks[iteration_index//2]
    if current_block == 'image':
        cur_image = stimulus_data[iteration_index]

        stimuli += [visual.ImageStim(
            win=win,
            name=f'image<>{i}',
            image=os.path.join('pictures', cur_image), mask=None,
            ori=0, pos=(0, 0), size=(0.85, 0.6),
            color=[1, 1, 1], colorSpace='rgb', opacity=1,
            flipHoriz=False, flipVert=False,
            texRes=128, interpolate=True, depth=0.0)]

        
    else:
        sentence = stimulus_data[iteration_index]
        # stimuli += [create_textstim(f'sentence<>{i}<>{plaus}<>{sentence}', sentence, pos=(0.0, 0), , size = 0.08)]


        stimuli += [visual.TextStim(
            alignHoriz='center',
            win=win,
            name=f'sentence<>{i}<>{sentence}',
            font='Liberation Serif',
            text=sentence,
            pos=(0.0, 0),
            height=0.08,
            wrapWidth=1.4)]

    current_key = keyboard.Keyboard()
    current_key.keys = []
    current_key.rt = []
    key_responses += [current_key]
    random.seed(rand_seed + iteration_index)
    directions += choice(['l', 'r'])
    
    # help_text = create_textstim(, '', , size=0.03)

    # helps += [visual.TextStim(
    #     alignHoriz='center',
    #     win=win,
    #     name=f'H{i}',
    #     font='Noto Sans',
    #     text='⅄ cím: ⅄ gomb\nƆ cím: Ɔ gomb',
    #     pos=(-0.7, -0.4),
    #     height=0.03,
    #     wrapWidth=1.4)]

    if iteration_index%2 == 0 and blocks[iteration_index//2] == 'image':
        instructions += [visual.TextStim(
        alignHoriz='center',
        win=win,
        name=f'H{i}',
        font='Noto Sans',
        text='Ön képeket fog látni. Majd a képernyő jobb alsó sarkában két felirat jelenik meg. Válassza ki közülük azt, amelyik legjobban kifejezi a kép lényegét.' + '\n' +
                'A feliratok közül a ⅄ és Ɔ gomb egyszeri lenyomásával válasszon.' + '\n' + 
                'Figyelem! A feliratok választásához rövid idő áll rendelkezésre. Amennyiben nem választott feliratot, a teszt végén megismétlődik egyszer a kép.\n' +
                'Nyomjon szóközt a továbbhaladáshoz.',        
        pos=(0, 0),
        height=0.05,
        wrapWidth=1.3)]
        current_key = keyboard.Keyboard()
        current_key.keys = []
        current_key.rt = []
        instruction_keypresses += [current_key]

    if iteration_index%2 == 0 and blocks[iteration_index//2] == 'sentence':
        instructions += [visual.TextStim(
        alignHoriz='center',
        win=win,
        name=f'H{i}',
        font='Noto Sans',
        text='Ön mondatokat fog látni. Majd a képernyő jobb alsó sarkában két felirat jelenik meg. Válassza ki közülük azt, amelyik legjobban kifejezi a mondat lényegét.' + '\n' +
                'A feliratok közül a ⅄ és Ɔ gomb egyszeri lenyomásával válasszon.' + '\n' + 
                'Figyelem! A feliratok választásához rövid idő áll rendelkezésre. Amennyiben nem választott feliratot, a teszt végén megismétlődik egyszer a mondat.\n' +
                'Nyomjon szóközt a továbbhaladáshoz.',        pos=(0, 0),
        height=0.05,
        wrapWidth=1.3)]
        current_key = keyboard.Keyboard()
        current_key.keys = []
        current_key.rt = []
        instruction_keypresses += [current_key]

start_and_end_keypresses = []

for i in range(2):
    current_key = keyboard.Keyboard()
    current_key.keys = []
    current_key.rt = []
    start_and_end_keypresses += [current_key]


start_and_end += [visual.TextStim(
        alignHoriz='center',
        win=win,
        name=f'H{i}',
        font='Noto Sans',
        text='Köszöntjük Budapesten, csodás ma az idő. Dőljön hátra, és élvezze a tesztet.\nNyomja meg a space gombot a teszt elindításához.',
        pos=(0, 0),
        height=0.05,
        wrapWidth=1.3)]

start_and_end += [visual.TextStim(
        alignHoriz='center',
        win=win,
        name=f'H{i}',
        font='Noto Sans',
        text='Ez a tanítófázis volt.' + '\n' +
              'Kérjük, nyomja meg a space gombot a tanítófázis befejezéséhez.',
        pos=(0, 0),
        height=0.05,
        wrapWidth=1.3)] 


retry_instruction = visual.TextStim(
        alignHoriz='center',
        win=win,
        name=f'H{i}',
        font='Noto Sans',
        text='Most újra meg fognak jelenni azok a képek és mondatok, amelyekre nem adott választ. ' + '\n' + 
              'Nyomjon szóközt a folytatáshoz.',
        pos=(0, 0),
        height=0.05,
        wrapWidth=1.3)

retry_inst_keypress = keyboard.Keyboard()
retry_inst_keypress.keys = []
retry_inst_keypress.rt = []



# raise('STOPHERE')

    


key_test = keyboard.Keyboard()


# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()


# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine

# ------Prepare to start Routine "trial"-------
routineTimer.add(8000.000000)
# update component parameters for each repeat
# keep track of which components have finished
trialComponents = stimuli + key_responses + nominalizations + fixations + instructions + instruction_keypresses + start_and_end + \
    start_and_end_keypresses + [retry_instruction, retry_inst_keypress]
for thisComponent in trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True
LIST_OF_KEYS = []
LIST_OF_INST_KEYS = []

#### PARAMETERS: #####



last_keypress_timestamp = -wait_between_images # to start slideshow at 0

DBG_end_of_last_image = -1

is_test_started = False
is_test_stopped = False

is_test_started = False
is_test_stopped = False
is_normal_routine_stopped = False

#################################################################################
####                              MAIN ROUTINE                               ####
#################################################################################


# -------Run Routine "trial"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame




    ############# STARTING SCREEN ###############

    if not is_test_started:
        
        screen = start_and_end[0]

        if screen.status == NOT_STARTED:
            # we have pressed i-1 keys so we are viewing the i_th picture
            # we also wait for wait_between_images second before showing the next
            # keep track of start time/frame for later
            # print(f"LAST IMAGE ENDED {(t - DBG_end_of_last_image):.3f} s ago")

            screen.frameNStart = frameN  # exact frame index
            screen.tStart = t  # local t and not account for scr refresh
            screen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(screen, 'tStartRefresh')  # time at next scr refresh
            screen.setAutoDraw(True)
            # print(image.frameNStart)
            # print(f'Last keypress time: {last_keypress_timestamp:.5f}')
            # print(f'starting image {i}: {stimulus.tStart:.5f}')
            
            # print(image.frameNStart/image.tStart)

        if screen.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if len(start_and_end_keypresses[0].keys) != 0:
                # keep track of stop time/frame for later
                screen.tStop = t  # not accounting for scr refresh
                screen.frameNStop = frameN  # exact frame index
                win.timeOnFlip(screen, 'tStopRefresh')  # time at next scr refresh
                screen.setAutoDraw(False)
                # print(f'stopping image {i}: {stimulus.tStop:.5f}')
                is_test_started = True
                # print('stopped start image')
                # print(f'{is_test_started} {is_test_stopped}')
            

        waitOnFlip = False
        if start_and_end_keypresses[0].status == NOT_STARTED: 
            
            # print('start sequence started, logging keys')
            start_and_end_keypresses[0].frameNStart = frameN  # exact frame index
            start_and_end_keypresses[0].tStart = t  # local t and not account for scr refresh
            start_and_end_keypresses[0].tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(start_and_end_keypresses[0], 'tStartRefresh')  # time at next scr refresh
            start_and_end_keypresses[0].status = STARTED
            # keyboard checking is just starting
            # print(f"time when entered key {i}: {key_inst.tStart}")
            waitOnFlip = True
            win.callOnFlip(start_and_end_keypresses[0].clock.reset)  # t=0 on next screen flip
            win.callOnFlip(start_and_end_keypresses[0].clearEvents, eventType='keyboard')  # clear events on next screen flip
            

        if start_and_end_keypresses[0].status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if len(start_and_end_keypresses[0].keys) != 0:
                # keep track of stop time/frame for later
                start_and_end_keypresses[0].tStop = t  # not accounting for scr refresh
                start_and_end_keypresses[0].frameNStop = frameN  # exact frame index
                win.timeOnFlip(start_and_end_keypresses[0], 'tStopRefresh')  # time at next scr refresh
                start_and_end_keypresses[0].status = FINISHED
                #print(key_responses)

        if start_and_end_keypresses[0].status == STARTED and not waitOnFlip:
            theseKeys = start_and_end_keypresses[0].getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                last_keypress_timestamp = t
                # print(theseKeys.name)
                # print(theseKeys.name)
                # print(theseKeys.rt)
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                start_and_end_keypresses[0].keys.append(theseKeys.name)  # storing all keys
                start_and_end_keypresses[0].rt.append(theseKeys.rt)
        



    ############# MAIN CYCLE #################
    if is_test_started and not is_normal_routine_stopped:
        
        for i, stimulus in enumerate(stimuli):
            
            KEY_INDEX = len(LIST_OF_KEYS)
            key_resp = key_responses[i]
            nominalization = nominalizations[i]
            # help_text = helps[i]
            instruction = instructions[i//2]
            fixation = fixations[i]
            INSTRUCTION_INDEX = len(LIST_OF_INST_KEYS)
            key_inst = instruction_keypresses[i//2]


            # IMAGE LOGIC

            if stimulus.status == NOT_STARTED and \
                i == KEY_INDEX and \
                t > last_keypress_timestamp + wait_between_images and \
                INSTRUCTION_INDEX == i//2+1: 
                # we have pressed i-1 keys so we are viewing the i_th picture
                # we also wait for wait_between_images second before showing the next
                # keep track of start time/frame for later

                stimulus.frameNStart = frameN  # exact frame index
                stimulus.tStart = t  # local t and not account for scr refresh
                stimulus.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stimulus, 'tStartRefresh')  # time at next scr refresh
                stimulus.setAutoDraw(True)

            if stimulus.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if i != KEY_INDEX:
                    # keep track of stop time/frame for later
                    stimulus.tStop = t  # not accounting for scr refresh
                    DBG_end_of_last_image = t
                    stimulus.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stimulus, 'tStopRefresh')  # time at next scr refresh
                    stimulus.setAutoDraw(False)
                
                time_elapsed = t - stimulus.tStart


            # TEXT LOGIC

            if nominalization.status == NOT_STARTED and \
                i == KEY_INDEX and \
                t > last_keypress_timestamp + wait_between_images + \
                    text_after_image and \
                INSTRUCTION_INDEX == i//2+1: 
                # keep track of start time/frame for later
                nominalization.frameNStart = frameN  # exact frame index
                nominalization.tStart = t  # local t and not account for scr refresh
                nominalization.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(nominalization, 'tStartRefresh')  # time at next scr refresh
                nominalization.setAutoDraw(True)

            if nominalization.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if i != KEY_INDEX:
                    # keep track of stop time/frame for later
                    nominalization.tStop = t  # not accounting for scr refresh
                    nominalization.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(nominalization, 'tStopRefresh')  # time at next scr refresh
                    nominalization.setAutoDraw(False)


            # FIXATION LOGIC
            if fixation.status == NOT_STARTED and \
                i == KEY_INDEX and \
                t > last_keypress_timestamp + wait_between_images and \
                INSTRUCTION_INDEX == i//2+1: 
                # keep track of start time/frame for later
                fixation.frameNStart = frameN  # exact frame index
                fixation.tStart = t  # local t and not account for scr refresh
                fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
                fixation.setAutoDraw(True)

            if fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if t > fixation.tStart + text_after_image - 1/20:
                    # keep track of stop time/frame for later
                    fixation.tStop = t  # not accounting for scr refresh
                    fixation.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                    fixation.setAutoDraw(False)
                # fixation.ori = (frameN*8)%360

            # KEY LOGIC
            # logs STIMULUSkeys
            waitOnFlip = False
            if key_resp.status == NOT_STARTED and \
                i == KEY_INDEX and \
                t > last_keypress_timestamp + wait_between_images + \
                    text_after_image and \
                INSTRUCTION_INDEX == i//2+1: 
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                key_resp.status = STARTED
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                

            if key_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if i != KEY_INDEX:
                    # keep track of stop time/frame for later
                    key_resp.tStop = t  # not accounting for scr refresh
                    key_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                    key_resp.status = FINISHED

            if key_resp.status == STARTED and not waitOnFlip:
                if t - key_resp.tStart <= press_time:
                    theseKeys = key_resp.getKeys(keyList=['x', 'o'], waitRelease=False)
                    if len(theseKeys):
                        theseKeys = theseKeys[0]  # at least one key was pressed
                        LIST_OF_KEYS += [theseKeys.name]
                        last_keypress_timestamp = t
                        if "escape" == theseKeys:
                            endExpNow = True
                        key_resp.keys.append(theseKeys.name)  # storing all keys
                        key_resp.rt.append(theseKeys.rt)
                else:
                    LIST_OF_KEYS += ['n']
                    key_resp.keys.append('n')
                    key_resp.rt.append(press_time)
                    last_keypress_timestamp = t

            #####################################################################
            # INSTRUCTIONS LOGIC
            # SHOWN BEFORE BLOX

            if instruction.status == NOT_STARTED and INSTRUCTION_INDEX == KEY_INDEX//2 and KEY_INDEX % 2 == 0 and INSTRUCTION_INDEX == i // 2 and \
                t > last_keypress_timestamp + wait_between_images:
                instruction.frameNStart = frameN  # exact frame index
                instruction.tStart = t  # local t and not account for scr refresh
                instruction.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(instruction, 'tStartRefresh')  # time at next scr refresh
                instruction.setAutoDraw(True)

            if instruction.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if INSTRUCTION_INDEX != i//2:
                    # keep track of stop time/frame for later
                    instruction.tStop = t  # not accounting for scr refresh
                    instruction.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(instruction, 'tStopRefresh')  # time at next scr refresh
                    instruction.setAutoDraw(False)

            waitOnFlip = False
            if key_inst.status == NOT_STARTED and INSTRUCTION_INDEX == KEY_INDEX//2 and KEY_INDEX % 2 == 0 and INSTRUCTION_INDEX == i // 2 and \
                t > last_keypress_timestamp + wait_between_images: 
                # keep track of start time/frame for later
                key_inst.frameNStart = frameN  # exact frame index
                key_inst.tStart = t  # local t and not account for scr refresh
                key_inst.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_inst, 'tStartRefresh')  # time at next scr refresh
                key_inst.status = STARTED
                waitOnFlip = True
                win.callOnFlip(key_inst.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_inst.clearEvents, eventType='keyboard')  # clear events on next screen flip
                

            if key_inst.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if i//2 != INSTRUCTION_INDEX:
                    # keep track of stop time/frame for later
                    key_inst.tStop = t  # not accounting for scr refresh
                    key_inst.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_inst, 'tStopRefresh')  # time at next scr refresh
                    key_inst.status = FINISHED

            if key_inst.status == STARTED and not waitOnFlip:

                theseKeys = key_inst.getKeys(keyList=['space'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    LIST_OF_INST_KEYS += [theseKeys.name]
                    last_keypress_timestamp = t
                    if "escape" == theseKeys:
                        endExpNow = True
                    key_inst.keys.append(theseKeys.name)  # storing all keys
                    key_inst.rt.append(theseKeys.rt)
                

            if KEY_INDEX == len(stimuli):
                is_normal_routine_stopped = True

##########################################################################
       

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        break

    # check if all components have finished
    if is_normal_routine_stopped:  # a component has requested a forced-end of Routine
        break

    win.flip()







########################################################################
###                        RETRY ROUTINE                             ###
########################################################################



retry_indices = [i for (i, l) in enumerate(LIST_OF_KEYS) if l == 'n']
#HACK 
# retry_indices = [0, 2, 11]
print('indices they need to retry are:')
print(retry_indices)



for i in retry_indices:
    stimuli[i].status = NOT_STARTED
    key_responses[i].status = NOT_STARTED
    nominalizations[i].status = NOT_STARTED
    fixations[i].status = NOT_STARTED
    key_responses[i].keys = []
    key_responses[i].rt = []

retry_inst_shown = False
RETRY_KEYS = []

print('STARTED NEW ROUTINE')

while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    if len(RETRY_KEYS) == len(retry_indices) and t > last_keypress_timestamp + wait_between_images + 0.1:
        is_test_stopped = True

    if len(retry_indices) == 0:
        retry_inst_shown = True
        is_test_stopped = True

    if not retry_inst_shown:

        screen = retry_instruction
        key_event = retry_inst_keypress

        if screen.status == NOT_STARTED:
            # we have pressed i-1 keys so we are viewing the i_th picture
            # we also wait for wait_between_images second before showing the next
            screen.frameNStart = frameN  # exact frame index
            screen.tStart = t  # local t and not account for scr refresh
            screen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(screen, 'tStartRefresh')  # time at next scr refresh
            screen.setAutoDraw(True)

        if screen.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if len(key_event.keys) != 0:
                # keep track of stop time/frame for later
                screen.tStop = t  # not accounting for scr refresh
                screen.frameNStop = frameN  # exact frame index
                win.timeOnFlip(screen, 'tStopRefresh')  # time at next scr refresh
                screen.setAutoDraw(False)
                retry_inst_shown = True
            

        waitOnFlip = False
        if key_event.status == NOT_STARTED: 
            # keep track of start time/frame for later
            key_event.frameNStart = frameN  # exact frame index
            key_event.tStart = t  # local t and not account for scr refresh
            key_event.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_event, 'tStartRefresh')  # time at next scr refresh
            key_event.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_event.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_event.clearEvents, eventType='keyboard')  # clear events on next screen flip
            

        if key_event.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if len(key_event.keys) != 0:
                # keep track of stop time/frame for later
                key_event.tStop = t  # not accounting for scr refresh
                key_event.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_event, 'tStopRefresh')  # time at next scr refresh
                key_event.status = FINISHED

        if key_event.status == STARTED and not waitOnFlip:
            theseKeys = key_event.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                last_keypress_timestamp = t
                if "escape" == theseKeys:
                    endExpNow = True
                key_event.keys.append(theseKeys.name)  # storing all keys
                key_event.rt.append(theseKeys.rt)

                



    if not is_test_stopped and retry_inst_shown:
    
        for i, r_ind in enumerate(retry_indices):
            
            stimulus = stimuli[r_ind]
            KEY_INDEX = len(RETRY_KEYS)
            key_resp = key_responses[r_ind]
            nominalization = nominalizations[r_ind]
            # help_text = helps[i]
            fixation = fixations[r_ind]

            if stimulus.status == NOT_STARTED and \
                i == KEY_INDEX and \
                t > last_keypress_timestamp + wait_between_images:
                # we have pressed i-1 keys so we are viewing the i_th picture
                # we also wait for wait_between_images second before showing the next
                # keep track of start time/frame for later


                stimulus.frameNStart = frameN  # exact frame index
                stimulus.tStart = t  # local t and not account for scr refresh
                stimulus.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stimulus, 'tStartRefresh')  # time at next scr refresh
                stimulus.setAutoDraw(True)

            if stimulus.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if i != KEY_INDEX:
                    # keep track of stop time/frame for later
                    stimulus.tStop = t  # not accounting for scr refresh
                    stimulus.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stimulus, 'tStopRefresh')  # time at next scr refresh
                    stimulus.setAutoDraw(False)
                
                time_elapsed = t - stimulus.tStart


            # TEXT LOGIC

            if nominalization.status == NOT_STARTED and \
                i == KEY_INDEX and \
                t > last_keypress_timestamp + wait_between_images + \
                    text_after_image: 
                # keep track of start time/frame for later
                nominalization.frameNStart = frameN  # exact frame index
                nominalization.tStart = t  # local t and not account for scr refresh
                nominalization.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(nominalization, 'tStartRefresh')  # time at next scr refresh
                nominalization.setAutoDraw(True)

            if nominalization.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if i != KEY_INDEX:
                    # keep track of stop time/frame for later
                    nominalization.tStop = t  # not accounting for scr refresh
                    nominalization.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(nominalization, 'tStopRefresh')  # time at next scr refresh
                    nominalization.setAutoDraw(False)


            # FIXATION LOGIC
            if fixation.status == NOT_STARTED and \
                i == KEY_INDEX and \
                t > last_keypress_timestamp + wait_between_images: 
                # keep track of start time/frame for later
                fixation.frameNStart = frameN  # exact frame index
                fixation.tStart = t  # local t and not account for scr refresh
                fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
                fixation.setAutoDraw(True)

            if fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if t > fixation.tStart + text_after_image - 1/20:
                    # keep track of stop time/frame for later
                    fixation.tStop = t  # not accounting for scr refresh
                    fixation.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                    fixation.setAutoDraw(False)
                # fixation.ori = (frameN*8)%360

            # KEY LOGIC
            # logs STIMULUSkeys
            waitOnFlip = False
            if key_resp.status == NOT_STARTED and \
                i == KEY_INDEX and \
                t > last_keypress_timestamp + wait_between_images + \
                    text_after_image: 
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                key_resp.status = STARTED
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                

            if key_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if i != KEY_INDEX:
                    # keep track of stop time/frame for later
                    key_resp.tStop = t  # not accounting for scr refresh
                    key_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                    key_resp.status = FINISHED

            if key_resp.status == STARTED and not waitOnFlip:
                if t - key_resp.tStart <= press_time:
                    theseKeys = key_resp.getKeys(keyList=['x', 'o'], waitRelease=False)
                    if len(theseKeys):
                        theseKeys = theseKeys[0]  # at least one key was pressed
                        RETRY_KEYS += [theseKeys.name]
                        last_keypress_timestamp = t
                        if "escape" == theseKeys:
                            endExpNow = True
                        key_resp.keys.append(theseKeys.name)  # storing all keys
                        key_resp.rt.append(theseKeys.rt)
                else:
                    RETRY_KEYS += ['n']
                    key_resp.keys.append('n')
                    key_resp.rt.append(press_time)
                    last_keypress_timestamp = t

                
    ############# END SCREEN ################

    if is_test_stopped:

        screen = start_and_end[1]

        if screen.status == NOT_STARTED:
            # we have pressed i-1 keys so we are viewing the i_th picture
            # we also wait for wait_between_images second before showing the next
            screen.frameNStart = frameN  # exact frame index
            screen.tStart = t  # local t and not account for scr refresh
            screen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(screen, 'tStartRefresh')  # time at next scr refresh
            screen.setAutoDraw(True)

        if screen.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if len(start_and_end_keypresses[1].keys) != 0:
                # keep track of stop time/frame for later
                screen.tStop = t  # not accounting for scr refresh
                screen.frameNStop = frameN  # exact frame index
                win.timeOnFlip(screen, 'tStopRefresh')  # time at next scr refresh
                screen.setAutoDraw(False)
            

        waitOnFlip = False
        if start_and_end_keypresses[1].status == NOT_STARTED: 
            # keep track of start time/frame for later
            start_and_end_keypresses[1].frameNStart = frameN  # exact frame index
            start_and_end_keypresses[1].tStart = t  # local t and not account for scr refresh
            start_and_end_keypresses[1].tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(start_and_end_keypresses[1], 'tStartRefresh')  # time at next scr refresh
            start_and_end_keypresses[1].status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(start_and_end_keypresses[1].clock.reset)  # t=0 on next screen flip
            win.callOnFlip(start_and_end_keypresses[1].clearEvents, eventType='keyboard')  # clear events on next screen flip
            

        if start_and_end_keypresses[1].status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if len(start_and_end_keypresses[1].keys) != 0:
                # keep track of stop time/frame for later
                start_and_end_keypresses[1].tStop = t  # not accounting for scr refresh
                start_and_end_keypresses[1].frameNStop = frameN  # exact frame index
                win.timeOnFlip(start_and_end_keypresses[1], 'tStopRefresh')  # time at next scr refresh
                start_and_end_keypresses[1].status = FINISHED

        if start_and_end_keypresses[1].status == STARTED and not waitOnFlip:
            theseKeys = start_and_end_keypresses[1].getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                last_keypress_timestamp = t
                if "escape" == theseKeys:
                    endExpNow = True
                start_and_end_keypresses[1].keys.append(theseKeys.name)  # storing all keys
                start_and_end_keypresses[1].rt.append(theseKeys.rt)



    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        break

    # check if all components have finished
    if start_and_end[1].status == FINISHED: 
        break

    # refresh the screen
    win.flip()


# -------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

##########################################################################

        

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        #HACK core.quit()
        break

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break

    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

    
print([(x.keys, x.rt) for x in key_responses])
# Flip one final time so any remaining win.callOnFlip()
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
# thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit

win.winHandle.set_fullscreen(False)
win.winHandle.set_visible(False)

win.close()


# response_dialog_input = {'Megjegyzések, észrevételek:': '', 'Milyen stratégiát alkalmazott? \nAmennyiben módja van rá, kérem foglalja össze:': ''}
# response_dialog = gui.DlgFromDict(dictionary=response_dialog_input, sortKeys=False, title=expName)
# if dlg.OK is False:
#     core.quit()  # user pressed cancel

# print(response_dialog_input)
    

core.quit()
