# ####Generate conditions
# 
# #Select Letters: 
# trimN = 3
# sel_letters<-LETTERS[(1+trimN):(length(LETTERS)-trimN)]
# n_letters<-2:6
# ###
# if(F){
# cl = parallel::makeForkCluster(n=6)
# all_comboX<-parallel::parLapply(cl,n_letters,function(selectN){
#   comboX<-data.frame(gtools::permutations(n=length(sel_letters),r = selectN,v=sel_letters,set = TRUE),stringsAsFactors = F)
#   comboX$list_og <- apply(comboX,1,paste,collapse="")
#   comboX$list_sort <- apply(comboX[1:selectN],1,function(x){paste(sort(x),collapse = "")})
#   comboX$N <- selectN
#   return(comboX)
# })
# parallel::stopCluster(cl)
# save(all_comboX,file = "prefix.rdata")
# } else {
#   load("prefix.rdata")
# }
# 
# ###diff gen:
# trialN = 90
# eachN = 15
# rewMag = 10:90
# n_contingency=100
# comboZ<-do.call(rbind,lapply(all_comboX,function(comboY){
#   comboY$distance<-stringdist::stringdist(comboY$list_og,comboY$list_sort,method = "dl")
#   comboY<-comboY[comboY$distance!=0,]
#   comboY<-comboY[c("list_og","list_sort","N","distance")]
#   return(comboY)
# }))
# 
# tb1<-table(paste(comboZ$N,"letters"),paste(comboZ$distance,"operations"))
# 
# comboZ_sp <- split(comboZ,comboZ$distance)
# comboZ_xp <- lapply(comboZ_sp,function(x){split(x,x$N)})
# 
# for (nx in 1:n_contingency) {
#   test_df<-do.call(rbind,lapply(1:max(comboZ$distance),function(distance){
#     minRX<-min(sapply(comboZ_xp[[distance]],nrow))
#     N_weight <- (rev(sapply(comboZ_xp[[distance]],nrow) / apply(tb1,2,sum)[distance]))/max(sapply(comboZ_xp[[distance]],nrow) / apply(tb1,2,sum)[distance])
#     rxd<-do.call(rbind,lapply(comboZ_xp[[distance]],function(dx){
#       dx<-dx[sample.int(n = nrow(dx),size = minRX*N_weight[match(unique(dx$N),names(comboZ_xp[[distance]]))],replace = F),]
#     }))
#     dfa<-rxd[sample.int(n = nrow(rxd),size = eachN,replace = F),]
#     dfa$cor_pos <- sapply(dfa$N,function(x){sample.int(x,1,replace = F)})
#     dfa$target_letter <- substr(dfa$list_sort,start = dfa$cor_pos,stop = dfa$cor_pos)
#     
#     ##Assign reward: 
#     #####Using uniform distribution:
#     dfa$rewMag<-paste(sample(rewMag,nrow(dfa),replace = F),"pts")
#     
#     #Fix the letters so it's better for presentation:
#     dfa$list_og <- sapply(dfa$list_og,function(x){paste(strsplit(x,"")[[1]],collapse = " ")})
#     
#     return(dfa)
#   }))
#   test_df<-test_df[sample.int(nrow(test_df),nrow(test_df),replace = F),]
#   row.names(test_df)<-NULL 
#   write.csv(test_df,file = file.path("./conditionsheets",paste0("contingency_",nx,".csv")),row.names = F)
#   test_df<-NULL
# }
# 
# 
# 
# table(paste(test_df$distance,"operations"),paste(test_df$N,"letters"))
# ggplot(test_df,aes(x=as.numeric(gsub(" pts","",rewMag)),y=as.numeric(distance),color=as.factor(N)))+geom_point()+
# xlab("reward magnitude")+ylab("distance")+geom_hline(yintercept = 3.5)+geom_vline(xintercept = 50)

####Distance gen:
trimN = 3
sel_letters<-LETTERS[(1+trimN):(length(LETTERS)-trimN)]
dist_range <- 1
n_letters <- 3:9
rewMag = 10:90
fixed_distance_move<-do.call(rbind,lapply(dist_range,function(distx){
  #print(distx)
  seq_letters<-sapply(1:10,function(x){
    seq(x,length(sel_letters),by = (distx+1))
  })
  dx<-unlist(lapply(seq_letters,function(xe){
    x <- sel_letters[xe]
    unlist(lapply(n_letters,function(letterN){
      if(length(x)<letterN){return(NULL)}
      lapply(0:(length(x)-letterN-1),function(y){
        x[(1:letterN)+y]
      })
    }),recursive = F)
  }),recursive = F)
  result_end<-data.frame(Ndist=rep(distx,length(dx)),stringsAsFactors = F)
  result_end$letterList <- dx
  result_end$NLetters<-sapply(result_end$letterList,length)
  return(result_end)
}))
fixed_distance_move<-fixed_distance_move[!duplicated(fixed_distance_move$letterList),]
fixed_distance_move<-fixed_distance_move[fixed_distance_move$NLetters %in% n_letters,]
fixed_distance_move<-fixed_distance_move[order(fixed_distance_move$NLetters),]

