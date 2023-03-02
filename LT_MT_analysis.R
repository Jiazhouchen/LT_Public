source("letter_utility.R")
library(ggplot2)
library(latex2exp)
dataset_name <- "LT_extend"
reload <- F
expected_trial <- 150
rdata_fname <- file.path(".","data",dataset_name,paste0(dataset_name,".rdata"))
if(!reload && file.exists(rdata_fname)) {
  load(rdata_fname)
} else {
  ls_csvs <- list.files(path = dirname(rdata_fname),pattern = "*.csv", recursive = F,include.dirs = T,full.names = T)
  ID_map <- read.csv(file = "./ID_mturk.csv")
  all_data <- lapply(ls_csvs,read.csv,stringsAsFactors = F)
  proc_data <- lapply(all_data,proc_func)
  proc_data <- proc_data[!sapply(proc_data, is.null)]
  all_varsx <- unique(unlist(lapply(proc_data,names)))
  proc_data <- lapply(proc_data,function(xd){
    xd[all_varsx[!all_varsx %in% names(xd)]] <- NA
    return(xd)
  })
  names(proc_data) <- sapply(proc_data,function(x){unique(x$participant)})
  message("### Total of ",length(proc_data)," processed ###")
  save(proc_data,ID_map,file = rdata_fname)
}

#temp proc 

proc_data <- lapply(proc_data,function(dx){
  dx$cu_natt <- cumsum(dx$nattempt)
  dx$cu_natt_s <- scale(dx$cu_natt,center = F)
  dx$cu_natt_lag <- c(NA,dx$cu_natt[1:(nrow(dx)-1)])
  dx$cu_natt_s_lag <- c(NA,dx$cu_natt_s[1:(nrow(dx)-1)])
  dx$mood_dmean <- scale(dx$slider.response)
  
  dx$failed <- !dx$win
  dx$failed_lead1 <- c(dx$failed[2:nrow(dx)],NA)
  dx$failed_lag1 <- c(NA,dx$failed[1:(nrow(dx)-1)])
  dx$failed_lag2 <- c(NA,NA,dx$failed[1:(nrow(dx)-2)])
  dx$failed_lag3 <- c(NA,NA,NA,dx$failed[1:(nrow(dx)-3)])
  dx$failed_lag4 <- c(NA,NA,NA,NA,dx$failed[1:(nrow(dx)-4)])
  
  dx$firstattwin <- dx$nattempt==1
  dx$firstattwin_lag1 <- c(NA,dx$firstattwin[1:(nrow(dx)-1)])
  dx$firstattwin_lag2 <- c(NA,NA,dx$firstattwin[1:(nrow(dx)-2)])
  dx$firstattwin_lag3 <- c(NA,NA,NA,dx$firstattwin[1:(nrow(dx)-3)])
  dx$firstattwin_lag4 <- c(NA,NA,NA,NA,dx$firstattwin[1:(nrow(dx)-4)])
  dx$firstattwin_lag5 <- c(NA,NA,NA,NA,NA,dx$firstattwin[1:(nrow(dx)-5)])
  dx$firstattwin_lag6 <- c(NA,NA,NA,NA,NA,NA,dx$firstattwin[1:(nrow(dx)-6)])
  
  dx$rewMag_cat <- round(dx$rewMag/10,0) * 10
  dx$pt_adj <- (dx$rewMag_cat/ 10) * dx$win
  dx$pt_dist <- dx$pt_adj
  
  dx$eff <- dx$pt_adj / dx$N
  dx$eff_exp <- dx$pt_adj / dx$nattempt
  
  dx$avg_eff_exp <- mean(dx$eff_exp)
  dx$avg_eff <- mean(dx$eff)
  
  
  dx$slider.response[dx$slider.rt > 5] <- NA
  
  dx$avg_mood <- mean(dx$slider.response,na.rm=T)
  return(dx)
})

summary_data <- do.call(rbind,lapply(proc_data,function(xd){
  #print(unique(xd$participant))
  if(is.null(xd$ViewDura)){
    xd$ViewDura <- 5
  }
  if (!is.null(xd$choice_key.keys)) {
    bias<-mean(as.numeric(xd$choice_key.keys=="j"))
  } else {
    bias<-NA
  }
  data.frame(prolific_pid = unique(xd$participant),
             dataset_name = dataset_name,
             session = unique(xd$session),
             ntrial = nrow(xd),
             mood_var = sd(xd$slider.response,na.rm = T),
             baseline_mood = unique(xd$blmood_response),
             endofstudy_mood = xd$slider.response[nrow(xd)],
             accuracy_rate = length(which(xd$TargetResp.corr==1)) / nrow(xd),
             win_per = mean(as.numeric(xd$win)),
             min_N = min(xd$N),
             total_nattempt = sum(xd$nattempt,na.rm = T),
             avg_nattempt = mean(xd$nattempt,na.rm=T),
             avg_nattempt_min = mean(xd$nattempt[xd$N==min(xd$N)]),
             avg_nattempt_per_trial = sum(xd$nattempt,na.rm = T) / nrow(xd),
             aN_ratio = xd$cu_natt[nrow(xd)] / sum(xd$N),
             left_right_bias = bias,
             total_earning = sum(as.numeric(gsub(" pts","",xd$rewMag)) * xd$TargetResp.corr),
             OS= unique(xd$OS),
             skip=unique(xd$skip),
             ViewDura = unique(xd$ViewDura),
             exclude = "NO",
             date=unique(sapply(strsplit(xd$date,"_"),`[[`,1)),
             stringsAsFactors = F)
}))
summary_data$baseline_mood_s<-scale(summary_data$baseline_mood)
summary_data$bonus_payment <- round(1.5 * summary_data$accuracy_rate * (summary_data$ntrial /180),2)

######Removing questionable IDs#######
if(any(duplicated(summary_data$prolific_pid))){
  message(paste(summary_data$prolific_pid[duplicated(summary_data$prolific_pid)],collapse = ", ")," has duplicate")
}
dup_ID <- summary_data$prolific_pid[which(summary_data$prolific_pid %in% ID_map$WorkerId[ID_map$Count>1])]
if(length(dup_ID)>0) {
  message("total of ",length(dup_ID),": ",paste(dup_ID,collapse = ", ")," have previsouly participated")
  summary_data$exclude[which(summary_data$prolific_pid %in% dup_ID)] <- paste(summary_data$exclude[which(summary_data$prolific_pid %in% dup_ID)],"PrevPart",sep=", ")
} 

summary_data$exclude[summary_data$ntrial/expected_trial <0.9]  <- paste(summary_data$exclude[summary_data$ntrial/expected_trial <0.9],"low trial",sep = ", ")
norm_cutoff <- mean(summary_data$avg_nattempt) + (sd(summary_data$avg_nattempt)*2.576)
summary_data$exclude[summary_data$avg_nattempt > norm_cutoff] <- paste(summary_data$exclude[summary_data$avg_nattempt > norm_cutoff],"high attempt",sep = ", ")
summary_data$exclude <- gsub("^NO, ","",summary_data$exclude)
message("Total of ",length(summary_data$prolific_pid[which(summary_data$exclude!="NO")])," was excluded")


