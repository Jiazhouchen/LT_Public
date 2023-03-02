require("lmerTest")
require("lme4")
require("ggplot2")

##following section is for loading data
if(FALSE) {
  ls_csvs <- list.files(path = "data/LT_SF",pattern = "*.csv", recursive = F,include.dirs = T,full.names = T)
  all_data <- lapply(ls_csvs,read.csv,stringsAsFactors = F)
  for (x in 1:length(all_data)){
    all_data[[x]]$uq_index <- x
  }
  
  ##Trials Only: 
  LT_SF_proc <- function(dfx) {
    ##Return nothing for ones with less than 15 trials (will not see first feedback)
    if(nrow(dfx)<15) {return(NULL)}
    
    if(is.na(unique(dfx$participant))){
      dfx$participant <- paste("NOID",sample(LETTERS,size = 1,replace = T),round(abs(rnorm(1))*100000000,0),sep = "_")
      NO_ID <- TRUE
    } else {
      NO_ID <- FALSE
    }
    #print(unique(dfx$participant))
    #clean up:
    dfx<-dfx[apply(dfx[grepl(".ran",names(dfx))],1,function(x){any(!is.na(x))}),]
    ##pretrial info & removal:
    if(!is.null(dfx$pre_trial_mood.ran)){
      pretrial_mood <- dfx$slider.response[!is.na(dfx$pre_trial_mood.ran)]
      dfx <- dfx[which(is.na(dfx$pre_trial_mood.ran)),]
    } else {
      pretrial_mood <- NA
    }
    ##get rid of ending code:
    if(!is.null(dfx$nih_end.ran)) {
      ID_code <- paste(dfx$passcode[!is.na(dfx$nih_end.ran)],dfx$ID[!is.na(dfx$nih_end.ran)],sep = " + ")
      dfx <- dfx[which(is.na(dfx$nih_end.ran)),]
    } else {
      ID_code <- "DID NOT REACH END"
    }
    
    ##clean up single trials data points: 
    s_in <- apply(dfx,2,function(x){length(unique(x))>1})
    singlet_vari <- apply(dfx[!s_in],2,unique)
    singlet_vari <- as.data.frame(t((singlet_vari[sapply(singlet_vari,length)!=0 & !is.na(singlet_vari)])))
    singlet_vari$passcode <- NULL
    ##get variables that varies by trials
    multit_vari <- dfx[s_in]
    ##clean up the feedback trials:
    fb_t <- lapply(which(!is.na(multit_vari$fb_logical.ran)),function(x){c(x,x+1)})
    fb_j <- do.call(rbind,lapply(fb_t,function(x){
      data.frame(t(apply(multit_vari[x,],2,function(y){
        y[y==""]<-NA
        if(any(!is.na(y))) {
          return(y[!is.na(y)])
        } else {
          return(NA)
        }
      })))
    }))
    
    dfy <- rbind(multit_vari[-unlist(fb_t),],fb_j)
    dfy <- dfy[order(as.numeric(dfy$trials.thisTrialN)),]
    dfy$trial <- as.numeric(dfy$trials.thisTrialN) + 1
    dfz <- suppressWarnings(as.data.frame(lapply(dfy[!grepl("fb_logical|trials.this|list_",names(dfy),perl = T)],as.numeric)))
    dfz$uq_index <- singlet_vari$uq_index
    if(is.null(dfz$TargetResp.keys)){
      dfz$TargetResp.keys<-NA
    }
    
    dfz$fb_zone <- cumsum(1:nrow(dfz) %in% which(dfz$fb_yn==1))
    fb_lts <- lapply(lapply(split(1:nrow(dfz),dfz$fb_zone),seq_along), `-`,1)
    fb_lts$`0` <- rep(NA,length(fb_lts$`0`))
    fb_lts$`7` <- rep(NA,length(fb_lts$`7`))
    
    fb_value <- unname(sapply(split(dfz$TargetResp.corr,cumsum(1:nrow(dfz) %in% (which(dfz$fb_yn==1)+1))),function(x){sum(x,na.rm = T)/length(x)}))
    fb_vb <- fb_lts
    for (x in 1:length(fb_value)) {
      fb_vb[[(x+1)]] <- rep(fb_value[x],length(fb_vb[[(x+1)]]))
    }
    
    dfz$nt_sfb <- unname(unlist(fb_lts))
    dfz$fb_value <- unname(unlist(fb_vb))
    #Add single subject data:
    singlet_vari$pretrial_mood <- pretrial_mood
    singlet_vari$total_t <- nrow(dfz)
    singlet_vari$act <- sum(dfz$TargetResp.corr,na.rm = T)
    singlet_vari$mit <- length(which(is.na(dfz$TargetResp.keys)))
    singlet_vari$acc_per <- singlet_vari$act / nrow(dfz)
    singlet_vari$no_id <- NO_ID
    singlet_vari$ID_code <- ID_code
    
    return(list(s_df = singlet_vari,m_df = dfz))
  }
  
  proc_data <- lapply(all_data,LT_SF_proc)
  proc_data <- proc_data[!sapply(proc_data, is.null)]
  
  
  sum_df <- do.call(rbind,lapply(proc_data,`[[`,"s_df"))
  
  sum_df$dup_part <- duplicated(sum_df$participant,fromLast = T) | duplicated(sum_df$participant)
  sum_df$insuf_act <- sum_df$act < 49
  sum_df$insuf_t <- sum_df$total_t < 168
  sum_df$insuf_vt <- sum_df$mit > 200
  sum_df$include <- !sum_df$dup_part & !sum_df$insuf_act & !sum_df$insuf_t
  
  nrow(sum_df[!sum_df$dup_part & !sum_df$insuf_act & !sum_df$insuf_t,])
  uq_include<-sum_df$uq_index[sum_df$include]
  
  bdf <- do.call(rbind,lapply(proc_data[which(sum_df$include)],`[[`,"m_df"))
  bdf$missed <- is.na(bdf$TargetResp.keys)
  bdf$fb_tt5 <- 0
  bdf$fb_tt5[which(bdf$nt_sfb %in% c(0:5))] <- 1
  
  #exclude people who are obviously not trying
  edf <- do.call(rbind,lapply(proc_data[which(!sum_df$include & !sum_df$insuf_t & !sum_df$insuf_vt)],`[[`,"m_df"))
  edf$missed <- is.na(edf$TargetResp.keys)
  edf$fb_tt5 <- 0
  edf$fb_tt5[which(edf$nt_sfb %in% c(0:5))] <- 1
  
  edf$par_type <- TRUE
  bdf$par_type <- FALSE
  
  cdf <- rbind(bdf,edf)
} else {
  load("LT_SF_analysis.rdata")
}

