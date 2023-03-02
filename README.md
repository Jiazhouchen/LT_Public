# Letter Task Experiment & Analysis Code - Public

## Experiment Code Availability:
For code to recreate the experiments, see "Experiment" folder. The Letter Task with Multiple Attempt (LT_MT) is available in the LT_MT_Task folder and the Letter Task with Single Attempt (LT_ST) is available in the LT_ST_Task folder. 
## Data Availability:
The data for both of the studies are available at the [OSF project page](https://osf.io/3txm5)

## Letter Task Multiple Attempt Version Analysis 
 To read more about the task, please refer to the paper.
 Start off by using script 
 > LT_MT_analysis.R 
 
 You can load the existing data or import from raw data directly. Source the script above to load the data into your environment (must first configure path to data folder)
 ###Overview of objects in existing data:

 1. Objects:
     - **sum_df**: data.frame object that contains summary stats on all participants (both included / excluded). Participants without IDs are supplied with one starting wtih "NOID_"
     - **bdf**: data.frame object containing filtered participants data (only accurate trial number > 49)
     - **edf**: data.frame object containing participant data that is not in bdf but passed basic filtering (missed < 200 trials and experienced > 200 trials)
     - **cdf**: data.frame object that's joint of bdf and edf.
 2. Variables:
     - **slider.response**: momentary happiness rating, one observation per trial per participant;
     - **slider.rt**: reaction time of slider.response;
     - **TargetResp.corr**: objective correctness of participants responses, one observation per trial per participant;
     - **TargetResp.rt**: reaction time of participants responses, one observation per trial per participant;
     - **missed**: indicator for no reponses recorded. TRUE for missed trial. one observation per trial per participant;
     - **N**: number of letters, task contingency, one observation per trial, range from 3 to 9;
     - **fb_yn**: indicator for if the trial contains feedback, 7 per participants
     - **trial**: number of trial, one observation per trial, identical across participants
     - **uq_index**: index for a unique participant
     - **nt_sfb**: number of trials since last feedback, NA indicates no feedback seen yet. one obverstaion per trial, identical across participants
     - **fb_value**: the accuracy percentage when participants view the feedback, 7 per participants, duplicated for all trials following each feedback;
     - **par_type**: TRUE for participants who would otherwise be excluded based on accurate trial number criteria. one per participant;
     - **fb_tt5**: indicator for feedback trials and 5 after them. Used mostly to exclude trials under the influence of feedback. 
 3. Regression Models:
     - See in-script comments

## Letter Task Single Attempt Version Analysis
 To read more about the task, please visit the [OSF pre-registration page](https://osf.io/3txm5)
 Start off by using script 
 > LT_ST_analysis.R 
 
 You can load the existing data or import from raw data directly. Source the script above to load the data into your environment (must first configure path to data folder)
 ###Overview of objects in existing data:

 1. Objects:
     - **sum_df**: data.frame object that contains summary stats on all participants (both included / excluded). Participants without IDs are supplied with one starting wtih "NOID_"
     - **bdf**: data.frame object containing filtered participants data (only accurate trial number > 49)
     - **edf**: data.frame object containing participant data that is not in bdf but passed basic filtering (missed < 200 trials and experienced > 200 trials)
     - **cdf**: data.frame object that's joint of bdf and edf.
 2. Variables:
     - **slider.response**: momentary happiness rating, one observation per trial per participant;
     - **slider.rt**: reaction time of slider.response;
     - **TargetResp.corr**: objective correctness of participants responses, one observation per trial per participant;
     - **TargetResp.rt**: reaction time of participants responses, one observation per trial per participant;
     - **missed**: indicator for no reponses recorded. TRUE for missed trial. one observation per trial per participant;
     - **N**: number of letters, task contingency, one observation per trial, range from 3 to 9;
     - **fb_yn**: indicator for if the trial contains feedback, 7 per participants
     - **trial**: number of trial, one observation per trial, identical across participants
     - **uq_index**: index for a unique participant
     - **nt_sfb**: number of trials since last feedback, NA indicates no feedback seen yet. one obverstaion per trial, identical across participants
     - **fb_value**: the accuracy percentage when participants view the feedback, 7 per participants, duplicated for all trials following each feedback;
     - **par_type**: TRUE for participants who would otherwise be excluded based on accurate trial number criteria. one per participant;
     - **fb_tt5**: indicator for feedback trials and 5 after them. Used mostly to exclude trials under the influence of feedback. 
 3. Regression Models:
     - See in-script comments
