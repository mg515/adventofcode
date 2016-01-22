# http://adventofcode.com/day/9

setwd("/media/diskC/Documents and Settings/miha/Documents/adventofcode/9/")

l <- readLines(con <- file("input.txt", encoding = "utf-8"))
close(con)

# gives the name of the first city
city1f <- function(string){
  a <- regexpr("\\w*\\S", string)
  city1 <- regmatches(string, a)
  return(city1)
}

# gives the names of the second city
city2f <- function(string){
  a <- regexpr("(?<=to\\s)(\\w+)", string, perl=T)
  city2 <- regmatches(string, a)
  return(city2)
}

# gives the distance between the first and the second city
distf <- function(string){
  a <- regexpr("[0-9]+", string)
  dist <- regmatches(string, a)
  return(dist)
}


cities1 <- unlist(unique(lapply(l, function(x) city1f(x))))
cities2 <- unlist(unique(lapply(l, function(x) city2f(x))))
cities <- unique(c(cities1, cities2))
matrika <- matrix(0, nrow=length(cities), ncol=length(cities))
rownames(matrika) <- cities
colnames(matrika) <- cities

# represent the weighted graph with a matrix
for (i in 1:length(l)){
  city1 <- city1f(l[i])
  city2 <- city2f(l[i])
  dist <- distf(l[i])
  
  matrika[city1, city2] <- as.numeric(dist)
}
matrika <- matrika + t(matrika)

# brute force the solution
min <- 0
perms <- permutations(length(cities), length(cities))
for (j in 1:factorial(length(cities))){
  perm <- perms[j,]
  dist <- 0
  for (i in 1:(length(perm)-1)){
    dist <- dist + matrika[perm[i], perm[i+1]]
  } 
  if (dist>min){
    min <- dist
  }
}
min