axis_style <- element_text(face = "bold.italic", color = "black", size = 20)
ag_cut<-aggregate(TargetResp.corr~N+uq_index,data = bdf,FUN = mean)
id_cut<-ag_cut$uq_index[which(ag_cut$N==3 & ag_cut$TargetResp.corr < 0.3) ]
bdf$id_cut <- bdf$uq_index %in% id_cut
bdf$mood_dmean<-do.call(c,lapply(split(bdf$slider.response,bdf$uq_index),function(x){as.numeric(scale(x,scale = T,center=T))}))
stop("")
###Overview:
######Objects:
###sum_df: data.frame object that contains summary stats on all participants (both included / excluded). Participants without IDs are supplied with one starting wtih "NOID_"
###bdf: data.frame object containing filtered participants data (only accurate trial number > 49)
###edf: data.frame object containing participant data that is not in bdf but passed basic filtering (missed < 200 trials and experienced > 200 trials)
###cdf: data.frame object that's joint of bdf and edf.
######Variables:
###slider.response: momentary happiness rating, one observation per trial per participant;
###slider.rt: reaction time of slider.response;
###TargetResp.corr: objective correctness of participants responses, one observation per trial per participant;
###TargetResp.rt: reaction time of participants responses, one observation per trial per participant;
###missed: indicator for no reponses recorded. TRUE for missed trial. one observation per trial per participant;
###N: number of letters, task contingency, one observation per trial, range from 3 to 9;
###fb_yn: indicator for if the trial contains feedback, 7 per participants
###trial: number of trial, one observation per trial, identical across participants
###uq_index: index for a unique participant
###nt_sfb: number of trials since last feedback, NA indicates no feedback seen yet. one obverstaion per trial, identical across participants
###fb_value: the accuracy percentage when participants view the feedback, 7 per participants, duplicated for all trials following each feedback;
###par_type: TRUE for participants who would otherwise be excluded based on accurate trial number criteria. one per participant;
###fb_tt5: indicator for feedback trials and 5 after them. Used mostly to exclude trials under the influence of feedback. 
ggplot(bdf,aes(y=slider.response,x=trial),color="#85d4c7") + 
  geom_point(position = position_dodge2(width = 1),color="#85d4c7",alpha=0.1)+
  geom_line(mapping = aes(fill=participant,color=participant),stat="smooth",method = "lm", size = 1.5,alpha = 0.4, color="#85d4c7")+
  stat_summary(fun.data=mean_sdl, fun.args = list(mult=1), geom="errorbar", color="#0c4a40", width=0.1, size =0.5) +
  geom_smooth(method="lm",color="#0c453c",fill="#0c4a40") + ylim(c(0,10.5)) +
  xlab("Trial") + ylab("Momentary Happiness Ratings")+ theme(text  = element_text(size = 20)) 
