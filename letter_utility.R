###utility 
# bdf[c("list_og","list_sort","rewMag","ViewDura","cor_pos","target_letter","N","trial")]
# lapply(1:length(condidf), function(x){
#   xy <- condi_sp[[1]]
#   xy$rewMag <- paste(xy$rewMag," pts")
#   write.csv(xy,file = paste0("contingency_",x,".csv"),row.names = F)
# })


letter_proc <- function(dfx){
  #remove instructions & related variables
  dfx<-dfx[is.na(dfx$rep_inst.ran),]
  dfx[dfx==""]<-NA
  dfx<-dfx[which(apply(dfx,2,function(x){any(!is.na(x))}))]
  dfx<-dfx[which(!names(dfx) %in% c("skip","expName","psychopyVersion","OS","frameRate","fbclid"))]
  
  #Add some new variables
  dfx$mood_swings<-dfx$slider.response - c(dfx$slider.response[2:nrow(dfx)],NA)
  
  #Fix the C & 1s:
  dfx$Ndist[dfx$target_letter=="C" & dfx$cor_pos=="1"] <- 0
  dfx$editDistance[dfx$target_letter=="C" & dfx$cor_pos=="1"] <- 0
  dfx$too_easy <- dfx$target_letter=="C" & dfx$cor_pos=="1"
  #Categorize the 3 dimensions:
  dfx$N_cat <-factor(c("low","mid","high")[dfx$N-3],levels = c("high","mid","low"))
  dfx$editDis_cat <-factor(c("low","low","mid","mid","high")[dfx$editDistance+1],levels = c("high","mid","low"))
  dfx$Ndist_cat<-factor(c("low","low","mid","high")[dfx$Ndist+1],levels = c("high","mid","low"))
  
  dfx$rewMag_num <- as.numeric(gsub(" pts","",dfx$rewMag))
  
  dfx$trial_num <- dfx$trials.thisIndex+1
  dfx$correct <- as.logical(dfx$TargetResp.corr)
  return(dfx)
}

subj_summary <- function(dfx){
  data.frame(
    participant = unique(dfx$participant),
    session = unique(dfx$session),
    accuracy_rate=round(mean(dfx$TargetResp.corr),4),
    mean_rt = mean(dfx$TargetResp.rt,na.rm = T),
    stringsAsFactors = F)
}

get_effectsize <- function(model = NULL) {
  fixed_ef <- summary(model)$coefficients[,1]
  x<-lme4::VarCorr(model)
  efsize<- abs(fixed_ef) / sqrt(sum(c(attr(x$participant,"stddev"),attr(x,"sc"))^2))
  return(efsize)
}

