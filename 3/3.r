# http://adventofcode.com/day/3

setwd("/media/diskC/Documents and Settings/miha/Documents/adventofcode/3/")

l <- readLines(con <- file("input.txt", encoding = "utf-8"))
str <- unlist(strsplit(l, ""))
close(con)

pos <- c(0,0)
positions1 <- list(pos)
for (i in str[(1:length(str)) %% 2 == 1]){
  
  switch(i,
         "^" = {
           pos[1] <- pos[1] + 1
         },
         "v" = {
           pos[1] <- pos[1] - 1
         },
         ">" = {
           pos[2] <- pos[2] + 1
         },
         "<" = {
           pos[2] <- pos[2] - 1
         })
  
  positions1 <- c(positions1, list(pos))
}
length(unique(positions1))

pos <- c(0,0)
positions2 <- list(pos)
for (i in str[(1:length(str)) %% 2 == 0]){
  
  switch(i,
         "^" = {
           pos[1] <- pos[1] + 1
         },
         "v" = {
           pos[1] <- pos[1] - 1
         },
         ">" = {
           pos[2] <- pos[2] + 1
         },
         "<" = {
           pos[2] <- pos[2] - 1
         })
  
  positions2 <- c(positions2, list(pos))
}
length(unique(c(positions1, positions2)))