bdf$participant <- bdf$uq_index
### Logistic regression for accuracy:
accuracy_m1<-lme4::glmer(TargetResp.corr ~ scale(N)*scale(trial)+(scale(N)*scale(trial)|uq_index),data = bdf,
                       family = binomial(),lme4::glmerControl(optimizer = "bobyqa", optCtrl = list(maxfun = 100000)))
### Plot accuracy by difficulty
ggplot(bdf[!is.na(bdf$TargetResp.rt),],aes(x=N,y=TargetResp.corr),color="#284E57")+
  #geom_histogram(data = aggregate(TargetResp.corr~N,data = bdf,FUN = mean),stat = "identity",alpha=0.2,fill="#0c4a40")+
  geom_point(data=aggregate(TargetResp.corr~N+uq_index,data = bdf[!is.na(bdf$TargetResp.rt),],FUN = mean),color="#284E57",alpha=0.2,position = position_jitter(width = 0.2))+
  geom_point(data=aggregate(TargetResp.corr~N,data = bdf[!is.na(bdf$TargetResp.rt),],FUN = mean),color="#284E57",size=5)+
  geom_line(data=aggregate(TargetResp.corr~N,data = bdf[!is.na(bdf$TargetResp.rt),],FUN = mean),color="#284E57",linewidth=2)+
  stat_summary(fun.data=mean_se, fun.args = list(mult=10), geom="errorbar", color="#0c4a40", width=0.2, size =1) +
  scale_x_continuous(breaks = 3:9,labels=c("3","4","5","6","7","8","9"))+
  xlab("Number of Letters") + ylab("Response Accuracy (%)") + 
  theme(text  = element_text(size = 20),axis.text = axis_style,legend.position = "none") 
ggsave(filename = "S2AxL.png",scale = 1.3,width=3,height = 4,units = "in")

##Investigate the small cluster of ppl in 3

ag_cut<-aggregate(TargetResp.corr~N+uq_index,data = bdf,FUN = mean)
id_cut<-ag_cut$uq_index[which(ag_cut$N==3 & ag_cut$TargetResp.corr < 0.3) ]
bdf$id_cut <- bdf$uq_index %in% id_cut
ggplot(bdf,aes(x=N,y=TargetResp.corr),color="#284E57")+
  #geom_histogram(data = aggregate(TargetResp.corr~N,data = bdf,FUN = mean),stat = "identity",alpha=0.2,fill="#0c4a40")+
  geom_point(data=aggregate(TargetResp.corr~N+uq_index,data = bdf[!bdf$id_cut,],FUN = mean),color="#284E57",alpha=0.1,position = position_jitter(width = 0.2))+
  geom_point(data=aggregate(TargetResp.corr~N+uq_index,data = bdf[bdf$id_cut,],FUN = mean),
             aes(x=N,y=TargetResp.corr,color=uq_index),
             alpha=0.4,position = position_jitter(width = 0.2))+
  geom_line(data=aggregate(TargetResp.corr~N+uq_index,data = bdf[bdf$id_cut,],FUN = mean),
             aes(x=N,y=TargetResp.corr,color=uq_index),
             alpha=0.4)+
  geom_point(data=aggregate(TargetResp.corr~N,data = bdf,FUN = mean),color="#284E57",size=5)+
  geom_line(data=aggregate(TargetResp.corr~N,data = bdf,FUN = mean),color="#284E57",linewidth=2)+
  stat_summary(fun.data=mean_se, fun.args = list(mult=10), geom="errorbar", color="#0c4a40", width=0.2, size =1) +
  scale_x_continuous(breaks = 3:9,labels=c("3","4","5","6","7","8","9"))+
  xlab("Number of Letters") + ylab("Response Accuracy (%)") + 
  theme(text  = element_text(size = 20),axis.text = axis_style,legend.position = "none") 
ag_cut<-aggregate(TargetResp.corr~N+uq_index,data = bdf,FUN = sum)
ag_cut_a<-ag_cut[which(ag_cut$uq_index %in% id_cut),]
ag_cut_b<-reshape2::dcast(ag_cut_a,uq_index~N,value.var = "TargetResp.corr")
ag_cut_b$tot<-apply(ag_cut_b[2:ncol(ag_cut_b)],1,sum)
ag_cut_c <- apply(ag_cut_b[2:ncol(ag_cut_b)],1,function(x){x[2:8]/x[9]})

