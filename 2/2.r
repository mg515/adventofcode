# http://adventofcode.com/day/2

setwd("/media/diskC/Documents and Settings/miha/Documents/adventofcode/2/")

data <- read.table("input.txt", sep="x")


# part1
calc_area <- function(dims){
  dims <- sort(dims)
  area <- 2*dims[1]*dims[2] + 2*dims[1]*dims[3] + 2*dims[2]*dims[3]
  area <- area + dims[1]*dims[2]
  
  return (area)
}
area <- sum(apply(data, 1, function(x) calc_area(x)))


# part2
calc_ribbon <- function(dims){
  dims <- sort(dims)
  ribwrap <- 2*dims[1] + 2*dims[2] + prod(dims)
  
  return (ribwrap)
}
ribbon <- sum(apply(data, 1, function(x) calc_ribbon(x)))

area
ribbon