bdf <- do.call(rbind,proc_data[which(names(proc_data) %in% summary_data$prolific_pid[summary_data$exclude=="NO"])])
bdf$dataset <- dataset_name

message("Total sample size: ",length(unique(bdf$participant)))

####Fixed re-scaling:
bdf$N_scale <- bdf$N-min(bdf$N)+1
###Getting some rt variant:
bdf$init_rt <- sapply(bdf$TargetResp_lsrt,`[[`,1)
bdf$effort.ran[is.na(bdf$effort.ran)] <- 0 
#exclusion: #at least have 20% accuracy 





###Model Fit graph: 
if(is.null(bdf$editDistance)) {bdf$editDistance <- 2}
bdf$`Edit Distance` <- factor(bdf$editDistance)
bdf$`N Letter` <- factor(bdf$N,levels = 1:10)
bdf$`N Attempt` <- factor(bdf$nattempt,levels = 1:10)
bdf$rew_upplow <- as.factor(floor(bdf$rewMag/40))
bdf$cor_in <- factor(ifelse(bdf$TargetResp.corr,"Correct","Incorrect"))
bdf$rewMag_cat <- round(bdf$rewMag/10,0) * 10

bdf$rel_mood <- bdf$slider.response - bdf$blmood_response






bdf$eff_eq <- bdf$eff == 1
bdf$eff_pn <- bdf$eff > 1
bdf$eff_pn[bdf$eff == 1] <- NA
#bdf$eff_pn[bdf$eff == 0] <- NA


bdf$eff_eqexp <- bdf$eff_exp == 1
bdf$eff_pnexp <- bdf$eff_exp > 1
bdf$eff_pnexp[bdf$eff_exp == 1] <- NA
#bdf$eff_pnexp[bdf$eff_exp == 0] <- NA

bdf$eff_avgexpfa <- bdf$eff_exp > bdf$avg_eff_exp 
bdf$eff_avgexpfa[bdf$eff_exp == bdf$avg_eff_exp ] <- NA

if(!is.null(bdf$c1_cor_pos)){
  bdf$c1_eff <- (bdf$c1_pt/10) / bdf$c1_n
  bdf$c2_eff <- (bdf$c2_pt/10) / bdf$c2_n
  
  bdf$pt_diff <- (bdf$c2_pt - bdf$c1_pt)/10
  bdf$e_diff <- (bdf$c2_n - bdf$c1_n)
  bdf$ef_diff <- bdf$c2_eff - bdf$c1_eff
  
  
  bdf$choice<-bdf$choice_key.keys == "j"
  #bdf <- bdf[bdf$e_diff!=0,]
  
  bdf$e_rational <- NA
  bdf$e_rational[bdf$ef_diff > 0 & bdf$choice] <- TRUE
  bdf$e_rational[bdf$ef_diff < 0 & bdf$choice] <- FALSE
  bdf$e_rational[bdf$ef_diff > 0 & !bdf$choice] <- FALSE
  bdf$e_rational[bdf$ef_diff < 0 & !bdf$choice] <- TRUE
}

bdf$success <- !bdf$failed




#scale by subject 
vn <- c("trial","N","rewMag","nattempt","eff","eff_exp","pt_adj")
vx <- c("rel_mood")
bdf<-do.call(rbind,lapply(split(bdf,bdf$participant),function(spx){
  
  
  for(x in vn) {
    spx[[paste0(x,"_s")]] <- scale(spx[[x]],center = F,scale = T)
  }
  for(x in vx) {
    spx[[paste0(x,"_s")]] <- scale(spx[[x]],center = T,scale = T)
  }
  return(spx)
}))