###
table(bdf$TargetResp.keys[bdf$id_cut],bdf$N[bdf$id_cut])
###Look into chance discounting:
dist_rate <- 1/1:9 
newcolor = "#637391"
ag_wID <- aggregate(TargetResp.corr~N+uq_index,data = bdf,FUN = mean)
ag_wID$dis_acc<-ag_wID$TargetResp.corr / dist_rate[ag_wID$N]
ag_nID <- aggregate(TargetResp.corr~N,data = bdf,FUN = mean)
ag_nID$dis_acc<-ag_nID$TargetResp.corr / dist_rate[ag_nID$N]
ggplot(bdf,aes(x=N,y=TargetResp.corr),color=newcolor)+
  #geom_histogram(data = aggregate(TargetResp.corr~N,data = bdf,FUN = mean),stat = "identity",alpha=0.2,fill="#0c4a40")+
  geom_point(data=ag_wID,aes(x=N,y=dis_acc),color=newcolor,alpha=0.2,position = position_jitter(width = 0.2))+
  geom_point(data=ag_nID,aes(x=N,y=dis_acc),color=newcolor,size=5)+
  geom_line(data=ag_nID,aes(x=N,y=dis_acc),color=newcolor,linewidth=2)+
  #stat_summary(fun.data=mean_se, fun.args = list(mult=10), geom="errorbar", color=newcolor, width=0.2, size =1) +
  scale_x_continuous(breaks = 3:9,labels=c("3","4","5","6","7","8","9"))+
  xlab("Number of Letters") + ylab("Adj. Response Accuracy Factor") + 
  theme(text  = element_text(size = 20),axis.text = axis_style,legend.position = "none") + 
  geom_hline(yintercept = 1,color="black",linewidth=1) 
ggsave(filename = "S2AAFxL.png",scale = 1.3,width=6,height = 4,units = "in")

summary(sapply(split(bdf$TargetResp.keys,bdf$uq_index),sd,na.rm=T))

### Maybe just plot the whole thing?
summary(mood_Full) -> dfa
as.data.frame(dfa$coefficients) -> dfa

##Plot the mood by the N:
ggplot(bdf,aes(x=N,y=mood_dmean),color="#b181b3")+
  #geom_histogram(data = aggregate(TargetResp.corr~N,data = bdf,FUN = mean),stat = "identity",alpha=0.2,fill="#0c4a40")+
  geom_point(data=aggregate(mood_dmean~N+uq_index,data = bdf,FUN = mean),color="#b181b3",alpha=0.2,position = position_jitter(width = 0.2))+
  geom_point(data=aggregate(mood_dmean~N,data = bdf,FUN = mean),color="#634a63",size=5)+
  geom_line(data=aggregate(mood_dmean~N,data = bdf,FUN = mean),color="#634a63",size=2)+
  stat_summary(fun.data=mean_se, fun.args = list(mult=10), geom="errorbar", color="#634a63", width=0.3, size =1) +
  scale_x_continuous(breaks = 3:9,labels=c("3","4","5","6","7","8","9"))+
  xlab("Number of Letters") + ylab("Happiness Rating (Z-score)") + 
  theme(text  = element_text(size = 20),axis.text = axis_style,legend.position = "none") 
ggsave(filename = "S2MxN.png",scale = 1.3,width=3,height = 4,units = "in")

ggplot(bdf,aes(x=(N),y=slider.response))+ geom_point(alpha=0.1,position = position_dodge2(width = 0.7),color = "rosybrown") + geom_smooth(method = "glm",color="darkred") + 
  ggtitle("Happiness Rating by Difficulty (All Trials)") + xlab("Difficulty (Number of Letters)") + ylab("Happiness Rating")
ggplot(bdf,aes(x=(N),y=slider.response)) + geom_smooth(method = "glm",color="darkred") + 
  ggtitle("Happiness Rating by Difficulty (All Trials)") + xlab("Difficulty (Number of Letters)") + ylab("Happiness Rating")

ggplot(bdf,aes(y=slider.response,x=N),color="#a493b5") + 
  geom_point(position = position_dodge2(width = 1),color="#a493b5",alpha=0.1)+
  geom_line(mapping = aes(fill=uq_index,color=uq_index),stat="smooth",method = "lm", size = 1.5,alpha = 0.3, color="#a493b5")+
  stat_summary(fun.data=mean_cl_boot, fun.args = list(), geom="errorbar", color="#231c2b", width=0.2, size =1) +
  geom_smooth(method="lm",color="#231c2b",fill="#231c2b") +
  xlab("Number of Letters") + ylab("Momentary Happiness Ratings") + theme(text  = element_text(size = 20)) 

