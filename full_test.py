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

# reading datafile which will be used when creating iterable object

datafile = pd.read_csv('Zimmerer_materials_Banreti_agent_patient.csv')

images_l1, images_l2 = defaultdict(dict), defaultdict(dict)
sentences_l1, sentences_l2 = defaultdict(dict), defaultdict(dict)
role_per_stimulus = defaultdict(dict)

for line in datafile.values:
    num, picsent, plaus, title, l, imgname, sentence, nomin, nom1ap, nom2ap = line
    if l == 1:
        if picsent == 'pic':
            images_l1[num]['image'] = imgname
            images_l1[num]['desc_of_image'] = title
            images_l1[num]['plausibility'] = plaus
        #print(nomin, type(nomin))
        if picsent == 'sent':
            sentences_l1[num]['sentence'] = sentence
            sentences_l1[num]['plausibility'] = plaus

        
    if l == 2:    
        if picsent == 'pic':
            images_l2[num]['image'] = imgname
            images_l2[num]['desc_of_image'] = title
            images_l2[num]['plausibility'] = plaus
        if picsent == 'sent':
            sentences_l2[num]['sentence'] = sentence
            sentences_l2[num]['plausibility'] = plaus
        #print(nomin, type(nomin))
    
    if isinstance(nomin, str):
        images_l1[num]['nomin'] = nomin
        images_l2[num]['nomin'] = nomin
        sentences_l1[num]['nomin'] = nomin
        sentences_l2[num]['nomin'] = nomin

    if picsent == 'pic':
        stim = title
    elif picsent == 'sent':
        stim = sentence

    #print(nomin)
    
    nom1, nom2 = nomin.split('#')
    role_per_stimulus[stim][nom1] = nom1ap
    role_per_stimulus[stim][nom2] = nom2ap



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

if expInfo['list_name'] == '1':
    images_dict = images_l1
    sentences_dict = sentences_l1
else:
    images_dict = images_l2
    sentences_dict = sentences_l2

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