bdf$mood_var<-summary_data$mood_var[match(bdf$participant,summary_data$prolific_pid)]
bdf$baseline_mood_s<-summary_data$baseline_mood_s[match(bdf$participant,summary_data$prolific_pid)]
row.names(bdf) <- NULL
assign(dataset_name,bdf)
if (F) {
  
  ##################################
  ##### Number of Attempts #########
  ##################################
  
  nattempt_M1R <- lmerTest::lmer(nattempt~N_s+trial_s+(N_s+trial_s|participant),data = bdf)
  
  # ggplot(data = bdf,aes(y=nattempt,x=as.factor(N)))+ geom_point(position = position_jitter(),alpha = 1,color="dark grey")  + 
  #   geom_histogram(stat="summary",alpha=0.6,fill="#8a2d37",color="#4a262a") + 
  #   geom_smooth(mapping = aes(y=nattempt,x=N-2),size=2, color = "#8a2d37") + 
  #   stat_summary(fun.data=mean_cl_boot, geom="errorbar", color="#4a262a", width=0.2, size =1) +
  #   ylab("Number of Errors") + xlab("Number of Letters") + 
  #   theme(text  = element_text(size = 20))  
  
  ggplot(bdf,aes(x=N,y=nattempt),color="#284E57")+
    geom_point(data=aggregate(nattempt~N+participant,data = bdf,FUN = mean),color="#b04e2e",alpha=0.2,position = position_jitter(width = 0.2))+
    geom_point(data=aggregate(nattempt~N,data = bdf,FUN = mean),color="#b04e2e",size=5)+
    geom_line(data=aggregate(nattempt~N,data = bdf,FUN = mean),color="#b04e2e",size=2)+
    stat_summary(fun.data=mean_se, fun.args = list(mult=10), geom="errorbar", color="#b04e2e", width=0.2, size =1) +
    scale_x_continuous(breaks = 3:9,labels=c("3","4","5","6","7","8","9"))+
    ylab("Number of Errors") + xlab("Number of Letters") + 
    theme(text  = element_text(size = 20),axis.text = axis_style) 
  ggsave(filename = "S1ExL.png",scale = 1.3,width=3,height = 4,units = "in")
  
  ##################################
  
  
  ##################################
  ############Mood Models###########
  ##################################
  nattmpt_M1R_bay<-rstanarm::stan_glmer(formula = nattempt~N_s+rewMag_s+trial_s+(N_s+rewMag_s|participant),data=bdf,family="ordinal")
  mood_M2R_bay<-rstanarm::stan_glmer(slider.response~nattempt_s+rewMag_s+eff_exp_s+trial_s+(nattempt_s+rewMag_s+eff_exp_s|participant),data = bdf)
  mood_M2S_bay<-rstanarm::stan_glmer(slider.response~nattempt_s+rewMag_s+trial_s+(nattempt_s+rewMag_s|participant),data = bdf)
  
  
  
  #Reporting:
  
  mood_M0R<-lmerTest::lmer(slider.response~pt_adj_s+
                             trial_s+(pt_adj_s+trial_s|participant),
                           data = bdf,
                           control = lme4::lmerControl(optimizer = "bobyqa"))
  
  mood_M0E<-lmerTest::lmer(slider.response~N_s+
                             trial_s+(N_s+trial_s|participant),
                           data = bdf,
                           control = lme4::lmerControl(optimizer = "bobyqa"))
  
  mood_M0Ex<-lmerTest::lmer(slider.response~nattempt_s+
                              trial_s+(nattempt_s+trial_s|participant),
                            data = bdf,
                            control = lme4::lmerControl(optimizer = "bobyqa"))
  
  mood_M1<-lmerTest::lmer(slider.response~pt_adj_s+N_s+
                            trial_s+(pt_adj_s+N_s+trial_s|participant),
                          data = bdf[bdf$nattempt==1,],
                          control = lme4::lmerControl(optimizer = "bobyqa"))
  
  mood_M2<-lmerTest::lmer(slider.response~N_s+nattempt_s+pt_adj_s+
                            trial_s+(N_s+ nattempt_s+pt_adj_s+trial_s|participant),
                          data = bdf,
                          control = lme4::lmerControl(optimizer = "bobyqa"))
  
  mood_M2<-lmerTest::lmer(slider.response~N_s+nattempt_s+pt_adj_s+
                            trial_s+(N_s+ nattempt_s+pt_adj_s+trial_s|participant),
                          data = bdf,
                          control = lme4::lmerControl(optimizer = "bobyqa"))
  # mood_M2<-lmerTest::lmer(slider.response~nattempt_s*avg_mood+pt_adj_s*avg_mood+
  #                           trial_s*avg_mood+(nattempt_s*avg_mood+pt_adj_s*avg_mood+
  #                                                      trial_s*avg_mood|participant),
  #                         data = bdf,
  #                         control = lme4::lmerControl(optimizer = "bobyqa"))
  # 
  coefficients(mood_M2)$participant -> dfx
  names(dfx) <- c("Intercept","N","Error","Reward Magnitude","Trial")
  dfx$uq <- 1:nrow(dfx)
  dfy<-reshape2::melt(dfx,id.vars="uq")
  dfy$variable <- as.factor(dfy$variable)
  dfy$Estimate <- dfy$value
  
  summary(mood_M2)-> dfz
  as.data.frame(dfz$coefficients) -> dfz
  dfz$variable <- as.factor(names(dfx)[!names(dfx) %in% c("uq")])
  dfz$se <- dfz$`Std. Error`
  dfz$upper <- dfz$Estimate + 2*dfz$se
  dfz$lower <- dfz$Estimate - 2*dfz$se
  
  conf_M2<-confint(mood_M2,method="boot",level = 0.95,nsim=50)
  conf_M2<-conf_M2[which(!grepl("sig",rownames(conf_M2))),]
  dfz$lower <- conf_M2[,1]
  dfz$upper <- conf_M2[,2]
  
  dfy <- dfy[dfy$variable!="Intercept",]
  dfz <- dfz[dfz$variable!="Intercept",]
  dfz$participant <- "none"
  dfy$participant <- paste("pt",dfy$uq,sep = "_")
  dfy$x_num <- as.numeric(as.factor(dfy$variable))
  axis_style <- element_text(face = "bold.italic", color = "black", size = 20)
  #   ggplot(data=dfy,aes(y=Estimate,x=x_num,fill=participant)) + 
  #    # geom_point(alpha=0.5) + 
  #     geom_line(alpha=0.5) + 
  #     geom_point(data = dfy[dfy$variable=="N",],aes(y=Estimate,x=2),color="#9c8936",alpha=0.2)+
  #     geom_point(data = dfz[dfz$variable=="N",],aes(y=Estimate,x=2,fill="none"),color="#9c8936",size=5,alpha=0.8)+
  #     geom_errorbar(data = dfz[dfz$variable=="N",],aes(ymax=upper,ymin=lower,x=2),width=0.25,color="#9c8936",size=1) + 
  #     geom_point(data = dfy[dfy$variable=="Error",],aes(y=Estimate,x=3),color="#c96e34",alpha=0.2)+
  #     geom_point(data = dfz[dfz$variable=="Error",],aes(y=Estimate,x=3,fill="none"),color="#c96e34",size=5)+
  #     geom_errorbar(data = dfz[dfz$variable=="Error",],aes(ymax=upper,ymin=lower,x=3),width=0.25,color="#c96e34",size=1) + 
  #     geom_point(data = dfy[dfy$variable=="Reward Magnitude",],aes(y=Estimate,x=4),color="#7bbf2c",alpha=0.2)+
  #     geom_point(data = dfz[dfz$variable=="Reward Magnitude",],aes(y=Estimate,x=4,fill="none"),color="#7bbf2c",size=5)+
  #     geom_errorbar(data = dfz[dfz$variable=="Reward Magnitude",],aes(ymax=upper,ymin=lower,x=4),width=0.25,color="#7bbf2c",size=1) + 
  #     geom_point(data = dfy[dfy$variable=="Trial",],aes(y=Estimate,x=5),color="#5f2cbf",alpha=0.2)+
  #     geom_point(data = dfz[dfz$variable=="Trial",],aes(y=Estimate,x=5,fill="none"),color="#5f2cbf",size=5)+
  #     geom_errorbar(data = dfz[dfz$variable=="Trial",],aes(ymax=upper,ymin=lower,x=5),width=0.25,color="#5f2cbf",size=1) + 
  #     geom_hline(yintercept = 0, color = "grey") +
  #     scale_x_continuous(breaks=2:5,labels=c("n","e","r","t")) + xlab("Variables") +
  #     theme(text  = element_text(size = 20),axis.text = axis_style,legend.position = "none") 
  # #axis.title.x=element_blank()
  #   ggsave(filename = "S1Regression.png",scale = 1.3,width=2522,height = 1782,units = "px")
  
  ggplot(dfz,aes(x=variable,y=Estimate,color=variable)) + 
    scale_x_discrete(labels=c("n","e","r","t")) +
    geom_point(data=dfy,aes(x=variable,y=Estimate),alpha=0.2,position = position_jitter(width = 0.2))+
    geom_errorbar(aes(ymax=upper,ymin=lower),width=0.5,size=2) + 
    geom_hline(yintercept = 0,alpha=0.5) +
    geom_point(size=5) + 
    #ylim(c(-2,2))+
    # geom_line(data=dfy[dfy$variable!="Intercept",],aes(x=variable,y=value,color=as.factor(uq))) + 
    xlab(" ") + ylab("Estimated Regression Coefficient") + 
    theme(text  = element_text(size = 20),axis.text = axis_style,legend.position = "none")+
    scale_color_manual(values=c("#9c8936","#c96e34","#7bbf2c","#5f2cbf"))
  ggsave(filename = "S1Regression.png",scale = 1.3,width=3,height = 4,units = "in")
  
  
  mood_M3<-lmerTest::lmer(slider.response~nattempt_s+pt_adj_s+eff_exp_s+failed+
                            trial_s+(nattempt_s+pt_adj_s+eff_exp_s+failed+trial_s|participant),
                          data = bdf,
                          control = lme4::lmerControl(optimizer = "bobyqa"))
  
  mood_M4<-lmerTest::lmer(slider.response~nattempt_s*pt_adj_s+failed+
                            trial_s+(nattempt_s*pt_adj_s+failed+trial_s|participant),
                          data = bdf,
                          control = lme4::lmerControl(optimizer = "bobyqa"))
  
  #########
  mood_M1I<-lmerTest::lmer(slider.response~N_s*rewMag_s+
                             trial_s+(N_s*rewMag_s|participant),
                           data = bdf,
                           control = lme4::lmerControl(optimizer = "bobyqa"))
  
  mood_M1R<-lmerTest::lmer(slider.response~N_s+rewMag_s+eff_s+
                             trial_s+(N_s+rewMag_s+eff_s|participant),
                           data = bdf,
                           control = lme4::lmerControl(optimizer = "bobyqa"))
  
  
  mood_M2S<-lmerTest::lmer(slider.response~nattempt_s+rewMag_s+
                             trial_s+(nattempt_s+rewMag_s|participant),
                           data = bdf[bdf$win,],
                           control = lme4::lmerControl(optimizer = "bobyqa"))
  
  
  
  mood_M2I<-lmerTest::lmer(slider.response~nattempt_s*rewMag_s+
                             trial_s+(nattempt_s*rewMag_s|participant),
                           data = bdf,
                           control = lme4::lmerControl(optimizer = "bobyqa"))
  
  
  mood_M2Lag<-lmerTest::lmer(slider.response~nattempt_s+rewMag_s+nattempt_lag+
                               trial_s+(nattempt_s+rewMag_s+nattempt_lag|participant),
                             data = bdf,
                             control = lme4::lmerControl(optimizer = "bobyqa"))
  
  mood_M2R<-lmerTest::lmer(slider.response~nattempt_s+pt_adj_s+eff_exp_s+
                             trial_s+(nattempt_s+pt_adj_s+eff_exp_s+trial_s|participant),
                           data = bdf,
                           control = lme4::lmerControl(optimizer = "bobyqa"))
  
  mood_M2R_r<-lmerTest::lmer(slider.response~nattempt_s+pt_adj_s+eff_exp_s+failed+trial_s+
                               (nattempt_s+pt_adj_s+eff_exp_s+failed+trial_s|participant),
                             data = bdf,
                             control = lme4::lmerControl(optimizer = "bobyqa"))
  
  mood_M2_sumrt<-lmerTest::lmer(slider.response~nattempt_s+pt_adj_s+failed+sum_rt_s*N_s+
                                  trial_s+(nattempt_s+pt_adj_s+failed+trial_s+sum_rt_s*N_s|participant),
                                data = bdf,
                                control = lme4::lmerControl(optimizer = "bobyqa"))
  
  mood_M2_nx_att<-lmerTest::lmer(slider.response~nattempt_s+pt_adj_s+failed+nx_att+
                                   trial_s+(nattempt_s+pt_adj_s+failed+trial_s+nx_att|participant),
                                 data = bdf,
                                 control = lme4::lmerControl(optimizer = "bobyqa"))
  
  
  
  mood_M2_perform<-lmerTest::lmer(slider.response~nattempt_s*avg_nattempt_per_trial+pt_adj_s*avg_nattempt_per_trial+failed+
                                    trial_s+(nattempt_s+pt_adj_s+failed+trial_s|participant),
                                  data = bdf,
                                  control = lme4::lmerControl(optimizer = "bobyqa"))
  
  mood_M2_nx_att<-lmerTest::lmer(slider.response~N_s+pt_adj_s+firstattwin+
                                   firstattwin_lag1+firstattwin_lag2+firstattwin_lag3+firstattwin_lag4+firstattwin_lag5+firstattwin_lag6+
                                   trial_s+(pt_adj_s+trial_s+N_s+firstattwin_lag1+firstattwin_lag2+firstattwin_lag3+firstattwin_lag4+firstattwin_lag5+firstattwin_lag6|participant),
                                 data = bdf,
                                 control = lme4::lmerControl(optimizer = "bobyqa"))
  
  coefficients(mood_M2_nx_att)$participant -> dfx
  dfx <- dfx[grepl("firstattwin_",names(dfx))]
  dfx$uq <- 1:nrow(dfx)
  dfy<-reshape2::melt(dfx,id.vars="uq")
  dfy$variable<-gsub(pattern = "*[^1-6]*","",dfy$variable)
  summary(mood_M2_nx_att)-> dfz
  as.data.frame(dfz$coefficients) -> dfz
  dfz$variable <- gsub("*[^1-6]*","",rownames(dfz))
  dfz <- dfz[dfz$variable!="",]
  dfz$se <- dfz$`Std. Error`
  dfz$upper <- dfz$Estimate + 2*dfz$se
  dfz$lower <- dfz$Estimate - 2*dfz$se
  dfy$Estimate <- dfy$value
  ggplot(dfz,aes(x=variable,y=Estimate)) + 
    geom_point(data=dfy,alpha=0.2,color="#557363",position = position_jitter(width = 0.2))+
    geom_hline(yintercept = 0,alpha=0.5) +
    geom_point(size=5,color="#557363") + 
    geom_line(data = dfz,mapping = aes(x=as.numeric(variable),y=Estimate),size=2,color="#557363") +
    geom_errorbar(aes(ymax=upper,ymin=lower),width=0.2,size=1,color="#557363") + 
    ylim(-0.1,0.5) +
    xlab("Time Steps (Lagged)") + ylab("Momentary Mood Ratings") + theme(text  = element_text(size = 20)) 
  ggsave(filename = "S1MxTS.png",scale = 1.3,width=2522,height = 1782,units = "px")
  
  bdf$stage <- ceiling(bdf$trial / (max(bdf$trial)/3))
  bdf$uq_index <- bdf$participant
  bdf$stage_fa <- as.factor(bdf$stage)
  bdf$mood_dmean<-do.call(c,lapply(split(bdf$slider.response,bdf$participant),function(x){as.numeric(scale(x,scale = T,center=T))}))
  ggplot(bdf,aes(x=nattempt,y=mood_dmean,color=stage_fa))+
    #geom_histogram(data = aggregate(TargetResp.corr~N,data = bdf,FUN = mean),stat = "identity",alpha=0.2,fill="#0c4a40")+
    geom_point(data=aggregate(mood_dmean~nattempt+uq_index+stage_fa,data = bdf,FUN = mean),alpha=0.1,position = position_dodge2(width = 0.2))+
    geom_point(data=aggregate(mood_dmean~nattempt+stage_fa,data = bdf,FUN = mean),size=5)+
    geom_line(data=aggregate(mood_dmean~nattempt+stage_fa,data = bdf,FUN = mean),size=2)+
    stat_summary(fun.data=mean_se, fun.args = list(mult=10), geom="errorbar", width=0.3, size =1) + 
    #scale_x_continuous(breaks = 3:9,labels=c("3","4","5","6","7","8","9"))+
    xlab("Number of Letters") + ylab("Happiness Rating (Z-score)") + 
    scale_color_manual(name = "Stages", labels = c("Early", "Mid","Late"), values=c("#81cbde","#39a2bd","#075163")) +  
    theme(text  = element_text(size = 20),axis.text = axis_style) 
  ggsave(filename = "S01_stageError.png",scale = 1.3,width=5,height = 3,units = "in")
  
  
  mood_M2R_ef<-lmerTest::lmer(slider.response~nattempt_s+eff_exp_s+failed+cu_natt_s+
                                (nattempt_s+eff_exp_s+failed+cu_natt_s|participant),
                              data = bdf,
                              control = lme4::lmerControl(optimizer = "bobyqa"))
  
  mood_M2R_fa<-lmerTest::lmer(slider.response~nattempt_s+pt_adj_s+eff_pnexp+failed+trial_s+
                                (nattempt_s+pt_adj_s+eff_pnexp++failed+trial_s|participant),
                              data = bdf,
                              control = lme4::lmerControl(optimizer = "bobyqa"))
  
  mood_M2R_avgfa<-lmerTest::lmer(slider.response~nattempt_s+pt_adj_s+eff_avgexpfa+failed+trial_s+
                                   (nattempt_s+pt_adj_s+eff_avgexpfa+failed+trial_s|participant),
                                 data = bdf,
                                 control = lme4::lmerControl(optimizer = "bobyqa"))
  
  mood_M2R_v<-lmerTest::lmer(slider.response~nattempt_s*mood_var+pt_adj_s*mood_var+eff_exp_s*mood_var+failed*mood_var+
                               trial_s*mood_var+(nattempt_s+pt_adj_s+eff_exp_s+failed|participant),
                             data = bdf[!is.na(bdf$failed),],
                             control = lme4::lmerControl(optimizer = "bobyqa"))
  
  
  mood_M2R_a<-lmerTest::lmer(slider.response~nattempt_s+pt_adj_s+eff_exp_s+
                               trial_s+(nattempt_s+pt_adj_s+eff_exp_s|participant),
                             data = bdf[bdf$win,],
                             control = lme4::lmerControl(optimizer = "bobyqa"))
  bdf$e_diff_s <- scale(bdf$e_diff) 
  bdf$pt_diff_s <-  scale(bdf$pt_diff)
  bdf$ef_diff_s <- scale(bdf$ef_diff)
  
  mood_M4_ts<-lmerTest::lmer(slider.response~nattempt_s+pt_adj_s+abs(e_diff_s)+abs(pt_diff_s)+failed+trial_s+
                               (nattempt_s+pt_adj_s+abs(e_diff_s)+abs(pt_diff_s)+failed+trial_s|participant),
                             data = bdf,
                             control = lme4::lmerControl(optimizer = "bobyqa"))
  
  
  a<-ggplot(bdf,aes(x=trial,y=slider.response)) + 
    geom_rect(aes(xmin=trial-0.4,xmax=trial+0.4,ymin=min(slider.response),ymax=min(slider.response)+1.4*sd(slider.response),fill=nattempt)) + 
    scale_fill_gradient2("nattempt", low = "#1B7837", mid = "white", high = "#762A83") +
    new_scale("fill") +
    geom_rect(aes(xmin=trial-0.4,xmax=trial+0.4,ymin=min(slider.response)+1.5*sd(slider.response),ymax=max(slider.response)-1.5*sd(slider.response),fill=pt_dist)) + 
    scale_fill_gradient2("pt_dist", low = "#762A83", mid = "white", high = "#1B7837") +
    new_scale("fill") +
    geom_rect(aes(xmin=trial-0.4,xmax=trial+0.4,ymin=max(slider.response)-1.4*sd(slider.response),ymax=max(slider.response),fill=eff_exp)) +
    scale_fill_gradient2("eff_exp", low = "#762A83", mid = "white", high = "#918144") +
    geom_line(color="black",size=1.5) + geom_point(aes(color=win),size=0.8) + scale_color_manual(values=c("TRUE"="royalblue","FALSE"="red")) + 
    facet_wrap(~participant,ncol=2) 
  #7 #15 efficacy 
  #8 #12 invariant 
  #9 #21 ???
  a <- a + theme(legend.position="top")
  ggsave(filename = "indi_mood_by_condis.pdf",plot = a,device = "pdf",width = 25,height = 160,limitsize = F)
  
  
  
  b<-ggplot(bdf,aes(y=slider.response,x=as.factor(eff_pnexp),fill=win,color=win))+
    geom_point(position = position_jitterdodge(),alpha=0.7) + 
    geom_boxplot(position = position_dodge(),alpha=0.9) +
    #facet_wrap(~participant,ncol=6) + 
    scale_color_manual(values=c("TRUE"="#8a3299","FALSE"="#b33e73"))+ scale_fill_manual(values=c("TRUE"="#8a3299","FALSE"="#b33e73")) +
    xlab("Efficacy Split") + ylab("Mood Ratings")
  
  
  
  b<-ggplot(bdf,aes(y=slider.response,x=as.factor(eff_exp),fill=win,color=win))+
    geom_violin(position = position_dodge(),alpha=0.7) + geom_point(position = position_jitterdodge()) + 
    #facet_wrap(~participant,ncol=6) + 
    scale_color_manual(values=c("TRUE"="#ab9b26","FALSE"="#e68337"))+ scale_fill_manual(values=c("TRUE"="#ab9b26","FALSE"="#e68337")) +
    xlab("Efficacy | Ratio Term") + ylab("Mood Ratings") 
  b<-b+theme(legend.position="top") 
  ggsave(filename = "indi_mood_by_eff.pdf",plot = b,device = "pdf",width = 25,height = 70,limitsize = F)
  
  ####Graphing
  ggplot(bdf,aes(y=slider.response,x=trial),color="#85d4c7") + 
    geom_point(position = position_dodge2(width = 1),color="#85d4c7",alpha=0.1)+
    geom_line(mapping = aes(fill=participant,color=participant),stat="smooth",method = "lm", size = 1.5,alpha = 0.4, color="#85d4c7")+
    stat_summary(fun.data=mean_cl_boot, fun.args = list(), geom="errorbar", color="#0c4a40", width=0.2, size =0.5) +
    geom_smooth(method="lm",color="#0c453c",fill="#0c4a40") + ylim(c(0,10.5)) +
    xlab("Trial") + ylab("Momentary Happiness Ratings")+ theme(text  = element_text(size = 20)) 
  
  ggplot(bdf,aes(y=slider.response,x=trial),color="#85d4c7") + 
    geom_point(position = position_dodge2(width = 1),color="#85d4c7",alpha=0.1)+
    geom_line(mapping = aes(fill=participant,color=participant),stat="smooth",method = "lm", size = 1.5,alpha = 0.4, color="#85d4c7")+
    stat_summary(fun.data=mean_se, fun.args = list(), geom="errorbar", color="#0c4a40", width=0.2, size =0.5) +
    geom_smooth(method="lm",color="#0c453c",fill="#0c4a40") + ylim(c(0,10.5)) +
    xlab("Trial") + ylab("Momentary Happiness Ratings")+ theme(text  = element_text(size = 20)) 
  
  ggplot(bdf,aes(y=slider.response,x=N),color="#a493b5") + 
    geom_point(position = position_dodge2(width = 1),color="#a493b5",alpha=0.1)+
    geom_line(mapping = aes(fill=participant,color=participant),stat="smooth",method = "lm", size = 1.5,alpha = 0.4, color="#a493b5")+
    stat_summary(fun.data=mean_cl_boot, fun.args = list(), geom="errorbar", color="#231c2b", width=0.2, size =1) +
    geom_smooth(method="lm",color="#231c2b",fill="#231c2b") +
    xlab("Number of Letters") + ylab("Momentary Happiness Ratings") + theme(text  = element_text(size = 20)) 
  
  ggplot(bdf,aes(y=slider.response,x=nattempt),color="#b33e73") + 
    geom_point(position = position_dodge2(width = 1),color="#ceadf0",alpha=0.1)+
    geom_line(mapping = aes(fill=participant,color=participant),stat="smooth",method = "lm", size = 1.5,alpha = 0.4, color="#ceadf0")+
    stat_summary(fun.data=mean_cl_boot, fun.args = list(), geom="errorbar", color="#8a3299", width=0.2, size =1) +
    geom_smooth(method="lm",color="#8a3299",fill="#8a3299") + ylim(c(0,10.5)) +
    xlab("Number of Errors") + ylab("Momentary Happiness Ratings") + theme(text  = element_text(size = 20)) 
  
  ggplot(bdf,aes(y=slider.response,x=pt_dist),color="#25424f") + 
    geom_point(position = position_dodge2(width = 1),color="#c98276",alpha=0.1)+
    geom_line(mapping = aes(fill=participant,color=participant),stat="smooth",method = "lm", size = 1.5,alpha = 0.4, color="#c98276")+
    stat_summary(fun.data=mean_cl_boot, fun.args = list(), geom="errorbar", color="#e35d6a", width=0.2, size =1) +
    geom_smooth(method="lm",color="#e35d6a",fill="#d29985") +
    xlab("Reward (10 pts)") + ylab("Momentary Happiness Ratings")+ theme(text  = element_text(size = 20)) 
  
  ######
  ggplot(bdf,aes(y=slider.response,x=eff_exp),color="#e68337") + 
    geom_point(position = position_dodge2(width = 1),color="#ab9b26",alpha=0.1)+
    geom_smooth(method="lm",color="#e68337",fill="#e68337") +
    xlab("Efficacy | (RM / NE)") + ylab("Mood Ratings")+ theme(text  = element_text(size = 20)) 
  
  ggplot(bdf,aes(y=slider.response,x=eff),color="#d6b37a") + 
    geom_point(position = position_dodge2(width = 1),color="#d6b37a",alpha=0.1)+
    geom_smooth(method="lm",color="#544223",fill="#704e16") +
    xlab("Efficacy | (RM / N)") + ylab("Mood Ratings") + theme(text  = element_text(size = 20)) 
  
  ggplot(bdf[!is.na(bdf$win),],aes(y=slider.response,x=win)) + geom_boxplot() +
    xlab("Win Trial?") + ylab("Mood Ratings") + theme(text  = element_text(size = 20)) 
  
  b<-ggplot(bdf,aes(y=slider.response,x=as.factor(nattempt)),color="#8a3299")+
    geom_violin(position = position_dodge(),alpha=0.7) + geom_point(position = position_jitter()) + 
    #facet_wrap(~participant,ncol=6) +  
    #scale_color_manual(values=c("TRUE"=,"FALSE"="#b33e73"))+ scale_fill_manual(values=c("TRUE"="#8a3299","FALSE"="#b33e73")) +
    xlab("Number of Attempts") + ylab("Mood Ratings")
  b<-b+theme(legend.position="top") 
  ggsave(filename = "indi_mood_by_nattempt.pdf",plot = b,device = "pdf",width = 25,height = 70,limitsize = F)
  
  
  b<-ggplot(bdf,aes(y=slider.response,x=as.factor(pt_dist),fill=win,color=win))+
    geom_violin(position = position_dodge(),alpha=0.7) + geom_point(position = position_jitterdodge()) + 
    facet_wrap(~participant,ncol=6) + 
    scale_color_manual(values=c("TRUE"="#1f8267","FALSE"="#20a89f"))+ scale_fill_manual(values=c("TRUE"="#1f8267","FALSE"="#20a89f")) +
    xlab("Reward (pts)") + ylab("Mood Ratings")
  b<-b+theme(legend.position="top") 
  ggsave(filename = "indi_mood_by_reward.pdf",plot = b,device = "pdf",width = 25,height = 70,limitsize = F)
  
  
  
  ggplot(aggregate(slider.response~pt_dist+nattempt,data=bdf[bdf$pt_dist!=0,],FUN = mean),aes(y=as.factor(pt_dist),x=as.factor(nattempt),fill=slider.response)) + geom_tile(stat="identity") +scale_fill_gradient(low="white", high="blue") 
  
  ggplot(aggregate(slider.response~pt_diff+e_diff,data=bdf,FUN = mean),aes(y=as.factor(pt_diff),x=as.factor(e_diff),fill=slider.response)) + geom_tile(stat="identity") +scale_fill_gradient(low="white", high="blue") 
  
  
  bdf_fdf<-reshape2::melt(bdf[c("participant","trial","mood_dmean",names(bdf)[grep("failed",names(bdf))])],id.vars=c("participant","trial","mood_dmean"))
  bdf_fdf$variable<-gsub("failed",0,bdf_fdf$variable)
  bdf_fdf$variable<-gsub("0_lead1",-1,bdf_fdf$variable)
  bdf_fdf$variable<-gsub("0_lag","",bdf_fdf$variable)
  bdf_fdf<-bdf_fdf[which(bdf_fdf$value),]
  
  ggplot(bdf_fdf,aes(y=mood_dmean,x=as.factor(variable)))+
    geom_violin(alpha=0.7,color="#65979e",fill="#65979e") + geom_point(color="#4a5e61") + 
    #facet_wrap(~participant,ncol=6) + 
    #scale_color_manual(values=c("TRUE"="#1f8267","FALSE"="#20a89f"))+ scale_fill_manual(values=c("TRUE"="#1f8267","FALSE"="#20a89f")) +
    xlab("Failed Trial Time Lag (negative indicate lead, positive for lag, i.e. 2 is 2 trials after the Failed trial)") + ylab("Mood Ratings")
  
  sjPlot::plot_model(mood_M2R,type = "slope",terms = c("nattempt","eff_exp","pt_adj"))
  
  mood_M2W<-lmerTest::lmer(slider.response~nattempt_s*win+rewMag_s*win+eff_exp_adj_s*win+
                             trial_s+(nattempt_s*win+rewMag_s*win+eff_exp_adj_s*win|participant),
                           data = bdf)
  mood_M2W_simp<-lmerTest::lmer(slider.response~nattempt_s*win+rewMag_s*win+eff_exp_adj*win+
                                  trial_s+(nattempt_s+rewMag_s+eff_exp_adj|participant),
                                data = bdf)
  mood_M2W_persub <- glm_bysubj(data = bdf,split_by = "participant", 
                                formula = slider.response~nattempt_s*win+rewMag_s*win+eff_exp_adj*win+trial_s)
  #########
  mood_M3S<-lmerTest::lmer(slider.response~nattempt_s+rewMag_s + 
                             nattempt_lag_s + rewMag_lag_s + 
                             trial_s+(nattempt_s+rewMag_s +nattempt_lag_s + rewMag_lag_s |participant),
                           data = bdf[!is.na(bdf$nattempt_lag) & !is.na(bdf$rewMag_lag),],
                           control = lme4::lmerControl(optimizer = "bobyqa"))
  
  mood_M3I<-lmerTest::lmer(slider.response~nattempt_s*rewMag_s + 
                             nattempt_lag_s * rewMag_lag_s + 
                             trial_s+(nattempt_s*rewMag_s+nattempt_lag_s*rewMag_lag_s|participant),
                           data = bdf[!is.na(bdf$nattempt_lag) & !is.na(bdf$rewMag_lag),],
                           control = lme4::lmerControl(optimizer = "bobyqa"))
  
  
  mood_M3R<-lmerTest::lmer(slider.response~nattempt_s+rewMag_s+e_eff_s + 
                             nattempt_lag_s + rewMag_lag_s + e_eff_lag_s + 
                             trial_s+(nattempt_s+rewMag_s+e_eff_s+nattempt_lag_s+rewMag_lag_s+e_eff_lag_s|participant),
                           data = bdf[!is.na(bdf$nattempt_lag) & !is.na(bdf$rewMag_lag),],
                           control = lme4::lmerControl(optimizer = "bobyqa"))
  
  
  #### Correlation Matrix ######
  library(reshape2)
  sub_bdf <- bdf[c("nattempt_s","pt_adj_s","eff_exp_s","trial_s")]
  names(sub_bdf) <- c("NE","RM","Efficacy","Trial")
  
  # creating correlation matrix
  corr_mat <- round( cor(sub_bdf,use = "complete")  ,2)
  
  melted_corr_mat <- melt(corr_mat)
  names(melted_corr_mat)[3] <- "Cor"
  ggplot(data = melted_corr_mat, aes(x=Var1, y=Var2,fill=Cor)) + scale_fill_viridis_c(option = "D") +
    geom_tile() + geom_text(aes(Var2, Var1, label = Cor),color = "white", size = 6) +  theme(axis.title=element_blank(),text  = element_text(size = 20))
  ##############Auto-lag############
  
  
  split(bdf,bdf$participant)[[2]] -> sdf
  #generate single subject metrics:L
  side_bias<-1-sapply(split(bdf,bdf$participant),function(sdf){mean(sdf$choice_key.corr[sdf$e_diff!=0])})
  remove <- side_bias > 0.95 | side_bias < 0.05
  bdf$side_bias <- side_bias[match(bdf$participant,names(side_bias))]
  if(any(remove)){
    message(paste(remove,collapse = ", "),"; are being removed")
    bdf$remove <- remove[match(bdf$participant,names(remove))]
  }
  
  ##Choice analysis:
  
  
  choice_M1<-lme4::glmer(choice ~ e_diff+pt_diff+trial_s+(e_diff+pt_diff+trial_s|participant),data = bdf,
                         family = binomial(),lme4::glmerControl(optimizer = "bobyqa", optCtrl = list(maxfun = 100000)))
  choice_M2<-lme4::glmer(choice ~ e_diff+pt_diff+ef_diff+trial_s+(e_diff+pt_diff+ef_diff+trial_s|participant),data = bdf,
                         family = binomial(),lme4::glmerControl(optimizer = "bobyqa", optCtrl = list(maxfun = 100000)))
  choice_M3<-lme4::glmer(choice ~ e_diff*pt_diff+trial_s+(e_diff*pt_diff+ef_diff+trial_s|participant),data = bdf,
                         family = binomial(),lme4::glmerControl(optimizer = "bobyqa", optCtrl = list(maxfun = 100000)))
  
  
  choice_M1<-lme4::glmer(choice ~ e_diff+pt_diff+ef_diff+(e_diff+pt_diff+ef_diff|participant),data = bdf,
                         family = binomial(),lme4::glmerControl(optimizer = "bobyqa", optCtrl = list(maxfun = 100000)))
  choice_M1a<-lme4::glmer(choice ~ e_diff*pt_diff+ef_diff+(e_diff*pt_diff+ef_diff|participant),data = bdf,
                          family = binomial(),lme4::glmerControl(optimizer = "bobyqa", optCtrl = list(maxfun = 100000)))
  
  choice_M2<-lme4::glmer(choice ~ pt_diff+e_diff+ef_diff+trial_s+(pt_diff+ef_diff+e_diff+trial_s|participant),data = bdf,
                         family = binomial(),lme4::glmerControl(optimizer = "bobyqa", optCtrl = list(maxfun = 100000)))
  
  choice_M2a<-lme4::glmer(choice ~ pt_diff+ef_diff+e_diff*cu_natt_s_lag+pt_diff*cu_natt_s_lag+ef_diff*cu_natt_s_lag+(pt_diff+ef_diff+e_diff+cu_natt_s_lag|participant),data = bdf,
                          family = binomial(),lme4::glmerControl(optimizer = "bobyqa", optCtrl = list(maxfun = 100000)))
  choice_M2b<-lme4::glmer(choice ~ pt_diff+ef_diff+e_diff*trial_s+pt_diff*trial_s+ef_diff*trial_s+(pt_diff+ef_diff+e_diff+trial_s|participant),data = bdf,
                          family = binomial(),lme4::glmerControl(optimizer = "bobyqa", optCtrl = list(maxfun = 100000)))
  choice_M2c<-lme4::glmer(choice ~ pt_diff+ef_diff+e_diff+e_diff*trial_s+(pt_diff+ef_diff+e_diff+e_diff*trial_s|participant),data = bdf,
                          family = binomial(),lme4::glmerControl(optimizer = "bobyqa", optCtrl = list(maxfun = 100000)))
  
  ############################
  choice_M3<-lme4::glmer(factor(choice) ~ pt_diff*e_diff+(pt_diff*e_diff|participant),data = bdf,
                         family = binomial(),lme4::glmerControl(optimizer = "bobyqa", optCtrl = list(maxfun = 100000)))
  
  choice_M4<-lme4::glmer(choice ~ pt_diff*e_diff+ef_diff+(pt_diff*ef_diff+e_diff|participant),data = bdf,
                         family = binomial(),lme4::glmerControl(optimizer = "bobyqa", optCtrl = list(maxfun = 100000)))
  
  
  ggplot(data=bdf[bdf$e_diff!=0,],aes(x=as.factor(choice),fill=as.factor(pt_diff)))+geom_histogram(stat="count",position = position_dodge2(),binwidth = 0.5) + facet_wrap(~participant)
  ggplot(data=bdf[bdf$e_diff!=0,],aes(x=as.factor(choice),fill=as.factor(e_diff)))+geom_histogram(stat="count",position = position_dodge2(),binwidth = 0.5) + facet_wrap(~(participant))
  
  
  ggplot(data=bdf[bdf$e_diff!=0,],aes(y=as.factor(choice)),x=e_diff)+geom_histogram(stat = "summarize")
  
  
  aggregate(nattempt ~ N, data = bdf[bdf$e_diff!=0 & !bdf$remove,],FUN = mean)
  
  ggplot(data = aggregate(choice ~ pt_diff + e_diff ,data = bdf[bdf$e_diff!=0,],FUN = mean), 
         aes(y=choice,x=as.factor(pt_diff),fill=as.factor(e_diff))) + 
    geom_histogram(position = position_dodge2(),binwidth = 0.5,stat = "identity") + 
    xlab("Difference in Reward Magnitude (in 10 points)") + ylab("Choice Percentage")  + ggtitle("Choice preference by\ndifference in reward magnitude and number of letters") + 
    labs(fill='Difference\nin\nnumber of letters\n(N)\n') +theme(text  = element_text(size = 20))
  
  ggplot(data = aggregate(choice ~ ef_diff ,data = bdf[bdf$e_diff!=0,],FUN = mean), 
         aes(y=choice,x=as.factor(ef_diff))) + 
    geom_histogram(position = position_dodge2(),binwidth = 0.5,stat = "identity") + ggtitle("Choice preference by efficacy") +
    xlab("low <- Difference in efficacy -> high") + ylab("Choice Percentage")  +theme(text  = element_text(size = 20),axis.text.x=element_blank())
  
  
  ggplot(data = aggregate(choice ~ pt_diff + e_diff ,data = bdf[bdf$e_diff!=0,],FUN = mean,na.action = na.omit), aes(y=choice,x=as.factor(pt_diff),fill=as.factor(e_diff))) + 
    geom_histogram(position = position_dodge2(),binwidth = 0.5,stat = "identity") 
  
  
  sum_df <- aggregate(choice ~ pt_diff + e_diff + participant,data = bdf[bdf$e_diff!=0,],FUN = mean)
  
  ggplot(data = sum_df,aes(x=(pt_diff),y=choice,color=as.factor(e_diff))) + geom_smooth()
  
  ggplot(data=bdf[bdf$e_diff!=0,],aes(x=ef_diff,y=choice))+geom_smooth()
  
  
  summary(lmerTest::lmer(nattempt ~ N*remove+(1|participant),data=bdf[bdf$e_diff!=0,]))
  
  #----------Baseline mood -----------#
  dfk <- con_sum[c("baseline_mood","endofstudy_mood","dataset_name","prolific_pid")]
  dfk_s <- reshape2::melt(dfk,id.var=c("prolific_pid","dataset_name"))
  dfk_s$dataset_name <- gsub("LT_choice","Study 2", gsub("LT_extend","Study 1",dfk_s$dataset_name))
  dfk_s$variable <- gsub("baseline_mood","Beginning of Study", gsub("endofstudy_mood","End of Study",dfk_s$variable))
  dfk_s$`Dataset Type` <- dfk_s$dataset_name
  
  ggplot(dfk_s,aes(x=variable,y=value,color=`Dataset Type`))+geom_boxplot()+geom_point(position = position_jitterdodge()) +
    theme(text  = element_text(size = 20))  + xlab("") + ylab("Mood Rating")
  summary(lmerTest::lmer(value ~ variable * dataset_name + (1|prolific_pid),data = dfk_s))
  
  
  
  
  
  bdf$failed <- as.factor(bdf$failed)
  mood_M2R_bl<-lmerTest::lmer(slider.response~nattempt_s+pt_adj_s+eff_exp_s+failed*baseline_mood_s+trial_s+
                                (nattempt_s+pt_adj_s+eff_exp_s+failed+trial_s|participant),
                              data = bdf,
                              control = lme4::lmerControl(optimizer = "bobyqa"))
  
  lt_vars <- c("slider.response","dataset","nattempt_s","pt_adj_s","trial_s","trial",
               "eff_exp_s","failed","baseline_mood_s","cu_natt_s","participant")
  bdf_joint <- rbind(LT_choice[lt_vars],LT_extend[LT_extend$trial %in% 1:150,lt_vars])
  bdf_joint$trial_s <- scale(bdf_joint$trial,center = F)
  moodjoint_M2R_bl<-lmerTest::lmer(slider.response~nattempt_s+pt_adj_s+failed*baseline_mood_s+cu_natt_s+trial_s+
                                     (nattempt_s+pt_adj_s+failed+cu_natt_s|participant),
                                   data = bdf_joint,
                                   control = lme4::lmerControl(optimizer = "bobyqa"))
  moodjoint_M2R_ds<-lmerTest::lmer(slider.response~nattempt_s*dataset+pt_adj_s*dataset+failed*baseline_mood_s+cu_natt_s*dataset+trial_s+
                                     (nattempt_s+pt_adj_s+failed+cu_natt_s+trial_s|participant),
                                   data = bdf_joint,
                                   control = lme4::lmerControl(optimizer = "bobyqa", optCtrl = list(maxfun = 100000)))
  
  
  #----------SV mood -----------------#
  #rationale mode 
  # utility = reward - effort | high utility preferred  
  # ratio | efficacy preferred
  
  
  dfk$mood_change <- dfk$endofstudy_mood - dfk$baseline_mood
  
  #--------test of linearity----------#
  
  
  #--------test of Reaction Time------#
  
  #Initial reaction time
  hist(bdf$init_rt)
  plot(bdf$init_rt,bdf$N)
  ggplot(bdf,aes(y=(init_rt),x=as.factor(N))) + geom_boxplot()
  
  ggplot(bdf,aes(color=is.na(init_rt),x=as.factor(N))) + geom_histogram(stat = "count")
  plot(bdf$slider.response,bdf$init_rt)
  
  bdf$init_rt_fx <- bdf$init_rt
  bdf$init_rt_fx[is.na(bdf$init_rt_fx)] <- sqrt(bdf$N[is.na(bdf$init_rt)])
  ggplot(bdf,aes(y=(init_rt_fx),x=as.factor(N))) + geom_boxplot()
  plot(bdf$slider.response,bdf$init_rt_fx)
  
  #total reaction time:
  bdf$sum_rt <- sapply(1:nrow(bdf),function(x){
    lsrt <- bdf$TargetResp_lsrt[[x]]
    n <- bdf$N[x]
    lsrt[is.na(lsrt)] <- sqrt(n)
    return(sum(lsrt))
  })
  ggplot(bdf[bdf$sum_rt<9,],aes(y=(sum_rt),x=as.factor(N))) + geom_boxplot()
  ggplot(bdf,aes(y=(sum_rt),x=as.factor(slider.response))) + geom_point()
  plot(bdf$slider.response[bdf$sum_rt<9],bdf$sum_rt[bdf$sum_rt<9])
  
  ##key press avg is 0.273
  
  bdf$nx_att <- sapply(bdf$TargetResp_lsrt,function(x){
    length(which(x<0.3))
  })
  
  
  a
  
  
  
  
}