###Plot the mood by N but without feedback influence
ggplot(bdf[bdf$fb_tt5==0,],aes(x=(N),y=slider.response))+ geom_point(alpha=0.1,position = position_dodge2(width = 0.7),color = "tan") + geom_smooth(method = "glm",color="tan3") + 
  ggtitle("Happiness Rating by Difficulty (No Feedback)") + xlab("Difficulty (Number of Letters)") + ylab("Happiness Rating")
ggplot(bdf[bdf$fb_tt5==0,],aes(x=(N),y=slider.response)) + geom_smooth(method = "glm",color="tan3") + 
  ggtitle("Happiness Rating by Difficulty (No Feedback)") + xlab("Difficulty (Number of Letters)") + ylab("Happiness Rating")

ggplot(bdf[bdf$fb_tt5==0,],aes(y=slider.response,x=N),color="#a493b5") + 
  geom_point(position = position_dodge2(width = 1),color="#a493b5",alpha=0.1)+
  geom_line(mapping = aes(fill=uq_index,color=uq_index),stat="smooth",method = "lm", size = 1.5,alpha = 0.3, color="#a493b5")+
  stat_summary(fun.data=mean_cl_boot, fun.args = list(), geom="errorbar", color="#231c2b", width=0.2, size =1) +
  geom_smooth(method="lm",color="#231c2b",fill="#231c2b") +
  xlab("Number of Letters") + ylab("Momentary Happiness Ratings") + theme(text  = element_text(size = 20)) 


###Plot mood by trials since last feedback 
ggplot(bdf,aes(x=(nt_sfb),y=slider.response))+ geom_smooth(method = "glm") + 
  ggtitle("Happiness Rating by Number of Trials Since Last Feedback (starting at 0): Fitted Smooth Line Only") + xlab("Number of Trials Since Last Feedback") + ylab("Happiness Rating") 
ggplot(bdf,aes(x=(nt_sfb),y=slider.response))+ geom_smooth(method = "glm") + geom_point(alpha=0.2) + 
  ggtitle("Happiness Rating by Number of Trials Since Last Feedback (starting at 0)") + xlab("Number of Trials Since Last Feedback") + ylab("Happiness Rating")

ggplot(bdf,aes(y=slider.response,x=nt_sfb),color="#a493b5") + 
  geom_point(position = position_dodge2(width = 1),color="#cfd8b2",alpha=0.1)+
  geom_line(mapping = aes(fill=uq_index,color=uq_index),stat="smooth",method = "lm", size = 1.5,alpha = 0.4, color="#71a376")+
  stat_summary(fun.data=mean_cl_boot, fun.args = list(), geom="errorbar", color="#2b4c41", width=0.2, size =1) +
  geom_smooth(method="lm",color="#2b4c41",fill="#2b4c41") +
  xlab("Happiness Rating by Number of Trials Since Last Feedback (starting at 0)") + ylab("Momentary Happiness Ratings") + theme(text  = element_text(size = 20)) 

ggplot(bdf,aes(x=nt_sfb,y=mood_dmean),color="#b181b3")+
  #geom_histogram(data = aggregate(TargetResp.corr~N,data = bdf,FUN = mean),stat = "identity",alpha=0.2,fill="#0c4a40")+
  geom_point(data=aggregate(mood_dmean~nt_sfb+uq_index,data = bdf,FUN = mean),color="#b181b3",alpha=0.2,position = position_jitter(width = 0.2))+
  geom_point(data=aggregate(mood_dmean~nt_sfb,data = bdf,FUN = mean),color="#634a63",size=5)+
  geom_line(data=aggregate(mood_dmean~nt_sfb,data = bdf,FUN = mean),color="#634a63",size=2)+
  stat_summary(fun.data=mean_se, fun.args = list(mult=10), geom="errorbar", color="#634a63", width=0.3, size =1) +
  ylim(2,-2)+
  #scale_x_continuous(breaks = 3:9,labels=c("3","4","5","6","7","8","9"))+
  xlab("Number of Letters") + ylab("Happiness Rating (Z-score)") + 
  theme(text  = element_text(size = 20),axis.text = axis_style,legend.position = "none") 
ggsave(filename = "S2MxN.png",scale = 1.3,width=3,height = 4,units = "in")
##Plot mood by trial 
ggplot(bdf,aes(y=slider.response,x=trial),color="#85d4c7") + 
  geom_point(position = position_dodge2(width = 1),color="#85d4c7",alpha=0.1)+
  geom_line(mapping = aes(fill=participant,color=participant),stat="smooth",method = "lm", size = 1.5,alpha = 0.4, color="#85d4c7")+
  stat_summary(fun.data=mean_cl_boot, fun.args = list(), geom="errorbar", color="#0c4a40", width=0.2, size =0.5) +
  geom_smooth(method="lm",color="#0c453c",fill="#0c4a40") + ylim(c(0,10.5)) +
  xlab("Trial") + ylab("Momentary Happiness Ratings")+ theme(text  = element_text(size = 20)) 

