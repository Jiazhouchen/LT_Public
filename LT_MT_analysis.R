source("letter_utility.R")
library(ggplot2)
library(latex2exp)
reload <- F
expected_trial <- 168
dt_path <- "/Users/jiazhouchen/Documents/Publish/LT_CABN/OSF\ Data\ Sharing/"
dataset_name <- "LT_MT"
rdata_fname <- file.path(dt_path,dataset_name,paste0(dataset_name,".rdata"))
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
####Fixed re-scaling:
bdf$N_scale <- bdf$N-min(bdf$N)+1
###Getting some rt variant:
bdf$init_rt <- sapply(bdf$TargetResp_lsrt,`[[`,1)
bdf$effort.ran[is.na(bdf$effort.ran)] <- 0 

message("Total sample size: ",length(unique(bdf$participant)))


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

stop("Finished Importing")

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



####Graphing
ggplot(bdf,aes(y=slider.response,x=trial),color="#85d4c7") + 
  geom_point(position = position_dodge2(width = 1),color="#85d4c7",alpha=0.1)+
  geom_line(mapping = aes(fill=participant,color=participant),stat="smooth",method = "lm", size = 1.5,alpha = 0.4, color="#85d4c7")+
  stat_summary(fun.data=mean_cl_boot, fun.args = list(), geom="errorbar", color="#0c4a40", width=0.2, size =0.5) +
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


