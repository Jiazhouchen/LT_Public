/****************** 
 * Lt_Points Test *
 ******************/

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

// store info about the experiment session:
let expName = 'LT_points';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001', 'ucl': '0', 'skip': '0', 'study_id': '', 'ver_control': ''};

// Start code blocks for 'Before Experiment'
var con_file, inst_loop_n, rewFB, p_change, t_roll, rewDur, encoding_t,choice_t,fb_t;

var min;
var max;
function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min)) + min; 
}
con_file = "".concat("conditionsheets/contingency_", getRandomInt(1, 100), ".csv");


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
flowScheduler.add(rep_instLoopBegin, rep_instLoopScheduler);
flowScheduler.add(rep_instLoopScheduler);
flowScheduler.add(rep_instLoopEnd);
const pre_trial_moodLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(pre_trial_moodLoopBegin, pre_trial_moodLoopScheduler);
flowScheduler.add(pre_trial_moodLoopScheduler);
flowScheduler.add(pre_trial_moodLoopEnd);
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin, trialsLoopScheduler);
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
const nih_endLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(nih_endLoopBegin, nih_endLoopScheduler);
flowScheduler.add(nih_endLoopScheduler);
flowScheduler.add(nih_endLoopEnd);
flowScheduler.add(endRoutineBegin());
flowScheduler.add(endRoutineEachFrame());
flowScheduler.add(endRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'conditionsheets/inst.csv', 'path': 'conditionsheets/inst.csv'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.DEBUG);


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.2.10';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  psychoJS.setRedirectUrls('https://app.prolific.co/submissions/complete?cc=35C6E585', '');

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
var new_sequence_alertClock;
var text_3;
var reward_t_infoClock;
var rew_tx1;
var rew_main;
var text_5;
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
var nih_esp;
var endClock;
var ending_text;
var key_resp_2;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "setup"
  setupClock = new util.Clock();
  psychoJS.downloadResources([
    { name: con_file, path: con_file}
    ]);
  // Initialize components for Routine "inst"
  instClock = new util.Clock();
  upperMsg1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'upperMsg1',
    text: 'Welcome to the experiment. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.8], height: 0.08,  wrapWidth: 1.7, ori: 0,
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
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: "and remember this sequence of letters. \n\nWe will then show you one of the letters, and you should tell us at what alphabetical position that letter is. \n\nFor instance, if we show you 'B',  you should press the number 2 on your keyboard. If we show you 'X', you should press the number 4 on your keyboard. \n\nIf you respond correctly, you will advance to the next sequence. However, if incorrect response is made, you will be asked to repeat the same sequence again. You will repeat until a correct response is made. ",
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.25)], height: 0.065,  wrapWidth: 1.7, ori: 0,
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
    color: new util.Color('black'),  opacity: 1,
    depth: -6.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Inst_2"
  Inst_2Clock = new util.Clock();
  Msg1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Msg1',
    text: 'You will earn the payment listed for this study. In addition, you will also earn “points” for each sequence. \n\nFor each sequence, you will start with some points and you will lose 10 points for every incorrect attempt. \n\nYou will earn the points that’s left when you made a correct response. However, your earnable points will NOT go below 0. That is, you will either earn some points or nothing for each sequnce, never negative points. \n\nYou will win additional bonus payment based on the total points at the end of the study.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.065,  wrapWidth: 1.7, ori: 0,
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
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  slider = new visual.Slider({
    win: psychoJS.window, name: 'slider',
    size: [1.0, 0.1], pos: [0, (- 0.4)], units: 'norm',
    labels: ["Unhappy", "Happy"], ticks: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    granularity: 0.01, style: [visual.Slider.Style.RATING],
    color: new util.Color('LightGray'), 
    fontFamily: 'HelveticaBold', bold: true, italic: false, depth: -3, 
    flip: false,
  });
  
  // Initialize components for Routine "fixation_cross"
  fixation_crossClock = new util.Clock();
  
  
  fixation2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixation2',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.3,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "new_sequence_alert"
  new_sequence_alertClock = new util.Clock();
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: 'A new sequence is coming up',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: 1.5, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "reward_t_info"
  reward_t_infoClock = new util.Clock();
  rew_tx1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'rew_tx1',
    text: 'You have ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  rew_main = new visual.TextStim({
    win: psychoJS.window,
    name: 'rew_main',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    color: new util.Color('red'),  opacity: 1,
    depth: -2.0 
  });
  
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: 'remaining for this sequence',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  preorder = new visual.TextStim({
    win: psychoJS.window,
    name: 'preorder',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.35,  wrapWidth: 5, ori: 0,
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
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  ISI_fix = new visual.TextStim({
    win: psychoJS.window,
    name: 'ISI_fix',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  letter = new visual.TextStim({
    win: psychoJS.window,
    name: 'letter',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.4,  wrapWidth: 3, ori: 0,
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
    color: new util.Color('black'),  opacity: 1,
    depth: -6.0 
  });
  
  TargetResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "feedback"
  feedbackClock = new util.Clock();
  polygon = new visual.Rect ({
    win: psychoJS.window, name: 'polygon', 
    width: [0.8, 0.65][0], height: [0.8, 0.65][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color(1.0),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  fb1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'fb1',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  rewTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'rewTxt',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.15)], height: 0.25,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "fixation_cross"
  fixation_crossClock = new util.Clock();
  
  
  fixation2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixation2',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.3,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "mood_rate"
  mood_rateClock = new util.Clock();
  ScaleMsgTop = new visual.TextStim({
    win: psychoJS.window,
    name: 'ScaleMsgTop',
    text: 'Use the following scale to indicate your current mood:',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.65], height: 0.07,  wrapWidth: 1.5, ori: 0,
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
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  slider = new visual.Slider({
    win: psychoJS.window, name: 'slider',
    size: [1.0, 0.1], pos: [0, (- 0.4)], units: 'norm',
    labels: ["Unhappy", "Happy"], ticks: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    granularity: 0.01, style: [visual.Slider.Style.RATING],
    color: new util.Color('LightGray'), 
    fontFamily: 'HelveticaBold', bold: true, italic: false, depth: -3, 
    flip: false,
  });
  
  // Initialize components for Routine "fixation_cross"
  fixation_crossClock = new util.Clock();
  
  
  fixation2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixation2',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.3,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "end_nih"
  end_nihClock = new util.Clock();
  nih_endtext = new visual.TextStim({
    win: psychoJS.window,
    name: 'nih_endtext',
    text: 'Thank you for your participation!\n\n\nYour completion code is: \n\n3YTZRJZ_00356\n\nPlease enter this code to the MTurk page for validation.\n\nYou may keep this page open while type in the code in the MTurk page. \n\nAlternatively, you can press SPACE BAR and a message will pop up to allow you to copy this code, and you may paste it there. \n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: 1.5, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  nih_esp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "end"
  endClock = new util.Clock();
  ending_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'ending_text',
    text: 'Thank you for your participation!\n\nPress space bar to close the experiment. You will be redirected to get your compensation. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
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
  return function () {
    //------Prepare to start Routine 'setup'-------
    t = 0;
    setupClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    setupComponents = [];
    
    setupComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function setupRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'setup'-------
    // get current time
    t = setupClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    setupComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
var ver_control;
function setupRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'setup'-------
    setupComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    var ver_control
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
    ver_control = expInfo["ver_control"]
    psychoJS.experiment.addData("ver_control", ver_control);
    // the Routine "setup" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var rep_inst;
var currentLoop;
function rep_instLoopBegin(rep_instLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  rep_inst = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 999, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'conditionsheets/inst.csv',
    seed: undefined, name: 'rep_inst'
  });
  psychoJS.experiment.addLoop(rep_inst); // add the loop to the experiment
  currentLoop = rep_inst;  // we're now the current loop

  // Schedule all the trials in the trialList:
  rep_inst.forEach(function() {
    const snapshot = rep_inst.getSnapshot();

    rep_instLoopScheduler.add(importConditions(snapshot));
    const trials_2LoopScheduler = new Scheduler(psychoJS);
    rep_instLoopScheduler.add(trials_2LoopBegin, trials_2LoopScheduler);
    rep_instLoopScheduler.add(trials_2LoopScheduler);
    rep_instLoopScheduler.add(trials_2LoopEnd);
    const trials_3LoopScheduler = new Scheduler(psychoJS);
    rep_instLoopScheduler.add(trials_3LoopBegin, trials_3LoopScheduler);
    rep_instLoopScheduler.add(trials_3LoopScheduler);
    rep_instLoopScheduler.add(trials_3LoopEnd);
    rep_instLoopScheduler.add(endLoopIteration(rep_instLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


var trials_2;
function trials_2LoopBegin(trials_2LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_2 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'trials_2'
  });
  psychoJS.experiment.addLoop(trials_2); // add the loop to the experiment
  currentLoop = trials_2;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials_2.forEach(function() {
    const snapshot = trials_2.getSnapshot();

    trials_2LoopScheduler.add(importConditions(snapshot));
    trials_2LoopScheduler.add(instRoutineBegin(snapshot));
    trials_2LoopScheduler.add(instRoutineEachFrame(snapshot));
    trials_2LoopScheduler.add(instRoutineEnd(snapshot));
    trials_2LoopScheduler.add(endLoopIteration(trials_2LoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function trials_2LoopEnd() {
  psychoJS.experiment.removeLoop(trials_2);

  return Scheduler.Event.NEXT;
}


var trials_3;
function trials_3LoopBegin(trials_3LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_3 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'trials_3'
  });
  psychoJS.experiment.addLoop(trials_3); // add the loop to the experiment
  currentLoop = trials_3;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials_3.forEach(function() {
    const snapshot = trials_3.getSnapshot();

    trials_3LoopScheduler.add(importConditions(snapshot));
    trials_3LoopScheduler.add(Inst_2RoutineBegin(snapshot));
    trials_3LoopScheduler.add(Inst_2RoutineEachFrame(snapshot));
    trials_3LoopScheduler.add(Inst_2RoutineEnd(snapshot));
    trials_3LoopScheduler.add(endLoopIteration(trials_3LoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function trials_3LoopEnd() {
  psychoJS.experiment.removeLoop(trials_3);

  return Scheduler.Event.NEXT;
}


function rep_instLoopEnd() {
  psychoJS.experiment.removeLoop(rep_inst);

  return Scheduler.Event.NEXT;
}


var pre_trial_mood;
function pre_trial_moodLoopBegin(pre_trial_moodLoopScheduler) {
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
  pre_trial_mood.forEach(function() {
    const snapshot = pre_trial_mood.getSnapshot();

    pre_trial_moodLoopScheduler.add(importConditions(snapshot));
    pre_trial_moodLoopScheduler.add(mood_rateRoutineBegin(snapshot));
    pre_trial_moodLoopScheduler.add(mood_rateRoutineEachFrame(snapshot));
    pre_trial_moodLoopScheduler.add(mood_rateRoutineEnd(snapshot));
    pre_trial_moodLoopScheduler.add(fixation_crossRoutineBegin(snapshot));
    pre_trial_moodLoopScheduler.add(fixation_crossRoutineEachFrame(snapshot));
    pre_trial_moodLoopScheduler.add(fixation_crossRoutineEnd(snapshot));
    pre_trial_moodLoopScheduler.add(endLoopIteration(pre_trial_moodLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function pre_trial_moodLoopEnd() {
  psychoJS.experiment.removeLoop(pre_trial_mood);

  return Scheduler.Event.NEXT;
}


var trials;
function trialsLoopBegin(trialsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: con_file,
    seed: undefined, name: 'trials'
  });
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials.forEach(function() {
    const snapshot = trials.getSnapshot();

    trialsLoopScheduler.add(importConditions(snapshot));
    trialsLoopScheduler.add(new_sequence_alertRoutineBegin(snapshot));
    trialsLoopScheduler.add(new_sequence_alertRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(new_sequence_alertRoutineEnd(snapshot));
    const rep_trialLoopScheduler = new Scheduler(psychoJS);
    trialsLoopScheduler.add(rep_trialLoopBegin, rep_trialLoopScheduler);
    trialsLoopScheduler.add(rep_trialLoopScheduler);
    trialsLoopScheduler.add(rep_trialLoopEnd);
    trialsLoopScheduler.add(fixation_crossRoutineBegin(snapshot));
    trialsLoopScheduler.add(fixation_crossRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(fixation_crossRoutineEnd(snapshot));
    trialsLoopScheduler.add(mood_rateRoutineBegin(snapshot));
    trialsLoopScheduler.add(mood_rateRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(mood_rateRoutineEnd(snapshot));
    trialsLoopScheduler.add(fixation_crossRoutineBegin(snapshot));
    trialsLoopScheduler.add(fixation_crossRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(fixation_crossRoutineEnd(snapshot));
    trialsLoopScheduler.add(endLoopIteration(trialsLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


var rep_trial;
function rep_trialLoopBegin(rep_trialLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  rep_trial = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 10, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'rep_trial'
  });
  psychoJS.experiment.addLoop(rep_trial); // add the loop to the experiment
  currentLoop = rep_trial;  // we're now the current loop

  // Schedule all the trials in the trialList:
  rep_trial.forEach(function() {
    const snapshot = rep_trial.getSnapshot();

    rep_trialLoopScheduler.add(importConditions(snapshot));
    rep_trialLoopScheduler.add(reward_t_infoRoutineBegin(snapshot));
    rep_trialLoopScheduler.add(reward_t_infoRoutineEachFrame(snapshot));
    rep_trialLoopScheduler.add(reward_t_infoRoutineEnd(snapshot));
    rep_trialLoopScheduler.add(trialRoutineBegin(snapshot));
    rep_trialLoopScheduler.add(trialRoutineEachFrame(snapshot));
    rep_trialLoopScheduler.add(trialRoutineEnd(snapshot));
    rep_trialLoopScheduler.add(feedbackRoutineBegin(snapshot));
    rep_trialLoopScheduler.add(feedbackRoutineEachFrame(snapshot));
    rep_trialLoopScheduler.add(feedbackRoutineEnd(snapshot));
    rep_trialLoopScheduler.add(endLoopIteration(rep_trialLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function rep_trialLoopEnd() {
  psychoJS.experiment.removeLoop(rep_trial);

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


var nih_end;
function nih_endLoopBegin(nih_endLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  nih_end = new TrialHandler({
    psychoJS: psychoJS,
    nReps: run_nih_consent, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'nih_end'
  });
  psychoJS.experiment.addLoop(nih_end); // add the loop to the experiment
  currentLoop = nih_end;  // we're now the current loop

  // Schedule all the trials in the trialList:
  nih_end.forEach(function() {
    const snapshot = nih_end.getSnapshot();

    nih_endLoopScheduler.add(importConditions(snapshot));
    nih_endLoopScheduler.add(end_nihRoutineBegin(snapshot));
    nih_endLoopScheduler.add(end_nihRoutineEachFrame(snapshot));
    nih_endLoopScheduler.add(end_nihRoutineEnd(snapshot));
    nih_endLoopScheduler.add(endLoopIteration(nih_endLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function nih_endLoopEnd() {
  psychoJS.experiment.removeLoop(nih_end);

  return Scheduler.Event.NEXT;
}


var _key_resp_allKeys;
var instComponents;
function instRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'inst'-------
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
    
    instComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'inst'-------
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
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'inst'-------
    instComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "inst" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_5_allKeys;
var Inst_2Components;
function Inst_2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Inst_2'-------
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
    
    Inst_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Inst_2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Inst_2'-------
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
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Inst_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Inst_2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Inst_2'-------
    Inst_2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    if (key_resp_5.corr) {
        rep_inst.finished = true;
    }
    
    // the Routine "Inst_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var mood_rateComponents;
function mood_rateRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'mood_rate'-------
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
    
    mood_rateComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function mood_rateRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'mood_rate'-------
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
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    mood_rateComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function mood_rateRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'mood_rate'-------
    mood_rateComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('slider.response', slider.getRating());
    psychoJS.experiment.addData('slider.rt', slider.getRT());
    // the Routine "mood_rate" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var dur_fixcross;
var fixation_crossComponents;
function fixation_crossRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'fixation_cross'-------
    t = 0;
    fixation_crossClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    dur_fixcross = getRandomInt(300, 1000)/1000;
    psychoJS.experiment.addData("ITI", dur_fixcross);
    // keep track of which components have finished
    fixation_crossComponents = [];
    fixation_crossComponents.push(fixation2);
    
    fixation_crossComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function fixation_crossRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'fixation_cross'-------
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
    if ((fixation2.status === PsychoJS.Status.STARTED || fixation2.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      fixation2.setAutoDraw(false);
    }
    
    if (fixation2.status === PsychoJS.Status.STARTED){ // only update if being drawn
      fixation2.setText('+', false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    fixation_crossComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fixation_crossRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'fixation_cross'-------
    fixation_crossComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "fixation_cross" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var rewPts;
var p_change;
var new_sequence_alertComponents;
function new_sequence_alertRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'new_sequence_alert'-------
    t = 0;
    new_sequence_alertClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.200000);
    // update component parameters for each repeat
    rewPts = rewMag.match(/\d+/);
    rewPts = rewPts.join("");
    p_change = 0;
    
    // keep track of which components have finished
    new_sequence_alertComponents = [];
    new_sequence_alertComponents.push(text_3);
    
    new_sequence_alertComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function new_sequence_alertRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'new_sequence_alert'-------
    // get current time
    t = new_sequence_alertClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_3* updates
    if (t >= 0.0 && text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_3.tStart = t;  // (not accounting for frame time here)
      text_3.frameNStart = frameN;  // exact frame index
      
      text_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((text_3.status === PsychoJS.Status.STARTED || text_3.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      text_3.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    new_sequence_alertComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function new_sequence_alertRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'new_sequence_alert'-------
    new_sequence_alertComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var rewT;
var reward_t_infoComponents;
function reward_t_infoRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'reward_t_info'-------
    t = 0;
    reward_t_infoClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.500000);
    // update component parameters for each repeat
    rewPts = (rewPts - p_change);
    if ((rewPts < 0)) {
        rewPts = 0;
    }
    rewT = String(rewPts) + " Pts";
    
    rew_main.setText(rewT);
    // keep track of which components have finished
    reward_t_infoComponents = [];
    reward_t_infoComponents.push(rew_tx1);
    reward_t_infoComponents.push(rew_main);
    reward_t_infoComponents.push(text_5);
    
    reward_t_infoComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function reward_t_infoRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'reward_t_info'-------
    // get current time
    t = reward_t_infoClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *rew_tx1* updates
    if (t >= 0.0 && rew_tx1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rew_tx1.tStart = t;  // (not accounting for frame time here)
      rew_tx1.frameNStart = frameN;  // exact frame index
      
      rew_tx1.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((rew_tx1.status === PsychoJS.Status.STARTED || rew_tx1.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      rew_tx1.setAutoDraw(false);
    }
    
    // *rew_main* updates
    if (t >= 0.0 && rew_main.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rew_main.tStart = t;  // (not accounting for frame time here)
      rew_main.frameNStart = frameN;  // exact frame index
      
      rew_main.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((rew_main.status === PsychoJS.Status.STARTED || rew_main.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      rew_main.setAutoDraw(false);
    }
    
    // *text_5* updates
    if (t >= 0.0 && text_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_5.tStart = t;  // (not accounting for frame time here)
      text_5.frameNStart = frameN;  // exact frame index
      
      text_5.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((text_5.status === PsychoJS.Status.STARTED || text_5.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      text_5.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    reward_t_infoComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function reward_t_infoRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'reward_t_info'-------
    reward_t_infoComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var t_isi;
var encoding_t;
var choice_t;
var fb_t;
var _TargetResp_allKeys;
var trialComponents;
function trialRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'trial'-------
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
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
    
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function trialRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'trial'-------
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
    if ((preorder.status === PsychoJS.Status.STARTED || preorder.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
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
    if ((assist.status === PsychoJS.Status.STARTED || assist.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
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
    if ((ISI_fix.status === PsychoJS.Status.STARTED || ISI_fix.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
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
    if ((letter.status === PsychoJS.Status.STARTED || letter.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
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
    if ((testMsgUpper.status === PsychoJS.Status.STARTED || testMsgUpper.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
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
    if ((testMsgLower.status === PsychoJS.Status.STARTED || testMsgLower.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
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
    if ((TargetResp.status === PsychoJS.Status.STARTED || TargetResp.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
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
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trialRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'trial'-------
    trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData("contingency", con_file);
    psychoJS.experiment.addData("list_og", list_og);
    psychoJS.experiment.addData("list_sort", list_sort);
    psychoJS.experiment.addData("rewMag", rewMag);
    psychoJS.experiment.addData("ViewDura", 5);
    // was no response the correct answer?!
    if (TargetResp.keys === undefined) {
      if (['None','none',undefined].includes(cor_pos)) {
         TargetResp.corr = 1;  // correct non-response
      } else {
         TargetResp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('TargetResp.keys', TargetResp.keys);
    psychoJS.experiment.addData('TargetResp.corr', TargetResp.corr);
    if (typeof TargetResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('TargetResp.rt', TargetResp.rt);
        routineTimer.reset();
        }
    
    TargetResp.stop();
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var fbtextpos;
var rewDur;
var rewFB;
var feedbacktext;
var fbColor;
var feedbackComponents;
function feedbackRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'feedback'-------
    t = 0;
    feedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    fbtextpos = [0, 0.13];
    rewDur = 1;
    p_change = 10;
    rewFB = "10 Pts";
    if ((! TargetResp.keys)) {
        feedbacktext = "No Answer\nYou lose";
        fbColor = [0.73, 0.73, 0.674];
    } else {
        if (TargetResp.corr) {
            feedbacktext = "Correct! \nYou win";
            fbColor = [0.65, 0.8118, 0.545];
            rewFB = rewT;
            rep_trial.finished = true;
            psychoJS.experiment.addData("reward_points", rewPts);
        } else {
            feedbacktext = "Oops! Incorrect\nYou lose";
            fbColor = [0.8667, 0.5137, 0.513725];
        }
    }
    
    polygon.setFillColor(new util.Color(fbColor));
    polygon.setLineColor(new util.Color([1, 1, 1]));
    fb1.setPos(fbtextpos);
    fb1.setText(feedbacktext);
    rewTxt.setText(rewFB);
    // keep track of which components have finished
    feedbackComponents = [];
    feedbackComponents.push(polygon);
    feedbackComponents.push(fb1);
    feedbackComponents.push(rewTxt);
    
    feedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function feedbackRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'feedback'-------
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

    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((polygon.status === PsychoJS.Status.STARTED || polygon.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      polygon.setAutoDraw(false);
    }
    
    // *fb1* updates
    if (t >= 0.0 && fb1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fb1.tStart = t;  // (not accounting for frame time here)
      fb1.frameNStart = frameN;  // exact frame index
      
      fb1.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((fb1.status === PsychoJS.Status.STARTED || fb1.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      fb1.setAutoDraw(false);
    }
    
    // *rewTxt* updates
    if (t >= 0.0 && rewTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rewTxt.tStart = t;  // (not accounting for frame time here)
      rewTxt.frameNStart = frameN;  // exact frame index
      
      rewTxt.setAutoDraw(true);
    }

    frameRemains = 0.0 + rewDur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((rewTxt.status === PsychoJS.Status.STARTED || rewTxt.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      rewTxt.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    feedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function feedbackRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'feedback'-------
    feedbackComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _nih_esp_allKeys;
var end_nihComponents;
function end_nihRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'end_nih'-------
    t = 0;
    end_nihClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    nih_esp.keys = undefined;
    nih_esp.rt = undefined;
    _nih_esp_allKeys = [];
    // keep track of which components have finished
    end_nihComponents = [];
    end_nihComponents.push(nih_endtext);
    end_nihComponents.push(nih_esp);
    
    end_nihComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function end_nihRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'end_nih'-------
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
      let theseKeys = nih_esp.getKeys({keyList: ['esc', 'space'], waitRelease: false});
      _nih_esp_allKeys = _nih_esp_allKeys.concat(theseKeys);
      if (_nih_esp_allKeys.length > 0) {
        nih_esp.keys = _nih_esp_allKeys[_nih_esp_allKeys.length - 1].name;  // just the last key pressed
        nih_esp.rt = _nih_esp_allKeys[_nih_esp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    end_nihComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function end_nihRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'end_nih'-------
    end_nihComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('nih_esp.keys', nih_esp.keys);
    if (typeof nih_esp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('nih_esp.rt', nih_esp.rt);
        routineTimer.reset();
        }
    
    nih_esp.stop();
    psychoJS.quit({message: 'The experiment is now complete. Thank you for your participation! Please copy-and-paste the following completion code into MTurk so that we can confirm your participation: 3YTZRJZ_00356'})
    // the Routine "end_nih" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_2_allKeys;
var endComponents;
function endRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'end'-------
    t = 0;
    endClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // keep track of which components have finished
    endComponents = [];
    endComponents.push(ending_text);
    endComponents.push(key_resp_2);
    
    endComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function endRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'end'-------
    // get current time
    t = endClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *ending_text* updates
    if (t >= 0.0 && ending_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ending_text.tStart = t;  // (not accounting for frame time here)
      ending_text.frameNStart = frameN;  // exact frame index
      
      ending_text.setAutoDraw(true);
    }

    
    // *key_resp_2* updates
    if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }

    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['esc', 'space'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    endComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function endRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'end'-------
    endComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
