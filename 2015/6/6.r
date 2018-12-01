# http://adventofcode.com/day/6

setwd("/media/diskC/Documents and Settings/miha/Documents/adventofcode/6/")


l <- readLines(con <- file("input.txt", encoding = "utf-8"))
close(con)

data_matrix <- matrix(0, nrow=1000, ncol=1000)

for (i in 1:length(l)){
  
  r <- regexpr("toggle|turn off|turn on", l[i])
  r <- unlist(regmatches(l[i], r))
  
  coord <- gregexpr("\\d+", l[i])
  coord <- as.numeric(unlist(regmatches(l[i], coord))) + 1
  
  switch(r,
         "turn on" = {
           data_matrix[coord[1]:coord[3], coord[2]:coord[4]] <- data_matrix[coord[1]:coord[3], coord[2]:coord[4]] + 1
         },
         "turn off" = {
           data_matrix[coord[1]:coord[3], coord[2]:coord[4]] <-data_matrix[coord[1]:coord[3], coord[2]:coord[4]] - 1
         },
         "toggle" = {
           data_matrix[coord[1]:coord[3], coord[2]:coord[4]] <- data_matrix[coord[1]:coord[3], coord[2]:coord[4]] + 2
         })
  data_matrix[data_matrix < 0] <- 0
}
 
