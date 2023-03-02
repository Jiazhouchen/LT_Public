#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.2),
    on Wed Sep 28 14:21:50 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from setup_code
from numpy.random import uniform
from math import sqrt

tcount = 0;
ccount = 0;


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.2'
expName = 'LetterTask_SparseFeedback'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'ucl': '0',
    'skip': '0',
}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/jiazhouchen/Documents/NIMH-UCL/PyhtonCode/LT_SF/LT_SF_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1080], fullscr=False, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='norm')
win.mouseVisible = True
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "setup" ---

# --- Initialize components for Routine "inst" ---
upperMsg1 = visual.TextStim(win=win, name='upperMsg1',
    text='Welcome to the experiment. ',
    font='Arial',
    pos=(0, 0.80), height=0.08, wrapWidth=1.7, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
upperMsg2 = visual.TextStim(win=win, name='upperMsg2',
    text='On each trial, we will show you a few letters, for example: ',
    font='Arial',
    pos=(0, 0.65), height=0.065, wrapWidth=1.7, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
example1 = visual.TextStim(win=win, name='example1',
    text='X F A B',
    font='Arial',
    pos=(0, 0.50), height=0.15, wrapWidth=1.7, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
midMsg1 = visual.TextStim(win=win, name='midMsg1',
    text='Please order these letters alphabetically in your mind. In this case: ',
    font='Arial',
    pos=(0, 0.35), height=0.065, wrapWidth=2, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
example2 = visual.TextStim(win=win, name='example2',
    text='A B F X',
    font='Arial',
    pos=(0, 0.20), height=0.15, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
text = visual.TextStim(win=win, name='text',
    text="and remember this sequence of letters. \n\nWe will then show you one of the letters, and you should tell us at what alphabetical position that letter is. \n\nFor instance, if we show you 'B',  you should press the number 2 on your keyboard. If we show you 'X', you should press the number 4 on your keyboard. \n\nIn most trials, you will not receive feedback on whether your response was correct or not. \n\nOnce in a while, we will show you correct responses count and accuracy percentage. The count and percentage will reset after you see them. ",
    font='Arial',
    pos=(0, -0.25), height=0.065, wrapWidth=1.7, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
rightnext = visual.TextStim(win=win, name='rightnext',
    text='Right Arrow Key: Next Page ',
    font='Arial',
    pos=(0.65, -0.8), height=0.05, wrapWidth=1.5, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "Inst_2" ---
Msg1 = visual.TextStim(win=win, name='Msg1',
    text='You will earn the payment listed for this study. In addition, you will also earn “points” for each correct response. \n\nYou will win additional bonus payment based on the total points at the end of the study.',
    font='Arial',
    pos=(0, 0.40), height=0.065, wrapWidth=1.7, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Mag2 = visual.TextStim(win=win, name='Mag2',
    text='We will also ask you to rate how happy you are at the end of every trial. \n\nYou will provide your response by clicking on a scale using your mouse. \n\nWhen you are ready to start, press SPACE BAR to start.',
    font='Arial',
    pos=(0, -0.20), height=0.065, wrapWidth=1.7, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
left2 = visual.TextStim(win=win, name='left2',
    text='Left Arrow Key: Previous Page ',
    font='Arial',
    pos=(-0.65, -0.8), height=0.05, wrapWidth=1.5, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
right2 = visual.TextStim(win=win, name='right2',
    text='Space bar: Start the Study',
    font='Arial',
    pos=(0.65, -0.8), height=0.05, wrapWidth=1.5, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
key_resp_5 = keyboard.Keyboard()

# --- Initialize components for Routine "mood_rate" ---
ScaleMsgTop = visual.TextStim(win=win, name='ScaleMsgTop',
    text='Use the following scale to indicate your current mood:',
    font='Arial',
    pos=(0, 0.65), height=0.07, wrapWidth=1.5, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
ScaleMsgMain = visual.TextStim(win=win, name='ScaleMsgMain',
    text='How happy are you currently?',
    font='Arial',
    pos=(0, 0.4), height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
ScaleMsgSec = visual.TextStim(win=win, name='ScaleMsgSec',
    text='Use your mouse to select',
    font='Arial',
    pos=(0, 0.15), height=0.07, wrapWidth=1.5, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
slider = visual.Slider(win=win, name='slider',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.4), units=None,
    labels=["Unhappy","Happy"], ticks=(0,1, 2, 3, 4, 5,6,7,8,9,10), granularity=0.01,
    style=['rating'], styleTweaks=[], opacity=1,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='HelveticaBold', labelHeight=0.05,
    flip=False, ori=0, depth=-3, readOnly=False)

# --- Initialize components for Routine "fixation_cross" ---
fixation2 = visual.TextStim(win=win, name='fixation2',
    text='',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "trial" ---
preorder = visual.TextStim(win=win, name='preorder',
    text='',
    font='Arial',
    pos=(0, 0), height=0.35, wrapWidth=5, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
assist = visual.TextStim(win=win, name='assist',
    text='Alphabetize...',
    font='Arial',
    pos=(0, 0.7), height=0.05, wrapWidth=5, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
ISI_fix = visual.TextStim(win=win, name='ISI_fix',
    text='',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
letter = visual.TextStim(win=win, name='letter',
    text='',
    font='Arial',
    pos=(0, 0), height=0.4, wrapWidth=3, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
testMsgUpper = visual.TextStim(win=win, name='testMsgUpper',
    text='After alphabetization, what is the position of ...',
    font='Arial',
    pos=(0, 0.6), height=0.07, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
testMsgLower = visual.TextStim(win=win, name='testMsgLower',
    text='Use numeric key to make a response.',
    font='Arial',
    pos=(0, -0.6), height=0.07, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
TargetResp = keyboard.Keyboard()

# --- Initialize components for Routine "feedback" ---
polygon = visual.Rect(
    win=win, name='polygon',
    width=(1, 0.75)[0], height=(1, 0.75)[1],
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=-1.0, interpolate=True)
fb1 = visual.TextStim(win=win, name='fb1',
    text='',
    font='Arial',
    pos=[0,0], height=0.15, wrapWidth=1, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
rewTxt = visual.TextStim(win=win, name='rewTxt',
    text='',
    font='Arial',
    pos=(0, -0.15), height=0.15, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "fixation_cross" ---
fixation2 = visual.TextStim(win=win, name='fixation2',
    text='',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "mood_rate" ---
ScaleMsgTop = visual.TextStim(win=win, name='ScaleMsgTop',
    text='Use the following scale to indicate your current mood:',
    font='Arial',
    pos=(0, 0.65), height=0.07, wrapWidth=1.5, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
ScaleMsgMain = visual.TextStim(win=win, name='ScaleMsgMain',
    text='How happy are you currently?',
    font='Arial',
    pos=(0, 0.4), height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
ScaleMsgSec = visual.TextStim(win=win, name='ScaleMsgSec',
    text='Use your mouse to select',
    font='Arial',
    pos=(0, 0.15), height=0.07, wrapWidth=1.5, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
slider = visual.Slider(win=win, name='slider',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.4), units=None,
    labels=["Unhappy","Happy"], ticks=(0,1, 2, 3, 4, 5,6,7,8,9,10), granularity=0.01,
    style=['rating'], styleTweaks=[], opacity=1,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='HelveticaBold', labelHeight=0.05,
    flip=False, ori=0, depth=-3, readOnly=False)

# --- Initialize components for Routine "fixation_cross" ---
fixation2 = visual.TextStim(win=win, name='fixation2',
    text='',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "end_nih" ---
nih_endtext = visual.TextStim(win=win, name='nih_endtext',
    text='Thank you for your participation!\n\n\nYour completion code is: ',
    font='Arial',
    pos=(0, 0.5), height=0.1, wrapWidth=1.5, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
mt_code = visual.TextStim(win=win, name='mt_code',
    text='',
    font='Arialbd',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
nih_esp = keyboard.Keyboard()
nih_endtext2 = visual.TextStim(win=win, name='nih_endtext2',
    text='Please provide this code back to the MTurk page for completion credit. Come back here and press SPACE BAR to close the session after you provided the code.\n\nFailure to do so might result in forfeiting your compensation. ',
    font='Arial',
    pos=(0, -0.5), height=0.1, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "setup" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
setupComponents = []
for thisComponent in setupComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "setup" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "setup" ---
for thisComponent in setupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from setup_code
if expInfo['skip']=='1':
    inst_loop_n = 0
else: 
    inst_loop_n = 1

if expInfo['ucl']=='1':
    run_nih_consent = 0
else: 
    run_nih_consent = 1
# the Routine "setup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
rep_inst = data.TrialHandler(nReps=0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='rep_inst')
thisExp.addLoop(rep_inst)  # add the loop to the experiment
thisRep_inst = rep_inst.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRep_inst.rgb)
if thisRep_inst != None:
    for paramName in thisRep_inst:
        exec('{} = thisRep_inst[paramName]'.format(paramName))

for thisRep_inst in rep_inst:
    currentLoop = rep_inst
    # abbreviate parameter names if possible (e.g. rgb = thisRep_inst.rgb)
    if thisRep_inst != None:
        for paramName in thisRep_inst:
            exec('{} = thisRep_inst[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    page1 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='page1')
    thisExp.addLoop(page1)  # add the loop to the experiment
    thisPage1 = page1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPage1.rgb)
    if thisPage1 != None:
        for paramName in thisPage1:
            exec('{} = thisPage1[paramName]'.format(paramName))
    
    for thisPage1 in page1:
        currentLoop = page1
        # abbreviate parameter names if possible (e.g. rgb = thisPage1.rgb)
        if thisPage1 != None:
            for paramName in thisPage1:
                exec('{} = thisPage1[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "inst" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # keep track of which components have finished
        instComponents = [upperMsg1, upperMsg2, example1, midMsg1, example2, text, rightnext, key_resp]
        for thisComponent in instComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "inst" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *upperMsg1* updates
            if upperMsg1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                upperMsg1.frameNStart = frameN  # exact frame index
                upperMsg1.tStart = t  # local t and not account for scr refresh
                upperMsg1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(upperMsg1, 'tStartRefresh')  # time at next scr refresh
                upperMsg1.setAutoDraw(True)
            
            # *upperMsg2* updates
            if upperMsg2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                upperMsg2.frameNStart = frameN  # exact frame index
                upperMsg2.tStart = t  # local t and not account for scr refresh
                upperMsg2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(upperMsg2, 'tStartRefresh')  # time at next scr refresh
                upperMsg2.setAutoDraw(True)
            
            # *example1* updates
            if example1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                example1.frameNStart = frameN  # exact frame index
                example1.tStart = t  # local t and not account for scr refresh
                example1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(example1, 'tStartRefresh')  # time at next scr refresh
                example1.setAutoDraw(True)
            
            # *midMsg1* updates
            if midMsg1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                midMsg1.frameNStart = frameN  # exact frame index
                midMsg1.tStart = t  # local t and not account for scr refresh
                midMsg1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(midMsg1, 'tStartRefresh')  # time at next scr refresh
                midMsg1.setAutoDraw(True)
            
            # *example2* updates
            if example2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                example2.frameNStart = frameN  # exact frame index
                example2.tStart = t  # local t and not account for scr refresh
                example2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(example2, 'tStartRefresh')  # time at next scr refresh
                example2.setAutoDraw(True)
            
            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                text.setAutoDraw(True)
            
            # *rightnext* updates
            if rightnext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rightnext.frameNStart = frameN  # exact frame index
                rightnext.tStart = t  # local t and not account for scr refresh
                rightnext.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rightnext, 'tStartRefresh')  # time at next scr refresh
                rightnext.setAutoDraw(True)
            
            # *key_resp* updates
            waitOnFlip = False
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['right','esc'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in instComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "inst" ---
        for thisComponent in instComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "inst" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 1 repeats of 'page1'
    
    
    # set up handler to look after randomisation of conditions etc
    page2 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='page2')
    thisExp.addLoop(page2)  # add the loop to the experiment
    thisPage2 = page2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPage2.rgb)
    if thisPage2 != None:
        for paramName in thisPage2:
            exec('{} = thisPage2[paramName]'.format(paramName))
    
    for thisPage2 in page2:
        currentLoop = page2
        # abbreviate parameter names if possible (e.g. rgb = thisPage2.rgb)
        if thisPage2 != None:
            for paramName in thisPage2:
                exec('{} = thisPage2[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "Inst_2" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        key_resp_5.keys = []
        key_resp_5.rt = []
        _key_resp_5_allKeys = []
        # keep track of which components have finished
        Inst_2Components = [Msg1, Mag2, left2, right2, key_resp_5]
        for thisComponent in Inst_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Inst_2" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Msg1* updates
            if Msg1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Msg1.frameNStart = frameN  # exact frame index
                Msg1.tStart = t  # local t and not account for scr refresh
                Msg1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Msg1, 'tStartRefresh')  # time at next scr refresh
                Msg1.setAutoDraw(True)
            
            # *Mag2* updates
            if Mag2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Mag2.frameNStart = frameN  # exact frame index
                Mag2.tStart = t  # local t and not account for scr refresh
                Mag2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Mag2, 'tStartRefresh')  # time at next scr refresh
                Mag2.setAutoDraw(True)
            
            # *left2* updates
            if left2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                left2.frameNStart = frameN  # exact frame index
                left2.tStart = t  # local t and not account for scr refresh
                left2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(left2, 'tStartRefresh')  # time at next scr refresh
                left2.setAutoDraw(True)
            
            # *right2* updates
            if right2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                right2.frameNStart = frameN  # exact frame index
                right2.tStart = t  # local t and not account for scr refresh
                right2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(right2, 'tStartRefresh')  # time at next scr refresh
                right2.setAutoDraw(True)
            
            # *key_resp_5* updates
            waitOnFlip = False
            if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_5.frameNStart = frameN  # exact frame index
                key_resp_5.tStart = t  # local t and not account for scr refresh
                key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
                key_resp_5.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_5.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_5.getKeys(keyList=['left','space'], waitRelease=False)
                _key_resp_5_allKeys.extend(theseKeys)
                if len(_key_resp_5_allKeys):
                    key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                    key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                    # was this correct?
                    if (key_resp_5.keys == str('space')) or (key_resp_5.keys == 'space'):
                        key_resp_5.corr = 1
                    else:
                        key_resp_5.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Inst_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Inst_2" ---
        for thisComponent in Inst_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from code_6
        if key_resp_5.corr: 
            rep_inst.finished = True
        # the Routine "Inst_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 1 repeats of 'page2'
    
# completed 0 repeats of 'rep_inst'


# set up handler to look after randomisation of conditions etc
pre_trial_mood = data.TrialHandler(nReps=0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='pre_trial_mood')
thisExp.addLoop(pre_trial_mood)  # add the loop to the experiment
thisPre_trial_mood = pre_trial_mood.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPre_trial_mood.rgb)
if thisPre_trial_mood != None:
    for paramName in thisPre_trial_mood:
        exec('{} = thisPre_trial_mood[paramName]'.format(paramName))

for thisPre_trial_mood in pre_trial_mood:
    currentLoop = pre_trial_mood
    # abbreviate parameter names if possible (e.g. rgb = thisPre_trial_mood.rgb)
    if thisPre_trial_mood != None:
        for paramName in thisPre_trial_mood:
            exec('{} = thisPre_trial_mood[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "mood_rate" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    slider.reset()
    # keep track of which components have finished
    mood_rateComponents = [ScaleMsgTop, ScaleMsgMain, ScaleMsgSec, slider]
    for thisComponent in mood_rateComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "mood_rate" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ScaleMsgTop* updates
        if ScaleMsgTop.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ScaleMsgTop.frameNStart = frameN  # exact frame index
            ScaleMsgTop.tStart = t  # local t and not account for scr refresh
            ScaleMsgTop.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ScaleMsgTop, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ScaleMsgTop.started')
            ScaleMsgTop.setAutoDraw(True)
        
        # *ScaleMsgMain* updates
        if ScaleMsgMain.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ScaleMsgMain.frameNStart = frameN  # exact frame index
            ScaleMsgMain.tStart = t  # local t and not account for scr refresh
            ScaleMsgMain.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ScaleMsgMain, 'tStartRefresh')  # time at next scr refresh
            ScaleMsgMain.setAutoDraw(True)
        
        # *ScaleMsgSec* updates
        if ScaleMsgSec.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ScaleMsgSec.frameNStart = frameN  # exact frame index
            ScaleMsgSec.tStart = t  # local t and not account for scr refresh
            ScaleMsgSec.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ScaleMsgSec, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ScaleMsgSec.started')
            ScaleMsgSec.setAutoDraw(True)
        
        # *slider* updates
        if slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider.frameNStart = frameN  # exact frame index
            slider.tStart = t  # local t and not account for scr refresh
            slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'slider.started')
            slider.setAutoDraw(True)
        
        # Check slider for response to end routine
        if slider.getRating() is not None and slider.status == STARTED:
            continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mood_rateComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "mood_rate" ---
    for thisComponent in mood_rateComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    pre_trial_mood.addData('slider.response', slider.getRating())
    pre_trial_mood.addData('slider.rt', slider.getRT())
    # the Routine "mood_rate" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "fixation_cross" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from ITI_code
    dur_fixcross = uniform(0.3,1)
    thisExp.addData('ITI', dur_fixcross)
    # keep track of which components have finished
    fixation_crossComponents = [fixation2]
    for thisComponent in fixation_crossComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "fixation_cross" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation2* updates
        if fixation2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation2.frameNStart = frameN  # exact frame index
            fixation2.tStart = t  # local t and not account for scr refresh
            fixation2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation2.started')
            fixation2.setAutoDraw(True)
        if fixation2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation2.tStartRefresh + dur_fixcross-frameTolerance:
                # keep track of stop time/frame for later
                fixation2.tStop = t  # not accounting for scr refresh
                fixation2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation2.stopped')
                fixation2.setAutoDraw(False)
        if fixation2.status == STARTED:  # only update if drawing
            fixation2.setText('+', log=False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixation_crossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "fixation_cross" ---
    for thisComponent in fixation_crossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "fixation_cross" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 0 repeats of 'pre_trial_mood'

# get names of stimulus parameters
if pre_trial_mood.trialList in ([], [None], None):
    params = []
else:
    params = pre_trial_mood.trialList[0].keys()
# save data for this loop
pre_trial_mood.saveAsText(filename + 'pre_trial_mood.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('contingency_SR.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_2
    t_isi = uniform(0.5,0.8)
    encoding_t = sqrt(N);
    choice_t = 3;
    fb_t = 1
    thisExp.addData('ISI', t_isi)
    preorder.setText(list_og)
    ISI_fix.setText('+')
    letter.setText(target_letter)
    TargetResp.keys = []
    TargetResp.rt = []
    _TargetResp_allKeys = []
    # keep track of which components have finished
    trialComponents = [preorder, assist, ISI_fix, letter, testMsgUpper, testMsgLower, TargetResp]
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
    frameN = -1
    
    # --- Run Routine "trial" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *preorder* updates
        if preorder.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            preorder.frameNStart = frameN  # exact frame index
            preorder.tStart = t  # local t and not account for scr refresh
            preorder.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(preorder, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'preorder.started')
            preorder.setAutoDraw(True)
        if preorder.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > preorder.tStartRefresh + encoding_t-frameTolerance:
                # keep track of stop time/frame for later
                preorder.tStop = t  # not accounting for scr refresh
                preorder.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'preorder.stopped')
                preorder.setAutoDraw(False)
        
        # *assist* updates
        if assist.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            assist.frameNStart = frameN  # exact frame index
            assist.tStart = t  # local t and not account for scr refresh
            assist.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(assist, 'tStartRefresh')  # time at next scr refresh
            assist.setAutoDraw(True)
        if assist.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > assist.tStartRefresh + encoding_t-frameTolerance:
                # keep track of stop time/frame for later
                assist.tStop = t  # not accounting for scr refresh
                assist.frameNStop = frameN  # exact frame index
                assist.setAutoDraw(False)
        
        # *ISI_fix* updates
        if ISI_fix.status == NOT_STARTED and tThisFlip >= encoding_t-frameTolerance:
            # keep track of start time/frame for later
            ISI_fix.frameNStart = frameN  # exact frame index
            ISI_fix.tStart = t  # local t and not account for scr refresh
            ISI_fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI_fix, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ISI_fix.started')
            ISI_fix.setAutoDraw(True)
        if ISI_fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ISI_fix.tStartRefresh + t_isi-frameTolerance:
                # keep track of stop time/frame for later
                ISI_fix.tStop = t  # not accounting for scr refresh
                ISI_fix.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ISI_fix.stopped')
                ISI_fix.setAutoDraw(False)
        
        # *letter* updates
        if letter.status == NOT_STARTED and tThisFlip >= encoding_t +t_isi-frameTolerance:
            # keep track of start time/frame for later
            letter.frameNStart = frameN  # exact frame index
            letter.tStart = t  # local t and not account for scr refresh
            letter.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letter, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'letter.started')
            letter.setAutoDraw(True)
        if letter.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > letter.tStartRefresh + choice_t-frameTolerance:
                # keep track of stop time/frame for later
                letter.tStop = t  # not accounting for scr refresh
                letter.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'letter.stopped')
                letter.setAutoDraw(False)
        
        # *testMsgUpper* updates
        if testMsgUpper.status == NOT_STARTED and tThisFlip >= encoding_t +t_isi-frameTolerance:
            # keep track of start time/frame for later
            testMsgUpper.frameNStart = frameN  # exact frame index
            testMsgUpper.tStart = t  # local t and not account for scr refresh
            testMsgUpper.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(testMsgUpper, 'tStartRefresh')  # time at next scr refresh
            testMsgUpper.setAutoDraw(True)
        if testMsgUpper.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > testMsgUpper.tStartRefresh + choice_t-frameTolerance:
                # keep track of stop time/frame for later
                testMsgUpper.tStop = t  # not accounting for scr refresh
                testMsgUpper.frameNStop = frameN  # exact frame index
                testMsgUpper.setAutoDraw(False)
        
        # *testMsgLower* updates
        if testMsgLower.status == NOT_STARTED and tThisFlip >= encoding_t+t_isi-frameTolerance:
            # keep track of start time/frame for later
            testMsgLower.frameNStart = frameN  # exact frame index
            testMsgLower.tStart = t  # local t and not account for scr refresh
            testMsgLower.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(testMsgLower, 'tStartRefresh')  # time at next scr refresh
            testMsgLower.setAutoDraw(True)
        if testMsgLower.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > testMsgLower.tStartRefresh + choice_t-frameTolerance:
                # keep track of stop time/frame for later
                testMsgLower.tStop = t  # not accounting for scr refresh
                testMsgLower.frameNStop = frameN  # exact frame index
                testMsgLower.setAutoDraw(False)
        
        # *TargetResp* updates
        waitOnFlip = False
        if TargetResp.status == NOT_STARTED and tThisFlip >= encoding_t+t_isi-frameTolerance:
            # keep track of start time/frame for later
            TargetResp.frameNStart = frameN  # exact frame index
            TargetResp.tStart = t  # local t and not account for scr refresh
            TargetResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TargetResp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TargetResp.started')
            TargetResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(TargetResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(TargetResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if TargetResp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > TargetResp.tStartRefresh + choice_t-frameTolerance:
                # keep track of stop time/frame for later
                TargetResp.tStop = t  # not accounting for scr refresh
                TargetResp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TargetResp.stopped')
                TargetResp.status = FINISHED
        if TargetResp.status == STARTED and not waitOnFlip:
            theseKeys = TargetResp.getKeys(keyList=['1','2','3','4','5','6','7','8','9'], waitRelease=False)
            _TargetResp_allKeys.extend(theseKeys)
            if len(_TargetResp_allKeys):
                TargetResp.keys = _TargetResp_allKeys[0].name  # just the first key pressed
                TargetResp.rt = _TargetResp_allKeys[0].rt
                # was this correct?
                if (TargetResp.keys == str(cor_pos)) or (TargetResp.keys == cor_pos):
                    TargetResp.corr = 1
                else:
                    TargetResp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial" ---
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_2
    tcount = tcount+1;
    if TargetResp.corr:
        ccount = ccount + 1;
        
    # check responses
    if TargetResp.keys in ['', [], None]:  # No response was made
        TargetResp.keys = None
        # was no response the correct answer?!
        if str(cor_pos).lower() == 'none':
           TargetResp.corr = 1;  # correct non-response
        else:
           TargetResp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('TargetResp.keys',TargetResp.keys)
    trials.addData('TargetResp.corr', TargetResp.corr)
    if TargetResp.keys != None:  # we had a response
        trials.addData('TargetResp.rt', TargetResp.rt)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    fb_logical = data.TrialHandler(nReps=fb_yn, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='fb_logical')
    thisExp.addLoop(fb_logical)  # add the loop to the experiment
    thisFb_logical = fb_logical.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFb_logical.rgb)
    if thisFb_logical != None:
        for paramName in thisFb_logical:
            exec('{} = thisFb_logical[paramName]'.format(paramName))
    
    for thisFb_logical in fb_logical:
        currentLoop = fb_logical
        # abbreviate parameter names if possible (e.g. rgb = thisFb_logical.rgb)
        if thisFb_logical != None:
            for paramName in thisFb_logical:
                exec('{} = thisFb_logical[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "feedback" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code
        rewPer = round((ccount / tcount)*100,1)
        if rewPer > 80:
            fbColor = [0.65,0.8118,0.545];
        else:
            fbColor = [0.8667,0.5137,0.513725];
        rewPer = str(rewPer)
        ccount = str(ccount)
        tcount = str(tcount)
        polygon.setFillColor(fbColor)
        polygon.setLineColor([1,1,1])
        fb1.setPos([0,0.13])
        fb1.setText('You got ' + ccount + ' / ' + tcount +' correct.' )
        rewTxt.setText('Your accuracy rate is ' + rewPer + '%')
        # keep track of which components have finished
        feedbackComponents = [polygon, fb1, rewTxt]
        for thisComponent in feedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "feedback" ---
        while continueRoutine and routineTimer.getTime() < 4.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *polygon* updates
            if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon.frameNStart = frameN  # exact frame index
                polygon.tStart = t  # local t and not account for scr refresh
                polygon.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon.started')
                polygon.setAutoDraw(True)
            if polygon.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon.tStop = t  # not accounting for scr refresh
                    polygon.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon.stopped')
                    polygon.setAutoDraw(False)
            
            # *fb1* updates
            if fb1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fb1.frameNStart = frameN  # exact frame index
                fb1.tStart = t  # local t and not account for scr refresh
                fb1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fb1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fb1.started')
                fb1.setAutoDraw(True)
            if fb1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fb1.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    fb1.tStop = t  # not accounting for scr refresh
                    fb1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fb1.stopped')
                    fb1.setAutoDraw(False)
            
            # *rewTxt* updates
            if rewTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rewTxt.frameNStart = frameN  # exact frame index
                rewTxt.tStart = t  # local t and not account for scr refresh
                rewTxt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rewTxt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'rewTxt.started')
                rewTxt.setAutoDraw(True)
            if rewTxt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rewTxt.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    rewTxt.tStop = t  # not accounting for scr refresh
                    rewTxt.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'rewTxt.stopped')
                    rewTxt.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback" ---
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from code
        tcount=0;
        ccount=0;
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-4.000000)
        thisExp.nextEntry()
        
    # completed fb_yn repeats of 'fb_logical'
    
    # get names of stimulus parameters
    if fb_logical.trialList in ([], [None], None):
        params = []
    else:
        params = fb_logical.trialList[0].keys()
    # save data for this loop
    fb_logical.saveAsText(filename + 'fb_logical.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # --- Prepare to start Routine "fixation_cross" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from ITI_code
    dur_fixcross = uniform(0.3,1)
    thisExp.addData('ITI', dur_fixcross)
    # keep track of which components have finished
    fixation_crossComponents = [fixation2]
    for thisComponent in fixation_crossComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "fixation_cross" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation2* updates
        if fixation2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation2.frameNStart = frameN  # exact frame index
            fixation2.tStart = t  # local t and not account for scr refresh
            fixation2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation2.started')
            fixation2.setAutoDraw(True)
        if fixation2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation2.tStartRefresh + dur_fixcross-frameTolerance:
                # keep track of stop time/frame for later
                fixation2.tStop = t  # not accounting for scr refresh
                fixation2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation2.stopped')
                fixation2.setAutoDraw(False)
        if fixation2.status == STARTED:  # only update if drawing
            fixation2.setText('+', log=False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixation_crossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "fixation_cross" ---
    for thisComponent in fixation_crossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "fixation_cross" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "mood_rate" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    slider.reset()
    # keep track of which components have finished
    mood_rateComponents = [ScaleMsgTop, ScaleMsgMain, ScaleMsgSec, slider]
    for thisComponent in mood_rateComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "mood_rate" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ScaleMsgTop* updates
        if ScaleMsgTop.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ScaleMsgTop.frameNStart = frameN  # exact frame index
            ScaleMsgTop.tStart = t  # local t and not account for scr refresh
            ScaleMsgTop.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ScaleMsgTop, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ScaleMsgTop.started')
            ScaleMsgTop.setAutoDraw(True)
        
        # *ScaleMsgMain* updates
        if ScaleMsgMain.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ScaleMsgMain.frameNStart = frameN  # exact frame index
            ScaleMsgMain.tStart = t  # local t and not account for scr refresh
            ScaleMsgMain.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ScaleMsgMain, 'tStartRefresh')  # time at next scr refresh
            ScaleMsgMain.setAutoDraw(True)
        
        # *ScaleMsgSec* updates
        if ScaleMsgSec.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ScaleMsgSec.frameNStart = frameN  # exact frame index
            ScaleMsgSec.tStart = t  # local t and not account for scr refresh
            ScaleMsgSec.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ScaleMsgSec, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ScaleMsgSec.started')
            ScaleMsgSec.setAutoDraw(True)
        
        # *slider* updates
        if slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider.frameNStart = frameN  # exact frame index
            slider.tStart = t  # local t and not account for scr refresh
            slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'slider.started')
            slider.setAutoDraw(True)
        
        # Check slider for response to end routine
        if slider.getRating() is not None and slider.status == STARTED:
            continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mood_rateComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "mood_rate" ---
    for thisComponent in mood_rateComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('slider.response', slider.getRating())
    trials.addData('slider.rt', slider.getRT())
    # the Routine "mood_rate" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "fixation_cross" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from ITI_code
    dur_fixcross = uniform(0.3,1)
    thisExp.addData('ITI', dur_fixcross)
    # keep track of which components have finished
    fixation_crossComponents = [fixation2]
    for thisComponent in fixation_crossComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "fixation_cross" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation2* updates
        if fixation2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation2.frameNStart = frameN  # exact frame index
            fixation2.tStart = t  # local t and not account for scr refresh
            fixation2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation2.started')
            fixation2.setAutoDraw(True)
        if fixation2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation2.tStartRefresh + dur_fixcross-frameTolerance:
                # keep track of stop time/frame for later
                fixation2.tStop = t  # not accounting for scr refresh
                fixation2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation2.stopped')
                fixation2.setAutoDraw(False)
        if fixation2.status == STARTED:  # only update if drawing
            fixation2.setText('+', log=False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixation_crossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "fixation_cross" ---
    for thisComponent in fixation_crossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "fixation_cross" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsText(filename + 'trials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
nih_end = data.TrialHandler(nReps=1, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('code.csv'),
    seed=None, name='nih_end')
thisExp.addLoop(nih_end)  # add the loop to the experiment
thisNih_end = nih_end.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNih_end.rgb)
if thisNih_end != None:
    for paramName in thisNih_end:
        exec('{} = thisNih_end[paramName]'.format(paramName))

for thisNih_end in nih_end:
    currentLoop = nih_end
    # abbreviate parameter names if possible (e.g. rgb = thisNih_end.rgb)
    if thisNih_end != None:
        for paramName in thisNih_end:
            exec('{} = thisNih_end[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "end_nih" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    mt_code.setText(passcode)
    nih_esp.keys = []
    nih_esp.rt = []
    _nih_esp_allKeys = []
    # keep track of which components have finished
    end_nihComponents = [nih_endtext, mt_code, nih_esp, nih_endtext2]
    for thisComponent in end_nihComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "end_nih" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *nih_endtext* updates
        if nih_endtext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            nih_endtext.frameNStart = frameN  # exact frame index
            nih_endtext.tStart = t  # local t and not account for scr refresh
            nih_endtext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nih_endtext, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'nih_endtext.started')
            nih_endtext.setAutoDraw(True)
        
        # *mt_code* updates
        if mt_code.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mt_code.frameNStart = frameN  # exact frame index
            mt_code.tStart = t  # local t and not account for scr refresh
            mt_code.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mt_code, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'mt_code.started')
            mt_code.setAutoDraw(True)
        
        # *nih_esp* updates
        waitOnFlip = False
        if nih_esp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            nih_esp.frameNStart = frameN  # exact frame index
            nih_esp.tStart = t  # local t and not account for scr refresh
            nih_esp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nih_esp, 'tStartRefresh')  # time at next scr refresh
            nih_esp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(nih_esp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(nih_esp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if nih_esp.status == STARTED and not waitOnFlip:
            theseKeys = nih_esp.getKeys(keyList=['space'], waitRelease=False)
            _nih_esp_allKeys.extend(theseKeys)
            if len(_nih_esp_allKeys):
                nih_esp.keys = _nih_esp_allKeys[-1].name  # just the last key pressed
                nih_esp.rt = _nih_esp_allKeys[-1].rt
                # was this correct?
                if (nih_esp.keys == str('space')) or (nih_esp.keys == 'space'):
                    nih_esp.corr = 1
                else:
                    nih_esp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *nih_endtext2* updates
        if nih_endtext2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            nih_endtext2.frameNStart = frameN  # exact frame index
            nih_endtext2.tStart = t  # local t and not account for scr refresh
            nih_endtext2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nih_endtext2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'nih_endtext2.started')
            nih_endtext2.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end_nihComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "end_nih" ---
    for thisComponent in end_nihComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_7
    if nih_esp.corr: 
        nih_end.finished = True
    thisExp.addData('verify_ID', ID);
    # the Routine "end_nih" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'nih_end'

# get names of stimulus parameters
if nih_end.trialList in ([], [None], None):
    params = []
else:
    params = nih_end.trialList[0].keys()
# save data for this loop
nih_end.saveAsText(filename + 'nih_end.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='comma')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