AllLetters<-do.call(rbind,lapply(1:nrow(fixed_distance_move),function(indexX){
  dx <- fixed_distance_move$letterList[[indexX]]
  gtx<-data.frame(reorderLetters=apply(gtools::permutations(n=length(dx),r = length(dx),v=dx,set = TRUE,repeats.allowed = F),1,paste,collapse=""),
             originalLetters=paste(dx,collapse = ""),Ndist=fixed_distance_move$Ndist[[indexX]],NLetters=fixed_distance_move$NLetters[[indexX]],stringsAsFactors = F)
  gtx$editDistance<-stringdist::stringdist(gtx$originalLetters,gtx$reorderLetters,method = "dl")
  gtx <- gtx[gtx$editDistance!=0,]
  return(gtx)
}))
SubAllLetters<-AllLetters[AllLetters$editDistance==2,]

ref_x<-as.data.frame(table(SubAllLetters$Ndist,SubAllLetters$NLetters))
#ref_x <- ref_x[ref_x$Var1 %in% 0:4 & ref_x$Var2 %in% 5:8,]



#Generate contingency;

N_per_con = 24
#Fixed Letter Distance but different Edit Distance: 
##Fixed letter distance at 2

####spliting into different Ndist for target letter and rewardMag randomization:
for (nx in 1:100){
  testDf<-do.call(rbind,lapply(1:nrow(ref_x),function(i){
    if (ref_x$Freq[i]==0) {
      #Find the nearest: 
      max_xd <- max(as.numeric(as.character(ref_x$Var2[ref_x$Var1 == ref_x$Var1[i] & ref_x$Freq!=0])))
      le_tAdd <- as.numeric(as.character(ref_x$Var2[i])) - max_xd
      gx<-SubAllLetters[SubAllLetters$Ndist==ref_x[i,1] & SubAllLetters$NLetters==max_xd,]
      gx$cor_pos <- sapply(gx$NLetters,function(x){sample.int(x,1,replace = F)})
      gx$target_letter <- substr(gx$originalLetters,start = gx$cor_pos,stop = gx$cor_pos)
      gx$N_filler <- le_tAdd
      for (ix in 1:le_tAdd){
        letterx<-sapply(gx$reorderLetters,function(x){
          sample(x = c("A","B","C","X","Y","Z")[which(!stringi::stri_detect_fixed(x,c("A","B","C","X","Y","Z")))],size=1,replace = F)
        },simplify = T,USE.NAMES = F)
        f_b<-sample(c(1,0),size=nrow(gx),replace = T)
        #1s
        gx$reorderLetters[as.logical(f_b)]<-paste(letterx[as.logical(f_b)],gx$reorderLetters[as.logical(f_b)],sep = "")
        #0s
        gx$reorderLetters[!as.logical(f_b)]<-paste(gx$reorderLetters[!as.logical(f_b)],letterx[!as.logical(f_b)],sep = "")
        #done
        gx$cor_pos <-gx$cor_pos + as.numeric(letterx %in% c("A","B","C"))
      }
      gx$NLetters <- gx$NLetters + le_tAdd
      gx$originalLetters <- sapply(gx$reorderLetters,function(x){paste(sort(strsplit(x,"")[[1]]),collapse = "")},USE.NAMES = F)
      
    } else {
      gx<-SubAllLetters[SubAllLetters$Ndist==ref_x[i,1] & SubAllLetters$NLetters==ref_x[i,2],]
      gx$cor_pos <- sapply(gx$NLetters,function(x){sample.int(x,1,replace = F)})
      gx$target_letter <- substr(gx$originalLetters,start = gx$cor_pos,stop = gx$cor_pos)
      gx$N_filler <- 0
    }
    
    gx<-gx[sample(nrow(gx),N_per_con,replace = F),]
    gx$rewMag<-paste(sample(rewMag,nrow(gx),replace = F),"pts")
    gx$effort_q <- rep(c(1,0),nrow(gx)/2)[sample.int(nrow(gx),nrow(gx))]
    return(gx)
  }))
  
  testDf$list_og <- sapply(strsplit(testDf$reorderLetters,""),paste,collapse=" ")
  testDf$list_sort <- testDf$originalLetters
  testDf$N <- testDf$NLetters
  testDf <- testDf[c("list_og","list_sort","N","cor_pos","target_letter","rewMag","Ndist","editDistance","N_filler","effort_q")]
  
  row.names(testDf)<-NULL 
  testDf <- testDf[sample(nrow(testDf),nrow(testDf),replace = F),]
  write.csv(testDf,file = file.path("./conditionsheets",paste0("contingency_",nx,".csv")),row.names = F)
  testDf<-NULL
}






