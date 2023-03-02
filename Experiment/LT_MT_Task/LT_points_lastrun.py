#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.10),
    on Mon May 10 20:36:16 2021
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
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

from numpy.random import uniform
from math import sqrt
con_file = "".join(["conditionsheets/contingency_",str(randint(1,100)),".csv"])


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.10'
expName = 'LetterTask_subpts'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001', 'ucl': '0', 'skip': '0', 'study_id': '', 'ver_control': ''}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/jiazhouchen/Documents/NIMH-UCL/PyhtonCode/LT_points/LT_points_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='norm')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "setup"
setupClock = core.Clock()

# Initialize components for Routine "inst"
instClock = core.Clock()
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
    text="and remember this sequence of letters. \n\nWe will then show you one of the letters, and you should tell us at what alphabetical position that letter is. \n\nFor instance, if we show you 'B',  you should press the number 2 on your keyboard. If we show you 'X', you should press the number 4 on your keyboard. \n\nIf you respond correctly, you will advance to the next sequence. However, if incorrect response is made, you will be asked to repeat the same sequence again. You will repeat until a correct response is made. ",
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

# Initialize components for Routine "Inst_2"
Inst_2Clock = core.Clock()
Msg1 = visual.TextStim(win=win, name='Msg1',
    text='You will earn the payment listed for this study. In addition, you will also earn “points” for each sequence. \n\nFor each sequence, you will start with some points and you will lose 10 points for every incorrect attempt. \n\nYou will earn the points that’s left when you made a correct response. However, your earnable points will NOT go below 0. That is, you will either earn some points or nothing for each sequnce, never negative points. \n\nYou will win additional bonus payment based on the total points at the end of the study.',
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

# Initialize components for Routine "mood_rate"
mood_rateClock = core.Clock()
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
    size=(1.0, 0.1), pos=(0, -0.4), units=None,
    labels=["Unhappy","Happy"], ticks=(0,1, 2, 3, 4, 5,6,7,8,9,10),
    granularity=0.01, style=['rating'],
    color='LightGray', font='HelveticaBold',
    flip=False, depth=-3)

