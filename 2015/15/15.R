

setwd("/media/diskC/Documents and Settings/miha/Documents/adventofcode/15/")

library(stringr)

matrika <- rep(0, 5)
l <- readLines(con <- file("input.txt", encoding = "utf-8"))
for (line in l){
  r <- gregexpr("(-\\d+)|(\\d+)", line)
  stevilke <- as.integer(unlist(regmatches(line, r)))
  matrika <- rbind(matrika, stevilke)
}
cals <- matrika[-1,ncol(matrika)]
matrika <- matrika[-1,-ncol(matrika)]
close(con)



opt.fun <- function(w, data, cals){
  
   w <- w/sum(w)
   w <- 100*w
   w <- round(w)
  print(sum(w))
  vr <- apply(data, 2, function(x) (x %*% w))
  cals <- cals %*% w
  vr[vr < 0] <- 0
  vr <- prod(vr)

  
  # part1
  # disable if you want to calc part2
  if (sum(w) != 100){
    vr <- vr - abs(sum(w) - 100)*10^6
    
  }
  
  # part2
  # disable if you want to calc part1
#   if (cals != 500){
#     vr <- vr - abs(cals - 500)^40
#   }



  return (-vr)
}




sp.meje <- rep(0, 4)
zg.meje <- rep(100, 4)
out <- DEoptim(fn=opt.fun,
               lower=sp.meje,
               upper=zg.meje,
               control = DEoptim.control(
                 VTR = -Inf,
                 CR = 0.5,
                 F = 0.8,
                 itermax= 250,
                 trace = TRUE),
               data = matrika,
               cals = cals)
w <- out$optim$bestmem
w <- w/sum(w)
w <- 100*w
w <- round(w)
out$optim$bestval