###Feedback accuracy hist 
ggplot(bdf,aes(x=fb_value))+geom_histogram()+ggtitle("Accuracy Rate at Each Feedback Histogram") + ylab("Count") + xlab("Accuracy Rate")
###Feedback accuracy time effect?
ggplot(bdf[bdf$fb_zone %in% 1:6,],aes(x=fb_value,fill=as.factor(fb_zone)))+geom_histogram(bins=40)+
  ggtitle("Accuracy Rate at Each Feedback Histogram") + ylab("Count") + xlab("Accuracy Rate") + scale_fill_discrete(name = "Number of Feedback")
###Feedback accuracy by feedback type (above average or not)
ggplot(bdf,aes(x=(nt_sfb),y=slider.response,color = fb_value > mean(fb_value,na.rm=T)))+ geom_point(alpha = 0.2) + geom_smooth(method = "glm") + 
  ggtitle("Happiness Rating by Number of Trials Since Last Feedback, split by Feedback Type") +
  xlab("Number of Trials Since Last Feedback") + ylab("Happiness Rating") + scale_color_discrete(name = "Positive Feedback")



##maybe a more accurate way is to do lm for everyone
sp_bdf <- split(bdf,bdf$uq_index)
dfxy<-do.call(rbind,lapply(1:length(sp_bdf),function(i){
  x <- sp_bdf[[i]]
  as.data.frame(summary(lm(slider.response~scale(N)+scale(nt_sfb)+scale(trial),data = x))$coefficients) -> xy
  xy$variable <- c("Intercept","N","NTSFB","Trial")
  rownames(xy) <- NULL
  xy$uq_sub <- i
  return(xy)
}))
ggplot(dfxy[dfxy$variable!="Intercept",],aes(x=Estimate)) + geom_histogram(bins = 50)+facet_wrap(~variable)



###Regression Model:
##(1) simple model with only trials and missed
mood_Null<-lmerTest::lmer(slider.response~scale(trial)+missed+(scale(trial)+missed+missed|uq_index),
                        data = bdf,control = lme4::lmerControl(optimizer = "bobyqa"))
##(2) Add influence of number of letters
mood_N<-lmerTest::lmer(slider.response~scale(N)+scale(trial)+missed+(scale(N)+scale(trial)+missed|uq_index),
                        data = bdf,control = lme4::lmerControl(optimizer = "bobyqa"))
##(3) Full model: Add influence of trials since last feedback
mood_Full<-lmerTest::lmer(slider.response~scale(N)+fb_yn+scale(nt_sfb)+scale(trial)+(scale(N)+fb_yn+scale(nt_sfb)+scale(trial)|uq_index),
                        data = bdf,control = lme4::lmerControl(optimizer = "bobyqa"))
##(4) Add "I feel like getting it wrong" effect 
mood_SF_cor<-lmerTest::lmer(slider.response~scale(N)+scale(trial)+scale(nt_sfb)+as.factor(TargetResp.corr==0)+missed+(scale(N)+scale(trial)+scale(nt_sfb)+as.factor(TargetResp.corr==0)+missed|uq_index),
                        data = bdf,control = lme4::lmerControl(optimizer = "bobyqa"))
##(5) Full model [3] but on trials without feedback influence (feedback + 5 t after)
mood_SF_noFB<-lmerTest::lmer(slider.response~scale(N)+scale(trial)+scale(nt_sfb)+missed+(scale(N)+scale(trial)+scale(nt_sfb)+missed|uq_index),
                        data = bdf[bdf$fb_tt5==0,],control = lme4::lmerControl(optimizer = "bobyqa"))
##(6) Full model [3] but 1) on full data including otherwise excluded participants based on accuracy; 
#########################2) included term to differentiate different types of participants (split by accurate trial number > 49)
mood_SF_cb<-lmerTest::lmer(slider.response~scale(N)*par_type+scale(trial)+scale(nt_sfb)+missed+
                             (scale(N)*par_type+scale(trial)+scale(nt_sfb)+missed|uq_index),
                           data = cdf,control = lme4::lmerControl(optimizer = "bobyqa"))
##(7) Same as (6) but on trials without influence of feedback only
mood_SF_cbnoFB<-lmerTest::lmer(slider.response~scale(N)*par_type+scale(trial)+scale(nt_sfb)+missed+
                                          (scale(N)*par_type+scale(trial)+scale(nt_sfb)+missed|uq_index),
                        data = cdf[cdf$fb_tt5==0,],control = lme4::lmerControl(optimizer = "bobyqa"))
