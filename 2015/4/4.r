# http://adventofcode.com/day/4

input = "bgvyzdsv"

test_zeroes <- function(str, n){
  str <- digest::digest(str,algo='md5', serialize = FALSE)
  splt <- strsplit(str, "")
  first_n <- unlist(splt)[1:n]
  
  if (any(first_n != "0")){
    return (FALSE)
  } else {
    return (TRUE)}
}

n = 5
i <- -1
cond = FALSE
while (!cond){
	i <- i+1
	str <- paste(input, toString(i), sep="")
	cond = test_zeroes(str, n)
}