# Initialize components for Routine "fixation_cross"
fixation_crossClock = core.Clock()
fixation2 = visual.TextStim(win=win, name='fixation2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "new_sequence_alert"
new_sequence_alertClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='A new sequence is coming up',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=1.5, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "reward_t_info"
reward_t_infoClock = core.Clock()
rew_tx1 = visual.TextStim(win=win, name='rew_tx1',
    text='You have ',
    font='Arial',
    pos=(0, 0.3), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
rew_main = visual.TextStim(win=win, name='rew_main',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text='remaining for this sequence',
    font='Arial',
    pos=(0, -0.3), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
preorder = visual.TextStim(win=win, name='preorder',
    text='default text',
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
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
letter = visual.TextStim(win=win, name='letter',
    text='default text',
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

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
polygon = visual.Rect(
    win=win, name='polygon',
    width=(0.8, 0.65)[0], height=(0.8, 0.65)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
fb1 = visual.TextStim(win=win, name='fb1',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.15, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
rewTxt = visual.TextStim(win=win, name='rewTxt',
    text='default text',
    font='Arial',
    pos=(0, -0.15), height=0.25, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "fixation_cross"
fixation_crossClock = core.Clock()
fixation2 = visual.TextStim(win=win, name='fixation2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "mood_rate"
mood_rateClock = core.Clock()
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
    size=(1.0, 0.1), pos=(0, -0.4), units=None,
    labels=["Unhappy","Happy"], ticks=(0,1, 2, 3, 4, 5,6,7,8,9,10),
    granularity=0.01, style=['rating'],
    color='LightGray', font='HelveticaBold',
    flip=False, depth=-3)

# Initialize components for Routine "fixation_cross"
fixation_crossClock = core.Clock()
fixation2 = visual.TextStim(win=win, name='fixation2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "end_nih"
end_nihClock = core.Clock()
nih_endtext = visual.TextStim(win=win, name='nih_endtext',
    text='Thank you for your participation!\n\n\nYour completion code is: \n\n3YTZRJZ_00356\n\nPlease enter this code to the MTurk page for validation.\n\nYou may keep this page open while type in the code in the MTurk page. \n\nAlternatively, you can press SPACE BAR and a message will pop up to allow you to copy this code, and you may paste it there. \n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.5, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
nih_esp = keyboard.Keyboard()

# Initialize components for Routine "end"
endClock = core.Clock()
ending_text = visual.TextStim(win=win, name='ending_text',
    text='Thank you for your participation!\n\nPress space bar to close the experiment. You will be redirected to get your compensation. ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "setup"-------
continueRoutine = True
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
setupClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "setup"-------
while continueRoutine:
    # get current time
    t = setupClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=setupClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "setup"-------
for thisComponent in setupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
if expInfo['skip']=='1':
    inst_loop_n = 0
else: 
    inst_loop_n = 1

if expInfo['ucl']=='1':
    run_nih_consent = 0
else: 
    run_nih_consent = 1

thisExp.addData('ver_control', expInfo['ver_control'])
# the Routine "setup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
rep_inst = data.TrialHandler(nReps=999, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditionsheets/inst.csv'),
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
    trials_2 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_2')
    thisExp.addLoop(trials_2)  # add the loop to the experiment
    thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    for thisTrial_2 in trials_2:
        currentLoop = trials_2
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                exec('{} = thisTrial_2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "inst"-------
        continueRoutine = True
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
        instClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "inst"-------
        while continueRoutine:
            # get current time
            t = instClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=instClock)
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
                theseKeys = key_resp.getKeys(keyList=['right', 'esc'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in instComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "inst"-------
        for thisComponent in instComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "inst" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 1 repeats of 'trials_2'
    
    
    # set up handler to look after randomisation of conditions etc
    trials_3 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_3')
    thisExp.addLoop(trials_3)  # add the loop to the experiment
    thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    for thisTrial_3 in trials_3:
        currentLoop = trials_3
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
        if thisTrial_3 != None:
            for paramName in thisTrial_3:
                exec('{} = thisTrial_3[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Inst_2"-------
        continueRoutine = True
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
        Inst_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Inst_2"-------
        while continueRoutine:
            # get current time
            t = Inst_2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Inst_2Clock)
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
                theseKeys = key_resp_5.getKeys(keyList=['left', 'space'], waitRelease=False)
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
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Inst_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Inst_2"-------
        for thisComponent in Inst_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        if key_resp_5.corr: 
            rep_inst.finished = True
        # the Routine "Inst_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 1 repeats of 'trials_3'
    
# completed 999 repeats of 'rep_inst'


# set up handler to look after randomisation of conditions etc
pre_trial_mood = data.TrialHandler(nReps=1, method='sequential', 
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
    
    # ------Prepare to start Routine "mood_rate"-------
    continueRoutine = True
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
    mood_rateClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "mood_rate"-------
    while continueRoutine:
        # get current time
        t = mood_rateClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=mood_rateClock)
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
            ScaleMsgSec.setAutoDraw(True)
        
        # *slider* updates
        if slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider.frameNStart = frameN  # exact frame index
            slider.tStart = t  # local t and not account for scr refresh
            slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
            slider.setAutoDraw(True)
        
        # Check slider for response to end routine
        if slider.getRating() is not None and slider.status == STARTED:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mood_rateComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "mood_rate"-------
    for thisComponent in mood_rateComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    pre_trial_mood.addData('ScaleMsgTop.started', ScaleMsgTop.tStartRefresh)
    pre_trial_mood.addData('ScaleMsgTop.stopped', ScaleMsgTop.tStopRefresh)
    pre_trial_mood.addData('ScaleMsgSec.started', ScaleMsgSec.tStartRefresh)
    pre_trial_mood.addData('ScaleMsgSec.stopped', ScaleMsgSec.tStopRefresh)
    pre_trial_mood.addData('slider.response', slider.getRating())
    pre_trial_mood.addData('slider.rt', slider.getRT())
    pre_trial_mood.addData('slider.started', slider.tStartRefresh)
    pre_trial_mood.addData('slider.stopped', slider.tStopRefresh)
    # the Routine "mood_rate" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "fixation_cross"-------
    continueRoutine = True
    # update component parameters for each repeat
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
    fixation_crossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fixation_cross"-------
    while continueRoutine:
        # get current time
        t = fixation_crossClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixation_crossClock)
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
            fixation2.setAutoDraw(True)
        if fixation2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation2.tStartRefresh + dur_fixcross-frameTolerance:
                # keep track of stop time/frame for later
                fixation2.tStop = t  # not accounting for scr refresh
                fixation2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation2, 'tStopRefresh')  # time at next scr refresh
                fixation2.setAutoDraw(False)
        if fixation2.status == STARTED:  # only update if drawing
            fixation2.setText('+')
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixation_crossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation_cross"-------
    for thisComponent in fixation_crossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    pre_trial_mood.addData('fixation2.started', fixation2.tStartRefresh)
    pre_trial_mood.addData('fixation2.stopped', fixation2.tStopRefresh)
    # the Routine "fixation_cross" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'pre_trial_mood'

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
    trialList=data.importConditions(con_file),
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
    
    # ------Prepare to start Routine "new_sequence_alert"-------
    continueRoutine = True
    routineTimer.add(1.200000)
    # update component parameters for each repeat
    rewPts = int("".join(filter(str.isdigit, rewMag)))
    p_change = 0;
    # keep track of which components have finished
    new_sequence_alertComponents = [text_3]
    for thisComponent in new_sequence_alertComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    new_sequence_alertClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "new_sequence_alert"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = new_sequence_alertClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=new_sequence_alertClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 1.2-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in new_sequence_alertComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "new_sequence_alert"-------
    for thisComponent in new_sequence_alertComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_3.started', text_3.tStartRefresh)
    trials.addData('text_3.stopped', text_3.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    rep_trial = data.TrialHandler(nReps=10, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='rep_trial')
    thisExp.addLoop(rep_trial)  # add the loop to the experiment
    thisRep_trial = rep_trial.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRep_trial.rgb)
    if thisRep_trial != None:
        for paramName in thisRep_trial:
            exec('{} = thisRep_trial[paramName]'.format(paramName))
    
    for thisRep_trial in rep_trial:
        currentLoop = rep_trial
        # abbreviate parameter names if possible (e.g. rgb = thisRep_trial.rgb)
        if thisRep_trial != None:
            for paramName in thisRep_trial:
                exec('{} = thisRep_trial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "reward_t_info"-------
        continueRoutine = True
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        rewPts = rewPts - p_change
        if rewPts <0: 
            rewPts = 0
        
        rewT = "".join([str(rewPts)," Pts"])
        rew_main.setText(rewT)
        # keep track of which components have finished
        reward_t_infoComponents = [rew_tx1, rew_main, text_5]
        for thisComponent in reward_t_infoComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        reward_t_infoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "reward_t_info"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = reward_t_infoClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=reward_t_infoClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *rew_tx1* updates
            if rew_tx1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rew_tx1.frameNStart = frameN  # exact frame index
                rew_tx1.tStart = t  # local t and not account for scr refresh
                rew_tx1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rew_tx1, 'tStartRefresh')  # time at next scr refresh
                rew_tx1.setAutoDraw(True)
            if rew_tx1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rew_tx1.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    rew_tx1.tStop = t  # not accounting for scr refresh
                    rew_tx1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rew_tx1, 'tStopRefresh')  # time at next scr refresh
                    rew_tx1.setAutoDraw(False)
            
            # *rew_main* updates
            if rew_main.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rew_main.frameNStart = frameN  # exact frame index
                rew_main.tStart = t  # local t and not account for scr refresh
                rew_main.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rew_main, 'tStartRefresh')  # time at next scr refresh
                rew_main.setAutoDraw(True)
            if rew_main.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rew_main.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    rew_main.tStop = t  # not accounting for scr refresh
                    rew_main.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rew_main, 'tStopRefresh')  # time at next scr refresh
                    rew_main.setAutoDraw(False)
            
            # *text_5* updates
            if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_5.frameNStart = frameN  # exact frame index
                text_5.tStart = t  # local t and not account for scr refresh
                text_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
                text_5.setAutoDraw(True)
            if text_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_5.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_5.tStop = t  # not accounting for scr refresh
                    text_5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
                    text_5.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in reward_t_infoComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "reward_t_info"-------
        for thisComponent in reward_t_infoComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        rep_trial.addData('rew_tx1.started', rew_tx1.tStartRefresh)
        rep_trial.addData('rew_tx1.stopped', rew_tx1.tStopRefresh)
        rep_trial.addData('rew_main.started', rew_main.tStartRefresh)
        rep_trial.addData('rew_main.stopped', rew_main.tStopRefresh)
        rep_trial.addData('text_5.started', text_5.tStartRefresh)
        rep_trial.addData('text_5.stopped', text_5.tStopRefresh)
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
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
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
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
                preorder.setAutoDraw(True)
            if preorder.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > preorder.tStartRefresh + encoding_t-frameTolerance:
                    # keep track of stop time/frame for later
                    preorder.tStop = t  # not accounting for scr refresh
                    preorder.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(preorder, 'tStopRefresh')  # time at next scr refresh
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
                    win.timeOnFlip(assist, 'tStopRefresh')  # time at next scr refresh
                    assist.setAutoDraw(False)
            
            # *ISI_fix* updates
            if ISI_fix.status == NOT_STARTED and tThisFlip >= encoding_t-frameTolerance:
                # keep track of start time/frame for later
                ISI_fix.frameNStart = frameN  # exact frame index
                ISI_fix.tStart = t  # local t and not account for scr refresh
                ISI_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ISI_fix, 'tStartRefresh')  # time at next scr refresh
                ISI_fix.setAutoDraw(True)
            if ISI_fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ISI_fix.tStartRefresh + t_isi-frameTolerance:
                    # keep track of stop time/frame for later
                    ISI_fix.tStop = t  # not accounting for scr refresh
                    ISI_fix.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(ISI_fix, 'tStopRefresh')  # time at next scr refresh
                    ISI_fix.setAutoDraw(False)
            
            # *letter* updates
            if letter.status == NOT_STARTED and tThisFlip >= encoding_t +t_isi-frameTolerance:
                # keep track of start time/frame for later
                letter.frameNStart = frameN  # exact frame index
                letter.tStart = t  # local t and not account for scr refresh
                letter.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(letter, 'tStartRefresh')  # time at next scr refresh
                letter.setAutoDraw(True)
            if letter.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > letter.tStartRefresh + choice_t-frameTolerance:
                    # keep track of stop time/frame for later
                    letter.tStop = t  # not accounting for scr refresh
                    letter.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(letter, 'tStopRefresh')  # time at next scr refresh
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
                    win.timeOnFlip(testMsgUpper, 'tStopRefresh')  # time at next scr refresh
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
                    win.timeOnFlip(testMsgLower, 'tStopRefresh')  # time at next scr refresh
                    testMsgLower.setAutoDraw(False)
            
            # *TargetResp* updates
            waitOnFlip = False
            if TargetResp.status == NOT_STARTED and tThisFlip >= encoding_t+t_isi-frameTolerance:
                # keep track of start time/frame for later
                TargetResp.frameNStart = frameN  # exact frame index
                TargetResp.tStart = t  # local t and not account for scr refresh
                TargetResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TargetResp, 'tStartRefresh')  # time at next scr refresh
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
                    win.timeOnFlip(TargetResp, 'tStopRefresh')  # time at next scr refresh
                    TargetResp.status = FINISHED
            if TargetResp.status == STARTED and not waitOnFlip:
                theseKeys = TargetResp.getKeys(keyList=['1', '2', '3', '4', '5', '6', '7', '8', '9'], waitRelease=False)
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
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
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
        thisExp.addData('contingency', con_file)
        thisExp.addData('list_og', list_og)
        thisExp.addData('list_sort', list_sort)
        thisExp.addData('rewMag', rewMag)
        thisExp.addData('ViewDura', 5)
        rep_trial.addData('preorder.started', preorder.tStartRefresh)
        rep_trial.addData('preorder.stopped', preorder.tStopRefresh)
        rep_trial.addData('ISI_fix.started', ISI_fix.tStartRefresh)
        rep_trial.addData('ISI_fix.stopped', ISI_fix.tStopRefresh)
        rep_trial.addData('letter.started', letter.tStartRefresh)
        rep_trial.addData('letter.stopped', letter.tStopRefresh)
        # check responses
        if TargetResp.keys in ['', [], None]:  # No response was made
            TargetResp.keys = None
            # was no response the correct answer?!
            if str(cor_pos).lower() == 'none':
               TargetResp.corr = 1;  # correct non-response
            else:
               TargetResp.corr = 0;  # failed to respond (incorrectly)
        # store data for rep_trial (TrialHandler)
        rep_trial.addData('TargetResp.keys',TargetResp.keys)
        rep_trial.addData('TargetResp.corr', TargetResp.corr)
        if TargetResp.keys != None:  # we had a response
            rep_trial.addData('TargetResp.rt', TargetResp.rt)
        rep_trial.addData('TargetResp.started', TargetResp.tStartRefresh)
        rep_trial.addData('TargetResp.stopped', TargetResp.tStopRefresh)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "feedback"-------
        continueRoutine = True
        # update component parameters for each repeat
        fbtextpos = [0,0.13]
        rewDur = 1;
        p_change = 10;
        rewFB = "10 Pts";
        if not TargetResp.keys :
            feedbacktext="No Answer\nYou lose"
            fbColor = [0.73,0.73,0.674]
        elif TargetResp.corr:
            feedbacktext="Correct! \nYou win"
            fbColor = [0.65,0.8118,0.545]
            rewFB = rewT
            rep_trial.finished = True
            thisExp.addData('reward_points', rewPts)
        else:
            feedbacktext="Oops! Incorrect\nYou lose"
            fbColor = [0.8667,0.5137,0.513725]
        
        polygon.setFillColor(fbColor)
        polygon.setLineColor([1,1,1])
        fb1.setPos(fbtextpos)
        fb1.setText(feedbacktext)
        rewTxt.setText(rewFB)
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
        feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "feedback"-------
        while continueRoutine:
            # get current time
            t = feedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
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
                polygon.setAutoDraw(True)
            if polygon.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon.tStop = t  # not accounting for scr refresh
                    polygon.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                    polygon.setAutoDraw(False)
            
            # *fb1* updates
            if fb1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fb1.frameNStart = frameN  # exact frame index
                fb1.tStart = t  # local t and not account for scr refresh
                fb1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fb1, 'tStartRefresh')  # time at next scr refresh
                fb1.setAutoDraw(True)
            if fb1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fb1.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    fb1.tStop = t  # not accounting for scr refresh
                    fb1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fb1, 'tStopRefresh')  # time at next scr refresh
                    fb1.setAutoDraw(False)
            
            # *rewTxt* updates
            if rewTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rewTxt.frameNStart = frameN  # exact frame index
                rewTxt.tStart = t  # local t and not account for scr refresh
                rewTxt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rewTxt, 'tStartRefresh')  # time at next scr refresh
                rewTxt.setAutoDraw(True)
            if rewTxt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rewTxt.tStartRefresh + rewDur-frameTolerance:
                    # keep track of stop time/frame for later
                    rewTxt.tStop = t  # not accounting for scr refresh
                    rewTxt.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rewTxt, 'tStopRefresh')  # time at next scr refresh
                    rewTxt.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "feedback"-------
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        rep_trial.addData('fb1.started', fb1.tStartRefresh)
        rep_trial.addData('fb1.stopped', fb1.tStopRefresh)
        # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 10 repeats of 'rep_trial'
    
    # get names of stimulus parameters
    if rep_trial.trialList in ([], [None], None):
        params = []
    else:
        params = rep_trial.trialList[0].keys()
    # save data for this loop
    rep_trial.saveAsText(filename + 'rep_trial.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # ------Prepare to start Routine "fixation_cross"-------
    continueRoutine = True
    # update component parameters for each repeat
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
    fixation_crossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fixation_cross"-------
    while continueRoutine:
        # get current time
        t = fixation_crossClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixation_crossClock)
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
            fixation2.setAutoDraw(True)
        if fixation2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation2.tStartRefresh + dur_fixcross-frameTolerance:
                # keep track of stop time/frame for later
                fixation2.tStop = t  # not accounting for scr refresh
                fixation2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation2, 'tStopRefresh')  # time at next scr refresh
                fixation2.setAutoDraw(False)
        if fixation2.status == STARTED:  # only update if drawing
            fixation2.setText('+')
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixation_crossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation_cross"-------
    for thisComponent in fixation_crossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('fixation2.started', fixation2.tStartRefresh)
    trials.addData('fixation2.stopped', fixation2.tStopRefresh)
    # the Routine "fixation_cross" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "mood_rate"-------
    continueRoutine = True
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
    mood_rateClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "mood_rate"-------
    while continueRoutine:
        # get current time
        t = mood_rateClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=mood_rateClock)
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
            ScaleMsgSec.setAutoDraw(True)
        
        # *slider* updates
        if slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider.frameNStart = frameN  # exact frame index
            slider.tStart = t  # local t and not account for scr refresh
            slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
            slider.setAutoDraw(True)
        
        # Check slider for response to end routine
        if slider.getRating() is not None and slider.status == STARTED:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mood_rateComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "mood_rate"-------
    for thisComponent in mood_rateComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('ScaleMsgTop.started', ScaleMsgTop.tStartRefresh)
    trials.addData('ScaleMsgTop.stopped', ScaleMsgTop.tStopRefresh)
    trials.addData('ScaleMsgSec.started', ScaleMsgSec.tStartRefresh)
    trials.addData('ScaleMsgSec.stopped', ScaleMsgSec.tStopRefresh)
    trials.addData('slider.response', slider.getRating())
    trials.addData('slider.rt', slider.getRT())
    trials.addData('slider.started', slider.tStartRefresh)
    trials.addData('slider.stopped', slider.tStopRefresh)
    # the Routine "mood_rate" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "fixation_cross"-------
    continueRoutine = True
    # update component parameters for each repeat
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
    fixation_crossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fixation_cross"-------
    while continueRoutine:
        # get current time
        t = fixation_crossClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixation_crossClock)
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
            fixation2.setAutoDraw(True)
        if fixation2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation2.tStartRefresh + dur_fixcross-frameTolerance:
                # keep track of stop time/frame for later
                fixation2.tStop = t  # not accounting for scr refresh
                fixation2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation2, 'tStopRefresh')  # time at next scr refresh
                fixation2.setAutoDraw(False)
        if fixation2.status == STARTED:  # only update if drawing
            fixation2.setText('+')
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixation_crossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation_cross"-------
    for thisComponent in fixation_crossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('fixation2.started', fixation2.tStartRefresh)
    trials.addData('fixation2.stopped', fixation2.tStopRefresh)
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
nih_end = data.TrialHandler(nReps=run_nih_consent, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
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
    
    # ------Prepare to start Routine "end_nih"-------
    continueRoutine = True
    # update component parameters for each repeat
    nih_esp.keys = []
    nih_esp.rt = []
    _nih_esp_allKeys = []
    # keep track of which components have finished
    end_nihComponents = [nih_endtext, nih_esp]
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
    end_nihClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "end_nih"-------
    while continueRoutine:
        # get current time
        t = end_nihClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=end_nihClock)
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
            nih_endtext.setAutoDraw(True)
        
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
            theseKeys = nih_esp.getKeys(keyList=['esc', 'space'], waitRelease=False)
            _nih_esp_allKeys.extend(theseKeys)
            if len(_nih_esp_allKeys):
                nih_esp.keys = _nih_esp_allKeys[-1].name  # just the last key pressed
                nih_esp.rt = _nih_esp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end_nihComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "end_nih"-------
    for thisComponent in end_nihComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    nih_end.addData('nih_endtext.started', nih_endtext.tStartRefresh)
    nih_end.addData('nih_endtext.stopped', nih_endtext.tStopRefresh)
    # check responses
    if nih_esp.keys in ['', [], None]:  # No response was made
        nih_esp.keys = None
    nih_end.addData('nih_esp.keys',nih_esp.keys)
    if nih_esp.keys != None:  # we had a response
        nih_end.addData('nih_esp.rt', nih_esp.rt)
    core.quit()
    # the Routine "end_nih" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed run_nih_consent repeats of 'nih_end'


# ------Prepare to start Routine "end"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
endComponents = [ending_text, key_resp_2]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ending_text* updates
    if ending_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ending_text.frameNStart = frameN  # exact frame index
        ending_text.tStart = t  # local t and not account for scr refresh
        ending_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ending_text, 'tStartRefresh')  # time at next scr refresh
        ending_text.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['esc', 'space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ending_text.started', ending_text.tStartRefresh)
thisExp.addData('ending_text.stopped', ending_text.tStopRefresh)
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='comma')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