def create_imagestim(name, image_path, size=(0.85, 0.6)):
    image = visual.ImageStim(
        win=win,
        name=name,
        image=image_path, mask=None,
        ori=0, pos=(0, 0), size=size,
        color=[1, 1, 1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=0.0)

    return(image)


def create_textstim(name, text, pos=(0.7, 0.4), font = 'Noto Sans', size=0.05, color=(1.0, 1.0, 1.0)):
    text = visual.TextStim(
        alignHoriz='center',
        win=win,
        name=name,
        font=font,
        text=text,
        pos=pos,
        color = color,
        height=size,
        wrapWidth=1.4)

    return(text)

def shuffle_title(string, updown, leftright):
    # 1 is up and left, it says nom1's position, nom2 ios diagonal to that
    nom1, nom2 = string.split('#')
    if updown == 1 and leftright == 1:
        formatted_string = f"⅄: {nom1}\n{' '*len(nom1)*2}Ɔ: {nom2}"
    if updown == 0 and leftright == 1:
        formatted_string = f"{' '*len(nom1)*2}⅄: {nom2}\nƆ: {nom1}"
    if updown == 1 and leftright == 0:
        formatted_string = f"{' '*len(nom2)*2}⅄: {nom1}\nƆ: {nom2}"
    if updown == 0 and leftright == 0:
        formatted_string = f"⅄: {nom2}\n{' '*len(nom2)*2}Ɔ: {nom1}"
    
    return(formatted_string)


def create_contingency_tables(filename):
    table = pd.read_csv(filename)
    output = []
    output.append(pd.crosstab(table['stimulus_plaus'],table['answer_role'], margins = True, normalize='index'))
    table_sentence = table[(table['stimulus_type'] == 'sentence')]
    table_image = table[(table['stimulus_type'] == 'image')]
    output.append(pd.crosstab(table_sentence['stimulus_plaus'],table_sentence['answer_role'], margins = True))
    output.append(pd.crosstab(table_image['stimulus_plaus'],table_image['answer_role'], margins = True))
    output.append(pd.crosstab(table['key_resp.keys'],table['answer_role'], margins = True))
    output.append(pd.crosstab(table['nom1_indented'],table['key_resp.keys'], margins = True))
    output.append(pd.crosstab(table['nom2_indented'],table['key_resp.keys'], margins = True))
    output.append(pd.crosstab([table['stimulus_type'],table['stimulus_plaus']],table['answer_role'], margins = True))
    return(output)

base_order = sorted(list(images_dict.keys()))

#print(images_dict)
#print(sentences_dict)



random.seed(expInfo['random_seed'])
shuffle(base_order)

np.random.seed(expInfo['random_seed'])
_nom1order = np.random.randint(2, size=80)
np.random.seed(expInfo['random_seed'] + 1000)
_nom2order = np.random.randint(2, size=80)

nomin_orders = list(zip(_nom1order, _nom2order))



images = []
key_responses = []
directions = []
nominalizations = []
# helps = []
instructions = []

blocks_1 = [ 'image', 'sentence','sentence',   'image']
blocks_2 = [ 'image', 'sentence','sentence',   'image']
shuffle(blocks_1)
shuffle(blocks_2)
blocks = blocks_1 + blocks_2

#barefoot method
#print(base_order)
image_indices, sentence_indices = [], []

for i, block in enumerate(blocks_1):
    for j in range(i*10, (i+1) * 10):
        if block == 'image':
            image_indices += [base_order[j]]
        elif block == 'sentence':
            sentence_indices += [base_order[j]]
        else:
            print('something has gone wrong with blox')
            raise(BaseException)

#print(blocks)
#print(image_indices, '\n', sentence_indices)

second_order_random = []
for i, block in enumerate(blocks_2):
    for j in range(i*10, (i+1) * 10):
        if block == 'image':
            # we need to remove one from SENTENCE_INDICES
            index = random.choice(sentence_indices)
            second_order_random += [index]
            sentence_indices.remove(index)
        elif block == 'sentence':
            index = random.choice(image_indices)
            second_order_random += [index]
            image_indices.remove(index)
        else:
            print('something has gone wrong with blox')
            raise(BaseException)

#print(blocks_2)
#print(second_order_random)

final_order = base_order + second_order_random

# raise(BaseException)

fixations = []
stimuli = []
instruction_keypresses = []
start_and_end = []

nom_position = (8/9, -0.4)
# TODO hardcoded stuff
for iteration_index, i in enumerate(final_order[:40]):
    
    x_order, y_order = nomin_orders[iteration_index]
    #nominalizations += [create_textstim(f, 
    #                          , ), 
    #                          pos = , )]

    nominalizations += [visual.TextStim(
        alignHoriz='right',
        win=win,
        name="title_{i}",
        font='Noto Sans',
        text=shuffle_title(sentences_dict[i]['nomin'], x_order, y_order),
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

    current_block = blocks[iteration_index//10]
    if current_block == 'image':
        current_img_data = images_dict[i]
        cur_image = current_img_data['image']
        plaus = current_img_data['plausibility']
        cur_desc = current_img_data['desc_of_image']

        stimuli += [visual.ImageStim(
            win=win,
            name=f'image<>{i}<>{plaus}<>{cur_desc}',
            image=os.path.join('pictures', cur_image), mask=None,
            ori=0, pos=(0, 0), size=(0.85, 0.6),
            color=[1, 1, 1], colorSpace='rgb', opacity=1,
            flipHoriz=False, flipVert=False,
            texRes=128, interpolate=True, depth=0.0)]

        
    else:
        current_sent_data = sentences_dict[i]
        sentence = current_sent_data['sentence']
        plaus = current_sent_data['plausibility']
        # stimuli += [create_textstim(f'sentence<>{i}<>{plaus}<>{sentence}', sentence, pos=(0.0, 0), , size = 0.08)]


        stimuli += [visual.TextStim(
            alignHoriz='center',
            win=win,
            name=f'sentence<>{i}<>{plaus}<>{sentence}',
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

    if iteration_index%10 == 0 and blocks[iteration_index//10] == 'image':
        instructions += [visual.TextStim(
        alignHoriz='center',
        win=win,
        name=f'H{i}',
        font='Noto Sans',
        text='Ön a következőben képeket fog látni. A képernyő jobb alsó sarkában olvasható két felirat közül válassza ki azt, amelyik a legjobban kifejezi a kép lényegét.' + '\n' +
                'Nyomjon szóközt a továbbhaladáshoz.',
        pos=(0, 0),
        height=0.05,
        wrapWidth=1.3)]
        current_key = keyboard.Keyboard()
        current_key.keys = []
        current_key.rt = []
        instruction_keypresses += [current_key]

    if iteration_index%10 == 0 and blocks[iteration_index//10] == 'sentence':
        instructions += [visual.TextStim(
        alignHoriz='center',
        win=win,
        name=f'H{i}',
        font='Noto Sans',
        text='Ön a következőben mondatokat fog látni. A képernyő jobb alsó sarkában olvasható két felirat közül válassza ki azt, amelyik a legjobban kifejezi a mondat lényegét.' + '\n' +
                'Nyomjon szóközt a továbbhaladáshoz.',
        pos=(0, 0),
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
        text='Köszöntjük Budapesten, csodás ma az idő. Dőljön hátra, és élvezze a tesztet. Space.',
        pos=(0, 0),
        height=0.05,
        wrapWidth=1.3)]

start_and_end += [visual.TextStim(
        alignHoriz='center',
        win=win,
        name=f'H{i}',
        font='Noto Sans',
        text='Köszönjük, hogy minket választott. Reméljük élvezte utazását, kifelé menet ne felejtsen el csippantani a kártyájával. Szíves viszontlátását. Space.',
        pos=(0, 0),
        height=0.05,
        wrapWidth=1.3)] 



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
trialComponents = stimuli + key_responses + nominalizations + fixations + instructions + instruction_keypresses + start_and_end + start_and_end_keypresses
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

wait_between_images = 0.5 / 20
float_in_time = 3 / 20
text_after_image = 3 / 20
last_keypress_timestamp = -wait_between_images # to start slideshow at 0

DBG_end_of_last_image = -1

is_test_started = False
is_test_stopped = False

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
                print('stopped start image')
                print(f'{is_test_started} {is_test_stopped}')
            

        waitOnFlip = False
        if start_and_end_keypresses[0].status == NOT_STARTED: 
            
            print('start sequence started, logging keys')
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
                print(theseKeys.name)
                # print(theseKeys.name)
                # print(theseKeys.rt)
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                start_and_end_keypresses[0].keys.append(theseKeys.name)  # storing all keys
                start_and_end_keypresses[0].rt.append(theseKeys.rt)
        

    ############# END SCREEN ################

    if is_test_stopped:

        screen = start_and_end[1]

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
            if len(start_and_end_keypresses[1].keys) != 0:
                # keep track of stop time/frame for later
                screen.tStop = t  # not accounting for scr refresh
                screen.frameNStop = frameN  # exact frame index
                win.timeOnFlip(screen, 'tStopRefresh')  # time at next scr refresh
                screen.setAutoDraw(False)
                # print(f'stopping image {i}: {stimulus.tStop:.5f}')
            

        waitOnFlip = False
        if start_and_end_keypresses[1].status == NOT_STARTED: 
            
            # print(f'started key_inst {i} ## {i//10} ## {i%10} ## {KEY_INDEX} ## {INSTRUCTION_INDEX} ## {KEY_INDEX//10}')

            # keep track of start time/frame for later
            start_and_end_keypresses[1].frameNStart = frameN  # exact frame index
            start_and_end_keypresses[1].tStart = t  # local t and not account for scr refresh
            start_and_end_keypresses[1].tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(start_and_end_keypresses[1], 'tStartRefresh')  # time at next scr refresh
            start_and_end_keypresses[1].status = STARTED
            # keyboard checking is just starting
            # print(f"time when entered key {i}: {key_inst.tStart}")
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
                #print(key_responses)

        if start_and_end_keypresses[1].status == STARTED and not waitOnFlip:
            theseKeys = start_and_end_keypresses[1].getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                last_keypress_timestamp = t
                print(theseKeys.name)
                # print(theseKeys.name)
                # print(theseKeys.rt)
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                start_and_end_keypresses[1].keys.append(theseKeys.name)  # storing all keys
                start_and_end_keypresses[1].rt.append(theseKeys.rt)

    ############# MAIN CYCLE #################
    if is_test_started and not is_test_stopped:
        
        for i, stimulus in enumerate(stimuli):
            
            KEY_INDEX = len(LIST_OF_KEYS)
            key_resp = key_responses[i]
            nominalization = nominalizations[i]
            # help_text = helps[i]
            instruction = instructions[i//10]
            fixation = fixations[i]
            INSTRUCTION_INDEX = len(LIST_OF_INST_KEYS)
            key_inst = instruction_keypresses[i//10]


            # IMAGE LOGIC

            if stimulus.status == NOT_STARTED and \
                i == KEY_INDEX and \
                t > last_keypress_timestamp + wait_between_images and \
                INSTRUCTION_INDEX == i//10+1: 
                # we have pressed i-1 keys so we are viewing the i_th picture
                # we also wait for wait_between_images second before showing the next
                # keep track of start time/frame for later
                # print(f"LAST IMAGE ENDED {(t - DBG_end_of_last_image):.3f} s ago")

                stimulus.frameNStart = frameN  # exact frame index
                stimulus.tStart = t  # local t and not account for scr refresh
                stimulus.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stimulus, 'tStartRefresh')  # time at next scr refresh
                stimulus.setAutoDraw(True)
                # print(image.frameNStart)
                # print(f'Last keypress time: {last_keypress_timestamp:.5f}')
                # print(f'starting image {i}: {stimulus.tStart:.5f}')
                
                # print(image.frameNStart/image.tStart)

            if stimulus.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if i != KEY_INDEX:
                    # keep track of stop time/frame for later
                    stimulus.tStop = t  # not accounting for scr refresh
                    DBG_end_of_last_image = t
                    stimulus.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stimulus, 'tStopRefresh')  # time at next scr refresh
                    stimulus.setAutoDraw(False)
                    # print(f'stopping image {i}: {stimulus.tStop:.5f}')
                
                time_elapsed = t - stimulus.tStart
                if time_elapsed <= float_in_time:
                    if directions[i] == 'r':
                        stimulus.setPos([-2 + 2*time_elapsed*(1/float_in_time), 0])
                    else:
                        stimulus.setPos([2 - 2*time_elapsed*(1/float_in_time), 0])# shows images 
                    
                else:
                    stimulus.setPos([0, 0])


            # TEXT LOGIC

            if nominalization.status == NOT_STARTED and \
                i == KEY_INDEX and \
                t > last_keypress_timestamp + wait_between_images + \
                    float_in_time + text_after_image and \
                INSTRUCTION_INDEX == i//10+1: 
                # keep track of start time/frame for later
                nominalization.frameNStart = frameN  # exact frame index
                nominalization.tStart = t  # local t and not account for scr refresh
                nominalization.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(nominalization, 'tStartRefresh')  # time at next scr refresh
                nominalization.setAutoDraw(True)
                # print(text.frameNStart)
                # print(text.tStart)
                # print(text.frameNStart/text.tStart)

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
                t > last_keypress_timestamp + wait_between_images + float_in_time and \
                INSTRUCTION_INDEX == i//10+1: 
                # keep track of start time/frame for later
                fixation.frameNStart = frameN  # exact frame index
                fixation.tStart = t  # local t and not account for scr refresh
                fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
                fixation.setAutoDraw(True)
                # print(text.frameNStart)
                # print(text.tStart)
                # print(text.frameNStart/text.tStart)

            if fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if t > fixation.tStart + text_after_image - 1/20:
                    # keep track of stop time/frame for later
                    fixation.tStop = t  # not accounting for scr refresh
                    fixation.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                    fixation.setAutoDraw(False)
                # fixation.ori = (frameN*8)%360



            # HELP LOGIC
            # shown on the bottom of the screen
            # if help_text.status == NOT_STARTED and \
            #     i == KEY_INDEX and \
            #     t > last_keypress_timestamp + wait_between_images and \
            #     INSTRUCTION_INDEX == i//10+1: 
            #     # keep track of start time/frame for later
            #     help_text.frameNStart = frameN  # exact frame index
            #     help_text.tStart = t  # local t and not account for scr refresh
            #     help_text.tStartRefresh = tThisFlipGlobal  # on global time
            #     win.timeOnFlip(help_text, 'tStartRefresh')  # time at next scr refresh
            #     help_text.setAutoDraw(True)
            #     # print(help_text.frameNStart)
            #     # print(help_text.tStart)
            #     # print(help_text.frameNStart/help_text.tStart)

            # if help_text.status == STARTED:
            #     # is it time to stop? (based on global clock, using actual start)
            #     if i != KEY_INDEX:
            #         # keep track of stop time/frame for later
            #         help_text.tStop = t  # not accounting for scr refresh
            #         help_text.frameNStop = frameN  # exact frame index
            #         win.timeOnFlip(help_text, 'tStopRefresh')  # time at next scr refresh
            #         help_text.setAutoDraw(False)

            # KEY LOGIC
            # logs STIMULUSkeys
            waitOnFlip = False
            if key_resp.status == NOT_STARTED and \
                i == KEY_INDEX and \
                t > last_keypress_timestamp + wait_between_images + \
                    text_after_image + float_in_time and \
                INSTRUCTION_INDEX == i//10+1: 
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                key_resp.status = STARTED
                # keyboard checking is just starting
                # print(f"time when entered key {i}: {key_resp.tStart}")
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
                    #print(key_responses)

            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['x', 'o'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    LIST_OF_KEYS += [theseKeys.name]
                    last_keypress_timestamp = t
                    print(theseKeys.name)
                    # print(theseKeys.name)
                    # print(theseKeys.rt)
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    key_resp.keys.append(theseKeys.name)  # storing all keys
                    key_resp.rt.append(theseKeys.rt)

            #####################################################################
            # INSTRUCTIONS LOGIC
            # SHOWN BEFORE BLOX

            if instruction.status == NOT_STARTED and INSTRUCTION_INDEX == KEY_INDEX//10 and KEY_INDEX % 10 == 0 and INSTRUCTION_INDEX == i // 10 and \
                t > last_keypress_timestamp + 0.2:
                # print(f'started instruction {i}')
                # keep track of start time/frame for later
                instruction.frameNStart = frameN  # exact frame index
                instruction.tStart = t  # local t and not account for scr refresh
                instruction.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(instruction, 'tStartRefresh')  # time at next scr refresh
                instruction.setAutoDraw(True)
                # print(instruction.frameNStart)
                # print(instruction.tStart)
                # print(instruction.frameNStart/instruction.tStart)

            if instruction.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if INSTRUCTION_INDEX != i//10:
                    # keep track of stop time/frame for later
                    instruction.tStop = t  # not accounting for scr refresh
                    instruction.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(instruction, 'tStopRefresh')  # time at next scr refresh
                    instruction.setAutoDraw(False)

            waitOnFlip = False
            if key_inst.status == NOT_STARTED and INSTRUCTION_INDEX == KEY_INDEX//10 and KEY_INDEX % 10 == 0 and INSTRUCTION_INDEX == i // 10 and \
                t > last_keypress_timestamp + 0.2: 
                
                # print(f'started key_inst {i} ## {i//10} ## {i%10} ## {KEY_INDEX} ## {INSTRUCTION_INDEX} ## {KEY_INDEX//10}')

                # keep track of start time/frame for later
                key_inst.frameNStart = frameN  # exact frame index
                key_inst.tStart = t  # local t and not account for scr refresh
                key_inst.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_inst, 'tStartRefresh')  # time at next scr refresh
                key_inst.status = STARTED
                # keyboard checking is just starting
                # print(f"time when entered key {i}: {key_inst.tStart}")
                waitOnFlip = True
                win.callOnFlip(key_inst.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_inst.clearEvents, eventType='keyboard')  # clear events on next screen flip
                

            if key_inst.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if i//10 != INSTRUCTION_INDEX:
                    # keep track of stop time/frame for later
                    key_inst.tStop = t  # not accounting for scr refresh
                    key_inst.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_inst, 'tStopRefresh')  # time at next scr refresh
                    key_inst.status = FINISHED
                    #print(key_responses)

            if key_inst.status == STARTED and not waitOnFlip:
                theseKeys = key_inst.getKeys(keyList=['space'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    LIST_OF_INST_KEYS += [theseKeys.name]
                    last_keypress_timestamp = t
                    print(theseKeys.name)
                    # print(theseKeys.name)
                    # print(theseKeys.rt)
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    key_inst.keys.append(theseKeys.name)  # storing all keys
                    key_inst.rt.append(theseKeys.rt)

            if KEY_INDEX == len(stimuli):
                is_test_stopped = True

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

for key_resp, stimulus, orders, nom in zip(key_responses, stimuli, nomin_orders, nominalizations):

    #thisExp.addData('stimulus.name', )
    stim_type, id, plaus, stim_name = stimulus.name.split('<>')
    thisExp.addData('stimulus_name', stim_name)
    thisExp.addData('stimulus_type', stim_type)
    thisExp.addData('stimulus_id', id)
    thisExp.addData('stimulus_plaus', plaus)

    nom1, nom2 = nom.text.split('\n')
    thisExp.addData('nom_1_X', nom1.strip('⅄Ɔ: '))
    thisExp.addData('nom_2_O', nom2.strip('⅄Ɔ: '))

    if key_resp.keys is not None and key_resp.keys != []:  # No response was made
        thisExp.addData('key_resp.keys', key_resp.keys[0])

        if key_resp.keys[0] == 'x':
            answer = nom1.strip('⅄Ɔ: ')
        else:
            answer = nom2.strip('⅄Ɔ: ')
        
        thisExp.addData('answer', answer)
        thisExp.addData('answer_role', role_per_stimulus[stim_name][answer])


    if key_resp.rt != []:  # we had a response
        #print(key_resp.keys)
        thisExp.addData('key_resp.rt', key_resp.rt[0])

    
    if nom1[:2] == '  ':
        pos_1, pos_2 = 1, 0
    else:
        pos_1, pos_2 = 0, 1

    thisExp.addData('nom1_indented', pos_1)
    thisExp.addData('nom2_indented', pos_2)
    # thisExp.addData('key_resp.started', key_resp.tStartRefresh)
    # thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
    # thisExp.addData('image_shown', stimulus.name)


    thisExp.addData('stimulus.started', stimulus.tStartRefresh)
    thisExp.addData('stimulus.stopped', stimulus.tStopRefresh)
    thisExp.addData('list_name', expInfo['list_name'])
    thisExp.addData('random_seed', rand_seed)
    thisExp.nextEntry()
    


# Flip one final time so any remaining win.callOnFlip()
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
# thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
      
win.winHandle.set_fullscreen(False)
win.winHandle.set_visible(False)

win.close()

if len(LIST_OF_KEYS) == len(stimuli):
    print('doing stats')
    output_tables = create_contingency_tables(filename+'.csv')
    writer = pd.ExcelWriter(filename+'_statistics.xlsx')
    offset = 0
    for dataframe in output_tables:
        dataframe.to_excel(writer, "sheet1", index=True, startrow=offset)
        offset += len(dataframe) + 2
    writer.save()


response_dialog_input = {'Megjegyzések, észrevételek:': '', 'Milyen stratégiát alkalmazott? \nAmennyiben módja van rá, kérem foglalja össze:': ''}
response_dialog = gui.DlgFromDict(dictionary=response_dialog_input, sortKeys=False, title=expName)
if dlg.OK is False:
    core.quit()  # user pressed cancel

#print(response_dialog_input)

with open(filename + '_commentary.txt', 'w') as f:
    for key, value in sorted(list(response_dialog_input.items())):
        f.write(key + '\n' + value + '\n')
    

core.quit()
