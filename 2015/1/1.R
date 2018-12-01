# http://adventofcode.com/day/1


setwd("/media/diskC/Documents and Settings/miha/Documents/adventofcode/1/")

l <- readLines(con <- file("input.txt", encoding = "utf-8"))
close(con)

### part1
start <- gregexpr("[(]" ,text=l)
finish <- gregexpr("[)]" ,text=l)

length(unlist(start)) - length(unlist(finish)) 


### part2
progress <- unlist(strsplit(l, ""))
floor <- 0
i <- 1
while (floor >= 0){
  if (progress[i]=="("){
    floor = floor + 1
  } else {
    floor = floor - 1
  }
  i = i + 1
}
i - 1 