##(8) Look into whether objective correctness has anything to do with mood
bdf$correct <- factor(bdf$TargetResp.corr)
mood_SF_objcor<-lmerTest::lmer(slider.response~scale(N)*correct+scale(trial)+scale(nt_sfb)+missed+(scale(N)*correct+scale(trial)+scale(nt_sfb)+missed|uq_index),
                          data = bdf,control = lme4::lmerControl(optimizer = "bobyqa"))
##(9) The investigation on individual differences in performance
bdf$act <- scale(sum_df$act)[match(bdf$uq_index,sum_df$uq_index)]
bdf$acc_per <- scale(sum_df$acc_per)[match(bdf$uq_index,sum_df$uq_index)]
bdf$err_per <- scale((210 - sum_df$act) / 210)[match(bdf$uq_index,sum_df$uq_index)]
mood_SF_idp<-lmerTest::lmer(slider.response~scale(N)*err_per+scale(trial)+scale(nt_sfb)+missed+(scale(N)*err_per+scale(trial)+scale(nt_sfb)+missed|uq_index),
                               data = bdf,control = lme4::lmerControl(optimizer = "bobyqa", optCtrl = list(maxfun = 100000)))

##(10) Early/mid/late portion of the task's effect; to show that later on without reward, the participants are more likely to 
bdf$stage <- ceiling(bdf$trial / (max(bdf$trial)/3)  )-1
bdf$stage_fa <- as.factor(bdf$stage)
bdf$N_s <- scale(bdf$N)
mood_SF_stg<-lmerTest::lmer(slider.response~scale(N)*stage+scale(nt_sfb)+missed+
                             (scale(N)*stage+scale(nt_sfb)+missed|uq_index),
                           data = bdf,control = lme4::lmerControl(optimizer = "bobyqa"))
mood_SF_stg_fa<-lmerTest::lmer(slider.response~scale(N)*stage_fa++scale(nt_sfb)+missed+
                              (scale(N)*stage_fa+scale(nt_sfb)+missed|uq_index),
                            data = bdf[bdf$N %in% 3:7,],control = lme4::lmerControl(optimizer = "bobyqa"))
mood_SF_trial <- lmerTest::lmer(slider.response~scale(N)*scale(trial)+scale(nt_sfb)+missed+
                                  (scale(N)*scale(trial)+scale(nt_sfb)+missed|uq_index),
                                data = bdf,control = lme4::lmerControl(optimizer = "bobyqa"))


ggplot(bdf[!is.na(bdf$TargetResp.corr),],aes(x=N,y=TargetResp.corr,color=stage_fa))+
  stat_summary(fun.data=mean_cl_boot, fun.args = list(), geom="point", size =4) +
  stat_summary(fun.data=mean_cl_boot, fun.args = list(), geom="line", linewidth=2) +
  stat_summary(fun.data=mean_cl_boot, fun.args = list(), geom="errorbar", width=0.3, size =1) +
  xlab("Number of Letters") + ylab("Response Accuracy (%)") +
  scale_x_continuous(breaks = 3:9,labels=c("3","4","5","6","7","8","9"))+
  scale_color_manual(name = "Stages", labels = c("Early", "Mid","Late"), values=c("#69b6c7","#22a3bf","#076478")) +  
  theme(text  = element_text(size = 20),axis.text = axis_style) 
ggsave(filename = "S1_t_accu.png",scale = 1.3,width=5,height = 3,units = "in")

ggplot(bdf,aes(x=N,y=mood_dmean,color=stage_fa))+
  stat_summary(fun.data=mean_cl_boot, fun.args = list(), geom="point", size =4) +
  stat_summary(fun.data=mean_cl_boot, fun.args = list(), geom="line", linewidth=2) +
  stat_summary(fun.data=mean_cl_boot, fun.args = list(), geom="errorbar", width=0.3, size =1) +
  xlab("Number of Letters") + ylab("Happiness Rating (Z-score)") + 
  scale_x_continuous(breaks = 3:9,labels=c("3","4","5","6","7","8","9"))+
  scale_color_manual(name = "Stages", labels = c("Early", "Mid","Late"), values=c("#d7de81","#cbd453","#565c0e")) +  
  theme(text  = element_text(size = 20),axis.text = axis_style) 
ggsave(filename = "S1_t_mood.png",scale = 1.3,width=5,height = 3,units = "in")

