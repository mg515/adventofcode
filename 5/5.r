# http://adventofcode.com/day/5

setwd("/media/diskC/Documents and Settings/miha/Documents/adventofcode/5/")


library(stringr)
l <- readLines(con <- file("input.txt", encoding = "utf-8"))
close(con)

check_nice <- function(string){
  cond1 <- length(unlist(gregexpr("[aeiou]", string))) >= 3
  cond2 <- unlist(gregexpr('(\\w*)(\\w)\\2(\\w*)', string)) == 1
  cond3 <- unlist(gregexpr('ab|cd|pq|xy', string)) == -1
  
  return (cond1 && cond2 && cond3)
}
sol <- unlist(lapply(l, function(x) check_nice(x)))


check_nice2 <- function(string){
  cond4 <- unlist(gregexpr('\\w*(\\w\\w)\\w*(\\1)', string)) == 1
  cond5 <- unlist(gregexpr('\\w*(\\w)[A-z](\\1)', string)) == 1
 
  return (cond4 && cond5)
}
sol2 <- unlist(lapply(l, function(x) check_nice2(x)))