/************** 
 * Lt_Sf Test *
 **************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2022.2.2.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'LT_SF';  // from the Builder filename that created this script
let expInfo = {
    'participant': '',
    'ucl': '0',
    'skip': '0',
};

// Start code blocks for 'Before Experiment'
// Run 'Before Experiment' code from setup_code
var con_file, inst_loop_n, rewPer, tcount, ccount, p_change, t_roll, rewDur, encoding_t,choice_t,fb_t;

var min;
var max;
function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min)) + min; 
}

tcount = 0;
ccount = 0;

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: false,
  color: new util.Color([0, 0, 0]),
  units: 'norm',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(setupRoutineBegin());
flowScheduler.add(setupRoutineEachFrame());
flowScheduler.add(setupRoutineEnd());
const rep_instLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(rep_instLoopBegin(rep_instLoopScheduler));
flowScheduler.add(rep_instLoopScheduler);
flowScheduler.add(rep_instLoopEnd);
const pre_trial_moodLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(pre_trial_moodLoopBegin(pre_trial_moodLoopScheduler));
flowScheduler.add(pre_trial_moodLoopScheduler);
flowScheduler.add(pre_trial_moodLoopEnd);
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
const nih_endLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(nih_endLoopBegin(nih_endLoopScheduler));
flowScheduler.add(nih_endLoopScheduler);
flowScheduler.add(nih_endLoopEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'code.csv', 'path': 'code.csv'},
    {'name': 'contingency_SR.csv', 'path': 'contingency_SR.csv'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.DEBUG);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2022.2.2';
  expInfo['OS'] = window.navigator.platform;

  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var setupClock;
var instClock;
var upperMsg1;
var upperMsg2;
var example1;
var midMsg1;
var example2;
var text;
var rightnext;
var key_resp;
var Inst_2Clock;
var Msg1;
var Mag2;
var left2;
var right2;
var key_resp_5;
var mood_rateClock;
var ScaleMsgTop;
var ScaleMsgMain;
var ScaleMsgSec;
var slider;
var fixation_crossClock;
var fixation2;
var trialClock;
var preorder;
var assist;
var ISI_fix;
var letter;
var testMsgUpper;
var testMsgLower;
var TargetResp;
var feedbackClock;
var polygon;
var fb1;
var rewTxt;
var end_nihClock;
var nih_endtext;
var mt_code;
var nih_esp;
var nih_endtext2;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "setup"
  setupClock = new util.Clock();
  // Initialize components for Routine "inst"
  instClock = new util.Clock();
  upperMsg1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'upperMsg1',
    text: 'Welcome to the experiment. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.8], height: 0.08,  wrapWidth: 1.7, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  upperMsg2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'upperMsg2',
    text: 'On each trial, we will show you a few letters, for example: ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.65], height: 0.065,  wrapWidth: 1.7, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  example1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'example1',
    text: 'X F A B',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.5], height: 0.15,  wrapWidth: 1.7, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  midMsg1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'midMsg1',
    text: 'Please order these letters alphabetically in your mind. In this case: ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.35], height: 0.065,  wrapWidth: 2, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  example2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'example2',
    text: 'A B F X',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.2], height: 0.15,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: "and remember this sequence of letters. \n\nWe will then show you one of the letters, and you should tell us at what alphabetical position that letter is. \n\nFor instance, if we show you 'B',  you should press the number 2 on your keyboard. If we show you 'X', you should press the number 4 on your keyboard. \n\nIn most trials, you will not receive feedback on whether your response was correct or not. \n\nOnce in a while, we will show you correct responses count and accuracy percentage. The count and percentage will reset after you see them. ",
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.25)], height: 0.065,  wrapWidth: 1.7, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -5.0 
  });
  
  rightnext = new visual.TextStim({
    win: psychoJS.window,
    name: 'rightnext',
    text: 'Right Arrow Key: Next Page ',
    font: 'Arial',
    units: undefined, 
    pos: [0.65, (- 0.8)], height: 0.05,  wrapWidth: 1.5, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -6.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Inst_2"
  Inst_2Clock = new util.Clock();
  Msg1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Msg1',
    text: 'You will earn the payment listed for this study. In addition, you will also earn “points” for each correct response. \n\nYou will win additional bonus payment based on the total points at the end of the study.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.065,  wrapWidth: 1.7, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  Mag2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Mag2',
    text: 'We will also ask you to rate how happy you are at the end of every trial. \n\nYou will provide your response by clicking on a scale using your mouse. \n\nWhen you are ready to start, press SPACE BAR to start.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.065,  wrapWidth: 1.7, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  left2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'left2',
    text: 'Left Arrow Key: Previous Page ',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.65), (- 0.8)], height: 0.05,  wrapWidth: 1.5, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  right2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'right2',
    text: 'Space bar: Start the Study',
    font: 'Arial',
    units: undefined, 
    pos: [0.65, (- 0.8)], height: 0.05,  wrapWidth: 1.5, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  key_resp_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "mood_rate"
  mood_rateClock = new util.Clock();
  ScaleMsgTop = new visual.TextStim({
    win: psychoJS.window,
    name: 'ScaleMsgTop',
    text: 'Use the following scale to indicate your current mood:',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.65], height: 0.07,  wrapWidth: 1.5, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  ScaleMsgMain = new visual.TextStim({
    win: psychoJS.window,
    name: 'ScaleMsgMain',
    text: 'How happy are you currently?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.1,  wrapWidth: 1.5, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  ScaleMsgSec = new visual.TextStim({
    win: psychoJS.window,
    name: 'ScaleMsgSec',
    text: 'Use your mouse to select',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.15], height: 0.07,  wrapWidth: 1.5, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  slider = new visual.Slider({
    win: psychoJS.window, name: 'slider',
    startValue: undefined,
    size: [1.0, 0.1], pos: [0, (- 0.4)], ori: 0, units: 'norm',
    labels: ["Unhappy", "Happy"], fontSize: 0.05, ticks: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    granularity: 0.01, style: ["RATING"],
    color: new util.Color('LightGray'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: 1, fontFamily: 'HelveticaBold', bold: true, italic: false, depth: -3, 
    flip: false,
  });
  
  // Initialize components for Routine "fixation_cross"
  fixation_crossClock = new util.Clock();
  
  
  fixation2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixation2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.3,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  preorder = new visual.TextStim({
    win: psychoJS.window,
    name: 'preorder',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.35,  wrapWidth: 5, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  assist = new visual.TextStim({
    win: psychoJS.window,
    name: 'assist',
    text: 'Alphabetize...',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.7], height: 0.05,  wrapWidth: 5, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  ISI_fix = new visual.TextStim({
    win: psychoJS.window,
    name: 'ISI_fix',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  letter = new visual.TextStim({
    win: psychoJS.window,
    name: 'letter',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.4,  wrapWidth: 3, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  testMsgUpper = new visual.TextStim({
    win: psychoJS.window,
    name: 'testMsgUpper',
    text: 'After alphabetization, what is the position of ...',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.6], height: 0.07,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -5.0 
  });
  
  testMsgLower = new visual.TextStim({
    win: psychoJS.window,
    name: 'testMsgLower',
    text: 'Use numeric key to make a response.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.6)], height: 0.07,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -6.0 
  });
  
  TargetResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "feedback"
  feedbackClock = new util.Clock();
  polygon = new visual.Rect ({
    win: psychoJS.window, name: 'polygon', 
    width: [1, 0.75][0], height: [1, 0.75][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  fb1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'fb1',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: 1, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  rewTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'rewTxt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.15)], height: 0.15,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "end_nih"
  end_nihClock = new util.Clock();
  nih_endtext = new visual.TextStim({
    win: psychoJS.window,
    name: 'nih_endtext',
    text: 'Thank you for your participation!\n\n\nYour completion code is: ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.5], height: 0.1,  wrapWidth: 1.5, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  mt_code = new visual.TextStim({
    win: psychoJS.window,
    name: 'mt_code',
    text: '',
    font: 'Arialbd',
    units: undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  nih_esp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  nih_endtext2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'nih_endtext2',
    text: 'Please provide this code back to the MTurk page for completion credit. Come back here and press SPACE BAR to close the session after you provided the code.\n\nFailure to do so might result in forfeiting your compensation. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.5)], height: 0.1,  wrapWidth: 1.5, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -4.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var setupComponents;
function setupRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'setup' ---
    t = 0;
    setupClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    setupComponents = [];
    
    for (const thisComponent of setupComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function setupRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'setup' ---
    // get current time
    t = setupClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of setupComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var inst_loop_n;
var run_nih_consent;
function setupRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'setup' ---
    for (const thisComponent of setupComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from setup_code
    if ((expInfo["skip"] === "1")) {
        inst_loop_n = 0;
    } else {
        inst_loop_n = 1;
    }
    
    if ((expInfo["ucl"] === "1")) {
        run_nih_consent = 0;
    } else {
        run_nih_consent = 1;
    }
    // the Routine "setup" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var rep_inst;
function rep_instLoopBegin(rep_instLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    rep_inst = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'rep_inst'
    });
    psychoJS.experiment.addLoop(rep_inst); // add the loop to the experiment
    currentLoop = rep_inst;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisRep_inst of rep_inst) {
      snapshot = rep_inst.getSnapshot();
      rep_instLoopScheduler.add(importConditions(snapshot));
      const page1LoopScheduler = new Scheduler(psychoJS);
      rep_instLoopScheduler.add(page1LoopBegin(page1LoopScheduler, snapshot));
      rep_instLoopScheduler.add(page1LoopScheduler);
      rep_instLoopScheduler.add(page1LoopEnd);
      const page2LoopScheduler = new Scheduler(psychoJS);
      rep_instLoopScheduler.add(page2LoopBegin(page2LoopScheduler, snapshot));
      rep_instLoopScheduler.add(page2LoopScheduler);
      rep_instLoopScheduler.add(page2LoopEnd);
      rep_instLoopScheduler.add(rep_instLoopEndIteration(rep_instLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var page1;
function page1LoopBegin(page1LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    page1 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'page1'
    });
    psychoJS.experiment.addLoop(page1); // add the loop to the experiment
    currentLoop = page1;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisPage1 of page1) {
      snapshot = page1.getSnapshot();
      page1LoopScheduler.add(importConditions(snapshot));
      page1LoopScheduler.add(instRoutineBegin(snapshot));
      page1LoopScheduler.add(instRoutineEachFrame());
      page1LoopScheduler.add(instRoutineEnd(snapshot));
      page1LoopScheduler.add(page1LoopEndIteration(page1LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function page1LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(page1);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function page1LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var page2;
function page2LoopBegin(page2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    page2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'page2'
    });
    psychoJS.experiment.addLoop(page2); // add the loop to the experiment
    currentLoop = page2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisPage2 of page2) {
      snapshot = page2.getSnapshot();
      page2LoopScheduler.add(importConditions(snapshot));
      page2LoopScheduler.add(Inst_2RoutineBegin(snapshot));
      page2LoopScheduler.add(Inst_2RoutineEachFrame());
      page2LoopScheduler.add(Inst_2RoutineEnd(snapshot));
      page2LoopScheduler.add(page2LoopEndIteration(page2LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function page2LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(page2);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function page2LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function rep_instLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(rep_inst);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function rep_instLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var pre_trial_mood;
function pre_trial_moodLoopBegin(pre_trial_moodLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    pre_trial_mood = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'pre_trial_mood'
    });
    psychoJS.experiment.addLoop(pre_trial_mood); // add the loop to the experiment
    currentLoop = pre_trial_mood;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisPre_trial_mood of pre_trial_mood) {
      snapshot = pre_trial_mood.getSnapshot();
      pre_trial_moodLoopScheduler.add(importConditions(snapshot));
      pre_trial_moodLoopScheduler.add(mood_rateRoutineBegin(snapshot));
      pre_trial_moodLoopScheduler.add(mood_rateRoutineEachFrame());
      pre_trial_moodLoopScheduler.add(mood_rateRoutineEnd(snapshot));
      pre_trial_moodLoopScheduler.add(fixation_crossRoutineBegin(snapshot));
      pre_trial_moodLoopScheduler.add(fixation_crossRoutineEachFrame());
      pre_trial_moodLoopScheduler.add(fixation_crossRoutineEnd(snapshot));
      pre_trial_moodLoopScheduler.add(pre_trial_moodLoopEndIteration(pre_trial_moodLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function pre_trial_moodLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(pre_trial_mood);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function pre_trial_moodLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'contingency_SR.csv',
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial of trials) {
      snapshot = trials.getSnapshot();
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(trialRoutineBegin(snapshot));
      trialsLoopScheduler.add(trialRoutineEachFrame());
      trialsLoopScheduler.add(trialRoutineEnd(snapshot));
      const fb_logicalLoopScheduler = new Scheduler(psychoJS);
      trialsLoopScheduler.add(fb_logicalLoopBegin(fb_logicalLoopScheduler, snapshot));
      trialsLoopScheduler.add(fb_logicalLoopScheduler);
      trialsLoopScheduler.add(fb_logicalLoopEnd);
      trialsLoopScheduler.add(fixation_crossRoutineBegin(snapshot));
      trialsLoopScheduler.add(fixation_crossRoutineEachFrame());
      trialsLoopScheduler.add(fixation_crossRoutineEnd(snapshot));
      trialsLoopScheduler.add(mood_rateRoutineBegin(snapshot));
      trialsLoopScheduler.add(mood_rateRoutineEachFrame());
      trialsLoopScheduler.add(mood_rateRoutineEnd(snapshot));
      trialsLoopScheduler.add(fixation_crossRoutineBegin(snapshot));
      trialsLoopScheduler.add(fixation_crossRoutineEachFrame());
      trialsLoopScheduler.add(fixation_crossRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var fb_logical;
function fb_logicalLoopBegin(fb_logicalLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    fb_logical = new TrialHandler({
      psychoJS: psychoJS,
      nReps: fb_yn, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'fb_logical'
    });
    psychoJS.experiment.addLoop(fb_logical); // add the loop to the experiment
    currentLoop = fb_logical;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisFb_logical of fb_logical) {
      snapshot = fb_logical.getSnapshot();
      fb_logicalLoopScheduler.add(importConditions(snapshot));
      fb_logicalLoopScheduler.add(feedbackRoutineBegin(snapshot));
      fb_logicalLoopScheduler.add(feedbackRoutineEachFrame());
      fb_logicalLoopScheduler.add(feedbackRoutineEnd(snapshot));
      fb_logicalLoopScheduler.add(fb_logicalLoopEndIteration(fb_logicalLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function fb_logicalLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(fb_logical);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function fb_logicalLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var nih_end;
function nih_endLoopBegin(nih_endLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    nih_end = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.FULLRANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'code.csv',
      seed: undefined, name: 'nih_end'
    });
    psychoJS.experiment.addLoop(nih_end); // add the loop to the experiment
    currentLoop = nih_end;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisNih_end of nih_end) {
      snapshot = nih_end.getSnapshot();
      nih_endLoopScheduler.add(importConditions(snapshot));
      nih_endLoopScheduler.add(end_nihRoutineBegin(snapshot));
      nih_endLoopScheduler.add(end_nihRoutineEachFrame());
      nih_endLoopScheduler.add(end_nihRoutineEnd(snapshot));
      nih_endLoopScheduler.add(nih_endLoopEndIteration(nih_endLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function nih_endLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(nih_end);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function nih_endLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var _key_resp_allKeys;
var instComponents;
function instRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'inst' ---
    t = 0;
    instClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    instComponents = [];
    instComponents.push(upperMsg1);
    instComponents.push(upperMsg2);
    instComponents.push(example1);
    instComponents.push(midMsg1);
    instComponents.push(example2);
    instComponents.push(text);
    instComponents.push(rightnext);
    instComponents.push(key_resp);
    
    for (const thisComponent of instComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function instRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'inst' ---
    // get current time
    t = instClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *upperMsg1* updates
    if (t >= 0.0 && upperMsg1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      upperMsg1.tStart = t;  // (not accounting for frame time here)
      upperMsg1.frameNStart = frameN;  // exact frame index
      
      upperMsg1.setAutoDraw(true);
    }

    
    // *upperMsg2* updates
    if (t >= 0.0 && upperMsg2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      upperMsg2.tStart = t;  // (not accounting for frame time here)
      upperMsg2.frameNStart = frameN;  // exact frame index
      
      upperMsg2.setAutoDraw(true);
    }

    
    // *example1* updates
    if (t >= 0.0 && example1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      example1.tStart = t;  // (not accounting for frame time here)
      example1.frameNStart = frameN;  // exact frame index
      
      example1.setAutoDraw(true);
    }

    
    // *midMsg1* updates
    if (t >= 0.0 && midMsg1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      midMsg1.tStart = t;  // (not accounting for frame time here)
      midMsg1.frameNStart = frameN;  // exact frame index
      
      midMsg1.setAutoDraw(true);
    }

    
    // *example2* updates
    if (t >= 0.0 && example2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      example2.tStart = t;  // (not accounting for frame time here)
      example2.frameNStart = frameN;  // exact frame index
      
      example2.setAutoDraw(true);
    }

    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    
    // *rightnext* updates
    if (t >= 0.0 && rightnext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rightnext.tStart = t;  // (not accounting for frame time here)
      rightnext.frameNStart = frameN;  // exact frame index
      
      rightnext.setAutoDraw(true);
    }

    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['right', 'esc'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'inst' ---
    for (const thisComponent of instComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    key_resp.stop();
    // the Routine "inst" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_5_allKeys;
var Inst_2Components;
function Inst_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Inst_2' ---
    t = 0;
    Inst_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_5.keys = undefined;
    key_resp_5.rt = undefined;
    _key_resp_5_allKeys = [];
    // keep track of which components have finished
    Inst_2Components = [];
    Inst_2Components.push(Msg1);
    Inst_2Components.push(Mag2);
    Inst_2Components.push(left2);
    Inst_2Components.push(right2);
    Inst_2Components.push(key_resp_5);
    
    for (const thisComponent of Inst_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Inst_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Inst_2' ---
    // get current time
    t = Inst_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Msg1* updates
    if (t >= 0.0 && Msg1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Msg1.tStart = t;  // (not accounting for frame time here)
      Msg1.frameNStart = frameN;  // exact frame index
      
      Msg1.setAutoDraw(true);
    }

    
    // *Mag2* updates
    if (t >= 0.0 && Mag2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Mag2.tStart = t;  // (not accounting for frame time here)
      Mag2.frameNStart = frameN;  // exact frame index
      
      Mag2.setAutoDraw(true);
    }

    
    // *left2* updates
    if (t >= 0.0 && left2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      left2.tStart = t;  // (not accounting for frame time here)
      left2.frameNStart = frameN;  // exact frame index
      
      left2.setAutoDraw(true);
    }

    
    // *right2* updates
    if (t >= 0.0 && right2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      right2.tStart = t;  // (not accounting for frame time here)
      right2.frameNStart = frameN;  // exact frame index
      
      right2.setAutoDraw(true);
    }

    
    // *key_resp_5* updates
    if (t >= 0.0 && key_resp_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_5.tStart = t;  // (not accounting for frame time here)
      key_resp_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.clearEvents(); });
    }

    if (key_resp_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_5.getKeys({keyList: ['left', 'space'], waitRelease: false});
      _key_resp_5_allKeys = _key_resp_5_allKeys.concat(theseKeys);
      if (_key_resp_5_allKeys.length > 0) {
        key_resp_5.keys = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].name;  // just the last key pressed
        key_resp_5.rt = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].rt;
        // was this correct?
        if (key_resp_5.keys == 'space') {
            key_resp_5.corr = 1;
        } else {
            key_resp_5.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Inst_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Inst_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Inst_2' ---
    for (const thisComponent of Inst_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    key_resp_5.stop();
    // Run 'End Routine' code from code_6
    if (key_resp_5.corr) {
        rep_inst.finished = true;
    }
    
    // the Routine "Inst_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var mood_rateComponents;
function mood_rateRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'mood_rate' ---
    t = 0;
    mood_rateClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    slider.reset()
    // keep track of which components have finished
    mood_rateComponents = [];
    mood_rateComponents.push(ScaleMsgTop);
    mood_rateComponents.push(ScaleMsgMain);
    mood_rateComponents.push(ScaleMsgSec);
    mood_rateComponents.push(slider);
    
    for (const thisComponent of mood_rateComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function mood_rateRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'mood_rate' ---
    // get current time
    t = mood_rateClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *ScaleMsgTop* updates
    if (t >= 0.0 && ScaleMsgTop.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ScaleMsgTop.tStart = t;  // (not accounting for frame time here)
      ScaleMsgTop.frameNStart = frameN;  // exact frame index
      
      ScaleMsgTop.setAutoDraw(true);
    }

    
    // *ScaleMsgMain* updates
    if (t >= 0.0 && ScaleMsgMain.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ScaleMsgMain.tStart = t;  // (not accounting for frame time here)
      ScaleMsgMain.frameNStart = frameN;  // exact frame index
      
      ScaleMsgMain.setAutoDraw(true);
    }

    
    // *ScaleMsgSec* updates
    if (t >= 0.0 && ScaleMsgSec.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ScaleMsgSec.tStart = t;  // (not accounting for frame time here)
      ScaleMsgSec.frameNStart = frameN;  // exact frame index
      
      ScaleMsgSec.setAutoDraw(true);
    }

    
    // *slider* updates
    if (t >= 0.0 && slider.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider.tStart = t;  // (not accounting for frame time here)
      slider.frameNStart = frameN;  // exact frame index
      
      slider.setAutoDraw(true);
    }

    
    // Check slider for response to end routine
    if (slider.getRating() !== undefined && slider.status === PsychoJS.Status.STARTED) {
      continueRoutine = false; }
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of mood_rateComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function mood_rateRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'mood_rate' ---
    for (const thisComponent of mood_rateComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('slider.response', slider.getRating());
    psychoJS.experiment.addData('slider.rt', slider.getRT());
    // the Routine "mood_rate" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var dur_fixcross;
var fixation_crossComponents;
function fixation_crossRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'fixation_cross' ---
    t = 0;
    fixation_crossClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from ITI_code
    dur_fixcross = getRandomInt(300, 1000)/1000;
    psychoJS.experiment.addData("ITI", dur_fixcross);
    // keep track of which components have finished
    fixation_crossComponents = [];
    fixation_crossComponents.push(fixation2);
    
    for (const thisComponent of fixation_crossComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function fixation_crossRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'fixation_cross' ---
    // get current time
    t = fixation_crossClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixation2* updates
    if (t >= 0.0 && fixation2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation2.tStart = t;  // (not accounting for frame time here)
      fixation2.frameNStart = frameN;  // exact frame index
      
      fixation2.setAutoDraw(true);
    }

    frameRemains = 0.0 + dur_fixcross - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixation2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixation2.setAutoDraw(false);
    }
    
    if (fixation2.status === PsychoJS.Status.STARTED){ // only update if being drawn
      fixation2.setText('+', false);
    }
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of fixation_crossComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fixation_crossRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'fixation_cross' ---
    for (const thisComponent of fixation_crossComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "fixation_cross" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var t_isi;
var encoding_t;
var choice_t;
var fb_t;
var _TargetResp_allKeys;
var trialComponents;
function trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial' ---
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_2
    t_isi = getRandomInt(500, 800)/1000;
    encoding_t = Math.sqrt(N);
    choice_t = 3;
    fb_t = 1
    psychoJS.experiment.addData("ISI", t_isi);
    preorder.setText(list_og);
    ISI_fix.setText('+');
    letter.setText(target_letter);
    TargetResp.keys = undefined;
    TargetResp.rt = undefined;
    _TargetResp_allKeys = [];
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(preorder);
    trialComponents.push(assist);
    trialComponents.push(ISI_fix);
    trialComponents.push(letter);
    trialComponents.push(testMsgUpper);
    trialComponents.push(testMsgLower);
    trialComponents.push(TargetResp);
    
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial' ---
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *preorder* updates
    if (t >= 0.0 && preorder.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      preorder.tStart = t;  // (not accounting for frame time here)
      preorder.frameNStart = frameN;  // exact frame index
      
      preorder.setAutoDraw(true);
    }

    frameRemains = 0.0 + encoding_t - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (preorder.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      preorder.setAutoDraw(false);
    }
    
    // *assist* updates
    if (t >= 0.0 && assist.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      assist.tStart = t;  // (not accounting for frame time here)
      assist.frameNStart = frameN;  // exact frame index
      
      assist.setAutoDraw(true);
    }

    frameRemains = 0.0 + encoding_t - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (assist.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      assist.setAutoDraw(false);
    }
    
    // *ISI_fix* updates
    if (t >= encoding_t && ISI_fix.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ISI_fix.tStart = t;  // (not accounting for frame time here)
      ISI_fix.frameNStart = frameN;  // exact frame index
      
      ISI_fix.setAutoDraw(true);
    }

    frameRemains = encoding_t + t_isi - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (ISI_fix.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      ISI_fix.setAutoDraw(false);
    }
    
    // *letter* updates
    if (t >= (encoding_t + t_isi) && letter.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      letter.tStart = t;  // (not accounting for frame time here)
      letter.frameNStart = frameN;  // exact frame index
      
      letter.setAutoDraw(true);
    }

    frameRemains = (encoding_t + t_isi) + choice_t - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (letter.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      letter.setAutoDraw(false);
    }
    
    // *testMsgUpper* updates
    if (t >= (encoding_t + t_isi) && testMsgUpper.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      testMsgUpper.tStart = t;  // (not accounting for frame time here)
      testMsgUpper.frameNStart = frameN;  // exact frame index
      
      testMsgUpper.setAutoDraw(true);
    }

    frameRemains = (encoding_t + t_isi) + choice_t - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (testMsgUpper.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      testMsgUpper.setAutoDraw(false);
    }
    
    // *testMsgLower* updates
    if (t >= (encoding_t + t_isi) && testMsgLower.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      testMsgLower.tStart = t;  // (not accounting for frame time here)
      testMsgLower.frameNStart = frameN;  // exact frame index
      
      testMsgLower.setAutoDraw(true);
    }

    frameRemains = (encoding_t + t_isi) + choice_t - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (testMsgLower.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      testMsgLower.setAutoDraw(false);
    }
    
    // *TargetResp* updates
    if (t >= (encoding_t + t_isi) && TargetResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TargetResp.tStart = t;  // (not accounting for frame time here)
      TargetResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { TargetResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { TargetResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { TargetResp.clearEvents(); });
    }

    frameRemains = (encoding_t + t_isi) + choice_t - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (TargetResp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      TargetResp.status = PsychoJS.Status.FINISHED;
  }

    if (TargetResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = TargetResp.getKeys({keyList: ['1', '2', '3', '4', '5', '6', '7', '8', '9'], waitRelease: false});
      _TargetResp_allKeys = _TargetResp_allKeys.concat(theseKeys);
      if (_TargetResp_allKeys.length > 0) {
        TargetResp.keys = _TargetResp_allKeys[0].name;  // just the first key pressed
        TargetResp.rt = _TargetResp_allKeys[0].rt;
        // was this correct?
        if (TargetResp.keys == cor_pos) {
            TargetResp.corr = 1;
        } else {
            TargetResp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var tcount;
var ccount;
function trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial' ---
    for (const thisComponent of trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from code_2
    tcount = tcount+1;
    if (TargetResp.corr) {
        ccount = ccount + 1;
    }
    // was no response the correct answer?!
    if (TargetResp.keys === undefined) {
      if (['None','none',undefined].includes(cor_pos)) {
         TargetResp.corr = 1;  // correct non-response
      } else {
         TargetResp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(TargetResp.corr, level);
    }
    psychoJS.experiment.addData('TargetResp.keys', TargetResp.keys);
    psychoJS.experiment.addData('TargetResp.corr', TargetResp.corr);
    if (typeof TargetResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('TargetResp.rt', TargetResp.rt);
        routineTimer.reset();
        }
    
    TargetResp.stop();
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var rewPer;
var fbColor;
var feedbackComponents;
function feedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback' ---
    t = 0;
    feedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(4.000000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code
    rewPer = Math.round((ccount / tcount) * 1000)/10;
    if (rewPer > 80) {
        fbColor = [0.65, 0.8118, 0.545];
    } else {
        fbColor = [0.8667, 0.5137, 0.513725];
    }
    rewPer = rewPer.toString();
    ccount = ccount.toString();
    tcount = tcount.toString();
    polygon.setFillColor(new util.Color(fbColor));
    polygon.setLineColor(new util.Color([1, 1, 1]));
    fb1.setPos([0, 0.13]);
    fb1.setText((((("You got " + ccount) + " / ") + tcount) + " correct."));
    rewTxt.setText((("Your accuracy rate is " + rewPer) + "%"));
    // keep track of which components have finished
    feedbackComponents = [];
    feedbackComponents.push(polygon);
    feedbackComponents.push(fb1);
    feedbackComponents.push(rewTxt);
    
    for (const thisComponent of feedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function feedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback' ---
    // get current time
    t = feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon* updates
    if (t >= 0.0 && polygon.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon.tStart = t;  // (not accounting for frame time here)
      polygon.frameNStart = frameN;  // exact frame index
      
      polygon.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (polygon.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      polygon.setAutoDraw(false);
    }
    
    // *fb1* updates
    if (t >= 0.0 && fb1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fb1.tStart = t;  // (not accounting for frame time here)
      fb1.frameNStart = frameN;  // exact frame index
      
      fb1.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fb1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fb1.setAutoDraw(false);
    }
    
    // *rewTxt* updates
    if (t >= 0.0 && rewTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rewTxt.tStart = t;  // (not accounting for frame time here)
      rewTxt.frameNStart = frameN;  // exact frame index
      
      rewTxt.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (rewTxt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rewTxt.setAutoDraw(false);
    }
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function feedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback' ---
    for (const thisComponent of feedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from code
    tcount=0;
    ccount=0;
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _nih_esp_allKeys;
var end_nihComponents;
function end_nihRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'end_nih' ---
    t = 0;
    end_nihClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    mt_code.setText(passcode);
    nih_esp.keys = undefined;
    nih_esp.rt = undefined;
    _nih_esp_allKeys = [];
    // keep track of which components have finished
    end_nihComponents = [];
    end_nihComponents.push(nih_endtext);
    end_nihComponents.push(mt_code);
    end_nihComponents.push(nih_esp);
    end_nihComponents.push(nih_endtext2);
    
    for (const thisComponent of end_nihComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function end_nihRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'end_nih' ---
    // get current time
    t = end_nihClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *nih_endtext* updates
    if (t >= 0.0 && nih_endtext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      nih_endtext.tStart = t;  // (not accounting for frame time here)
      nih_endtext.frameNStart = frameN;  // exact frame index
      
      nih_endtext.setAutoDraw(true);
    }

    
    // *mt_code* updates
    if (t >= 0.0 && mt_code.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mt_code.tStart = t;  // (not accounting for frame time here)
      mt_code.frameNStart = frameN;  // exact frame index
      
      mt_code.setAutoDraw(true);
    }

    
    // *nih_esp* updates
    if (t >= 0.0 && nih_esp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      nih_esp.tStart = t;  // (not accounting for frame time here)
      nih_esp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { nih_esp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { nih_esp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { nih_esp.clearEvents(); });
    }

    if (nih_esp.status === PsychoJS.Status.STARTED) {
      let theseKeys = nih_esp.getKeys({keyList: ['space'], waitRelease: false});
      _nih_esp_allKeys = _nih_esp_allKeys.concat(theseKeys);
      if (_nih_esp_allKeys.length > 0) {
        nih_esp.keys = _nih_esp_allKeys[_nih_esp_allKeys.length - 1].name;  // just the last key pressed
        nih_esp.rt = _nih_esp_allKeys[_nih_esp_allKeys.length - 1].rt;
        // was this correct?
        if (nih_esp.keys == 'space') {
            nih_esp.corr = 1;
        } else {
            nih_esp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *nih_endtext2* updates
    if (t >= 0.0 && nih_endtext2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      nih_endtext2.tStart = t;  // (not accounting for frame time here)
      nih_endtext2.frameNStart = frameN;  // exact frame index
      
      nih_endtext2.setAutoDraw(true);
    }

    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of end_nihComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function end_nihRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'end_nih' ---
    for (const thisComponent of end_nihComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    nih_esp.stop();
    // Run 'End Routine' code from code_7
    if (nih_esp.corr) {
        nih_end.finished = true;
    }
    psychoJS.experiment.addData("verify_ID", ID);
    // the Routine "end_nih" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