ggplot(bdf,aes(x=trial,y=mood_dmean),color="#d1c84f")+
  #stat_summary(fun.data=mean_cl_boot, fun.args = list(), geom="point", size =4,color="#d1c84f") +
  #stat_summary(fun.data=mean_cl_boot, fun.args = list(), geom="line", linewidth=2,color="#d1c84f") +
  #stat_summary(fun.data=mean_cl_boot, fun.args = list(), geom="errorbar", width=0.3, size =1,color="#d1c84f") +
  #geom_point(size=0.5,alpha=0.01,color="#d1c84f")+
  geom_smooth(color="#d1c84f",level=.95) +
  xlab("Number of Trial") + ylab("Happiness Rating (Z-score)") + 
  #scale_x_continuous(breaks = 3:9,labels=c("3","4","5","6","7","8","9"))+
  #scale_color_manual(name = "Stages", labels = c("Early", "Mid","Late"), values=c("#d7de81","#cbd453","#565c0e")) +  
  theme(text  = element_text(size = 20),axis.text = axis_style) 
ggsave(filename = "S1_t_moodSmooth.png",scale = 1.3,width=5,height = 3,units = "in")
##(11) Exp N
bdf$N_scl_sq <- scale(bdf$N)^2
mood_SF_sq<-lmerTest::lmer(slider.response~scale(N)+N_scl_sq+scale(nt_sfb)+missed+
                              (scale(N)+N_scl_sq+scale(nt_sfb)+missed|uq_index),
                            data = bdf[bdf$fb_tt5==0,],control = lme4::lmerControl(optimizer = "bobyqa"))

##Graphing the results:
coefficients(mood_Full)$uq_index -> dfx
names(dfx) <- c("Intercept","N","NTSFB","Trial")
dfx$uq <- 1:nrow(dfx)
dfy<-reshape2::melt(dfx,id.vars="uq")
dfy$variable <- as.factor(dfy$variable)
dfy$Estimate <- dfy$value

ggplot(dfy[dfy$variable!="Intercept",],aes(x=value)) + geom_histogram(bins = 50)+facet_wrap(~variable)

summary(mood_Full)-> dfz
as.data.frame(dfz$coefficients) -> dfz
dfz$variable <- as.factor(names(dfx)[!names(dfx) %in% c("uq")])
dfz$se <- dfz$`Std. Error`
dfz$upper <- dfz$Estimate + 2*dfz$se
dfz$lower <- dfz$Estimate - 2*dfz$se

ggplot(dfz[dfz$variable!="Intercept",],aes(x=variable,y=Estimate,color=variable)) + 
  geom_point(data=dfy[dfy$variable!="Intercept",],aes(x=variable,y=value,color=variable),alpha=0.1,position = position_jitter(width = 0.2))+
  geom_hline(yintercept = 0,alpha=0.5) +
  geom_point(size=5) +  ylim(c(-0.6,0.6))+
  geom_errorbar(aes(ymax=upper,ymin=lower),width=0.1,size=1) + 
  xlab("Variable") + ylab("Estimated Regression Coefficient") + 
  theme(text  = element_text(size = 20),legend.position = "none",axis.title.x=element_blank()) +
  scale_color_manual(values=c("#9c8936","#60965a","#bd3a41","#5f2cbf"))
ggsave(filename = "S2Regression.png",scale = 1.3,width=2522,height = 1782,units = "px")



bdf$TargetResp.rt
bdf$rt_log <- log(bdf$TargetResp.rt)
bdf$rt_scale <- unlist(lapply(split(bdf$TargetResp.rt,bdf$uq_index),scale))
bdf$id_cutlab <- ifelse(bdf$id_cut,"Cluster Outlier","Rest of the Sample")
##First graph it
ggplot(bdf[!is.na(bdf$rt_log),],aes(x=N,y=TargetResp.rt),color="#284E57")+
  geom_point(color="#284E57",alpha=0.01,position = position_jitter(width = 0.2))+
  #geom_point(color="#284E57",size=5)+
  #geom_line(color="#284E57",linewidth=2)+
  stat_summary(fun.data=mean_sdl, fun.args = list(mult=1), geom="point", color="#0c4a40", size =5) +
  stat_summary(fun.data=mean_sdl, fun.args = list(mult=1), geom="line", color="#0c4a40", linewidth =2) +
  stat_summary(fun.data=mean_sdl, fun.args = list(mult=1), geom="errorbar", color="#0c4a40", width=0.2, size =1) +
  #scale_x_continuous(breaks = 3:9,labels=c("3","4","5","6","7","8","9"))+
  xlab("Number of Letters") + ylab("Response Reaction Time") + 
  theme(text  = element_text(size = 20),axis.text = axis_style,legend.position = "none") 
ggsave(filename = "E02_rt.png",scale = 1.3,width=5,height = 3,units = "in")

RT_Full<-lmerTest::lmer(log(TargetResp.rt)~scale(N)+scale(trial)+(scale(N)+scale(trial)|uq_index),
                          data = bdf,control = lme4::lmerControl(optimizer = "bobyqa"))
#