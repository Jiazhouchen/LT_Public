###simulate some data to show what the graph would look like 

condi <- bdf[c("nattempt_s","pt_adj_s","eff_exp_s","trial_s","participant","pt_dist","nattempt")]
condi <- condi[condi$pt_dist!=0,]
condi$intercept <- rnorm(n = length(unique(condi$participant)),mean = 6,sd = 1)[match(condi$participant,unique(condi$participant))]
condi$mood <- condi$intercept + (-0.6) * as.numeric(condi$nattempt_s) + (0.4) * as.numeric(condi$pt_adj_s) + (0.5) * as.numeric(condi$eff_exp_s) + 
  (-0.9) * as.numeric(condi$trial_s)

condi$mood[condi$mood > 10] <- 10
condi$mood[condi$mood < 0] <- 0

dt <- aggregate(mood~pt_dist+nattempt,data=condi,FUN = mean)

ggplot(dt,aes(x=as.factor(pt_dist),y=(nattempt),fill=mood)) + geom_tile(stat="identity") + scale_fill_gradient(low="white", high="blue") + 
  scale_y_continuous(trans = "reverse", breaks = unique(dt$nattempt))

bt <- aggregate(slider.response~pt_dist+nattempt,data=bdf[bdf$pt_dist!=0,],FUN = mean)
ggplot(bt,aes(x=as.factor(pt_dist),y=(nattempt),fill=slider.response)) + geom_tile(stat="identity") +scale_fill_gradient(low="white", high="blue") +
  scale_y_continuous(trans = "reverse", breaks = unique(bt$nattempt))


Xmood_M2R_f<-lmerTest::lmer(mood~N_s+pt_adj_s+eff_s+trial_s+(1|participant),data = condi)



#Should we build up a case for first attempt only?
bdf$pt_discount <- ((4-(bdf$nattempt))/4)


###Total trial number:
cal_sprase_fb_trial_n<-function(n_total=200,eff_per=0.2,eff_dur=5,tr_dis=1) {
 
  #Set criteria
  #n_total = 200: Total trial number (ballpark)
  #eff_per = 0.2 #20% trial being under the influence of feedback
  #eff_dur = 5 #LME showed that effect is significant for 5 trials back
  #tr_dis = 8 #distance for the different number of trials 
  ###calculate maximum number of trial with feedback
  n_fb = ceiling(200 * 0.2 / (1+eff_dur))
  n_fb_mean = ceiling(n_total / n_fb)
  
  if(n_fb %% 2 == 0) {
    #even number
    n_fb_list =   unlist(lapply((1:(n_fb/2))*tr_dis,function(x) {
      c(n_fb_mean+x,n_fb_mean-x)
    }))
  } else {
    #odd number 
    #include mean at the center:
    n_fb_list = c(n_fb_mean,unlist(lapply((1:((n_fb-1)/2))*tr_dis,function(x) {
      c(n_fb_mean+x,n_fb_mean-x)
    })))
  }
  if(any(n_fb_list<=0)){stop("tr distance too high, now with negative number, reduce please")}
  #recalculate total trial number and effect percentage:
  n_total_f = sum(n_fb_list) 
  n_effect = sum(n_fb_list-eff_dur-1)
  eff_per_f=(n_total_f-n_effect)/n_total_f
  message("Final total number of trials: ",n_total_f)
  message("Total feedback trials: ",length(n_fb_list))
  message("Total effective trials: ", n_effect, ", and effective percentage: ",round(eff_per_f*100,digits = 2),"%")
  message("Trials #: ",paste(sort(n_fb_list), collapse = ", "))
  return(sort(n_fb_list))
}

cal_sprase_fb_trial_n(n_total = 210,eff_per = 0.2,eff_dur = 5,tr_dis = 8)

###The simulation study for regular LT:
N <- 3:9
ntrial <- 168
ns <- 10000



output<-sapply(1:ns,function(i){
  gt<-unlist(lapply(N,function(nx) {sapply(1:(ntrial/length(N)), function(i) {
    test <- F
    tn <- 0
    while(!test && tn < 10) {
      test <- sample(nx,size=1,replace = T) == 1
      tn <- tn + 1
    }
    return(tn)
  })
  }))
  return(sum(gt) / ntrial)
})
print(quantile(output,.95))



###The simulation study for sparse feedback:
#####Couple of assumptions: They choose keys randomly, they don't learn, they only press 1:N keys and not the full range 
N <- 3:9 
ntrial <- 210
ns <- 100000
output<-sapply(1:ns,function(i) {do.call(sum,lapply(N,function(nx) {sum(sample(x=nx,size = 210/length(N),replace = T) ==1)}))})
print(quantile(output,.95))