proc_func <- function(xd){
  #print(unique(xd$participant))
  if(is.null(xd$ViewDura)){
    xd$ViewDura <- 5
  }
  if (is.na(unique(xd$participant))) {
    xd$participant <- paste(sample(0:9,7,replace = T),collapse = "")
  }
  message("processing ",unique(xd$participant))
  #clean up 
  if (length(which(xd$trials_2.ran==1 | xd$trials_3.ran==1))>0){
    xd <- xd[-which(xd$trials_2.ran==1 | xd$trials_3.ran==1),]
  }
  IsChoice <- any(grepl("c1_n",names(xd)))
  if(IsChoice) {
    xd$Ndist_scale <- 0
  }
  xd <- xd[which(apply(xd,2,function(x){any(!is.na(x))}))]
  xd <- xd[which(!grepl("Inst|inst",names(xd)))]
  
  xd <- rbind(xd[which(!1:nrow(xd) %in% c(which(xd$effort.ran==1),which(xd$effort.ran==1)+1)),],
              do.call(rbind,lapply(which(xd$effort.ran==1),function(x){
                xe<-xd[c(x,x+1),]
                as.data.frame(lapply(xe,function(y){
                  if(any(!is.na(y))){
                    if(any(is.na(y))){
                      y[!is.na(y)]
                    } else if (any(duplicated(y))) {
                      y[!duplicated(y)]
                    } else if ("" %in% y) {
                      y[y!=""]
                    } else {
                      stop(y)
                    }
                  } else {return(NA)}
                }))
              })))
  
  if(nrow(xd)<30){return(NULL)}
  if(!is.null(xd$pre_trial_mood.ran)){
    xd$blmood_response <- xd$slider.response[which(xd$pre_trial_mood.ran==1)]
    xd$blmood_rt <- xd$slider.rt[which(xd$pre_trial_mood.ran==1)]
    xd <- xd[-which(xd$pre_trial_mood.ran==1),]
  } else {
    xd$blmood_response <- NA
    xd$blmood_rt <- NA
  }
  xd <- xd[which(!grepl("pre_trial_mood",names(xd)))]
  
  if(!is.null(xd$effort_rate.response) && any(!is.na(xd$effort_rate.response))){
    xd$effort_rate_scale<-as.numeric(scale(xd$effort_rate.response,center = T,scale = T))
    xd$effort_medsplit <- ifelse(xd$effort_rate_scale > median(xd$effort_rate_scale,na.rm = T),"High","Low")
  } else {
    xd$effort_rate.response <- NA
    xd$effort.ran <- NA
  }
  
  
  if(any(grepl("rep_trial",names(xd)))) {
    t_num<-which(!is.na(xd$trials.ran))
    if(is.null(xd$trials.thisIndex)){
      return(NULL)
    } 
    xd$trial_index <- xd$trials.thisIndex+1
    xd$trial_index[is.na(xd$trial_index)]<-xd$trial_index[sapply(which(is.na(xd$trials.ran)),function(x){
      xa<-which(!is.na(xd$ trials.ran)) - x
      return(t_num[xa>0][1])
    })]
    xd_sp <- split(xd,xd$trial_index)
    #count<-0
    xd<-do.call(rbind,lapply(xd_sp,function(xdk){
      #count <<- count+1
      #print(count)
      single_row_x <- xdk[1,which(!apply(xdk,2,function(x){length(unique(x))>1}))]
      muiltiple_x <- xdk[,which(apply(xdk,2,function(x){length(unique(x))>1}))]
      s_mrate <- muiltiple_x[which(!is.na(muiltiple_x$trials.ran)),]
      muiltiple_x <- muiltiple_x[which(is.na(muiltiple_x$trials.ran)),]
      single_row_y <- cbind(single_row_x,s_mrate[which(!apply(s_mrate,2,is.na))])
      muiltiple_x <- muiltiple_x[which(apply(muiltiple_x,2,function(x){any(!is.na(x))}))]
      single_row_y$nattempt <- as.numeric(nrow(muiltiple_x))
      single_row_y$contingency <- unique(muiltiple_x$contingency[muiltiple_x$contingency!=""])
      single_row_y$ViewDura <-  5
      if(is.null(muiltiple_x$TargetResp.keys)) {
        return(NULL)
      }
      if(!is.null(muiltiple_x$reward_points)) {
        single_row_y$reward_points <-  as.numeric(na.omit(muiltiple_x$reward_points))
      }
      single_row_y$TargetResp_lskeys <- list(muiltiple_x$TargetResp.keys)
      single_row_y$TargetResp_lsrt <- list(muiltiple_x$TargetResp.rt)
      single_row_y$TargetResp.cor <- list(muiltiple_x$TargetResp.corr)
      single_row_y$win <- any(muiltiple_x$TargetResp.corr==1)
      single_row_y$TargetResp_rt_mean <- mean(muiltiple_x$TargetResp.rt,na.rm=T)
      single_row_y$TargetResp_init_rt <- muiltiple_x$TargetResp.rt[1]
      if(IsChoice) {
        single_row_y$choice_key.keys <- muiltiple_x$choice_key.keys[muiltiple_x$choice_key.keys!=""]
        single_row_y$choice_key.corr <- muiltiple_x$choice_key.corr[muiltiple_x$choice_key.keys!=""]
        single_row_y$choice_key.rt  <- muiltiple_x$choice_key.corr[muiltiple_x$choice_key.keys!=""]
        single_row_y$N <- single_row_y[[paste0("c",ifelse(single_row_y$choice_key.corr==1,1,2),"_n")]]
        single_row_y$rewMag <- single_row_y[[paste0("c",ifelse(single_row_y$choice_key.corr==1,1,2),"_pt")]]
      }
      
      return(single_row_y)
    }))
    if(is.null(xd)||nrow(xd) < 2) {
      return(NULL)
    }
    xd$trial_index <- NULL
    xd$TargetResp_rt_mean_lag <- scale(c(NA,xd$TargetResp_rt_mean[1:(nrow(xd)-1)]))
    xd$TargetResp_init_rt_lag <- scale(c(NA,xd$TargetResp_init_rt[1:(nrow(xd)-1)]))
    xd$TargetResp.rt <- NA
    xd$TargetResp.corr <- 1
  } 
  xd$nmissed <- sapply(xd$TargetResp_lskeys,function(x){length(which(is.na(x)))})
  
  xd <- xd[which(!is.na(xd$trials.thisTrialN)),]
  xd$trial <- as.numeric(xd$trials.thisTrialN)+1
  xd$trials.order <- NULL
  
  xd <- xd[order(xd$trial),]
  xd$trial <- 1:nrow(xd)
  xd <- xd[order(names(xd))]
  if(nrow(xd)<30){return(NULL)}
  message(paste("participant: ",xd$participant[1],"has trial N of ",nrow(xd)))
  if(nrow(xd)>1){
    xd$rt_lag <- scale(c(NA,xd$TargetResp.rt[1:(nrow(xd)-1)]))
    xd$mood_lag <- scale(c(NA,xd$slider.response[1:(nrow(xd)-1)]))
    xd$effort_lag <- scale(c(NA,xd$effort_rate.response[1:(nrow(xd)-1)]))
    xd$accurate_lag <- c(NA,xd$TargetResp.cor[1:(nrow(xd)-1)])
  } else {
    xd$rt_lag <- NA
    xd$mood_lag <- NA
    xd$accurate_lag <- NA
    xd$effort_lag <- NA
  }
  if(!is.null(xd$rewMag)) {
    xd$rewMag <- as.numeric(gsub(" pts","",xd$rewMag))
  }
  
  xd$Reward <- factor(ifelse(as.logical(xd$TargetResp.corr),"Reward","Omission"),levels = c("Omission","Reward"))
  ##Scale: 
  lag_vars <- c("N","nattempt","rewMag")
  for (v in lag_vars) {
    xd[[paste(v,"_lag",sep = "")]]<-c(NA,xd[[v]][1:(nrow(xd)-1)])
  }
  xd$mood_rate_lag<-c(NA,xd$slider.response[1:(nrow(xd)-1)])
  xd$mood_change <- xd$slider.response - xd$mood_rate_lag
  
  
  return(xd)
}
glm_bysubj <- function(data=NULL,split_by=NULL,formula=NULL) {
  
  subj_betas<-do.call(rbind,lapply(split(x = data,f = data[[split_by]]),function(db){
    dt<-lm(formula = formula,data = db)
    gxt<-as.data.frame(summary(dt)$coefficient)
    gxt$terms <- as.character(rownames(gxt))
    return(gxt)
  }))
  one_sample_t<-do.call(rbind,lapply(split(subj_betas,subj_betas$terms),function(rx){
    x<-t.test(rx$Estimate)
    data.frame(t=x$statistic,df=x$parameter,p_value = x$p.value,
               estimate = x$estimate,ci_95_min = x$conf.int[1],ci_95_max = x$conf.int[2],
               terms = unique(rx$terms),stringsAsFactors = F)
  }))
}
sum_model <- function(x){
  print(summary(x))
  print(get_effectsize(x))
  print(MuMIn::r.squaredGLMM(x))
}