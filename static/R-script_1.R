

# Test
Test <- function(){
  print('-------hello world--------')
  print(pi)
}

# Test1
Test1 <- function(a=4){
  # print('this is a self-defined function with arg')
  # print('result is arg*2')
  result = a*2
  ## here should be NOTICE: must be return 'result'. must not return (a*2).
  ## if do, it will error: arg would not be used
  return(result)
}

# normal
fun_normal <- function(sample_size, mean_value, sd_value, decimal_places){
  sample_size=as.numeric(sample_size)
  mean_value=as.numeric(mean_value)
  sd_value=as.numeric(sd_value)
  decimal_places=as.numeric(decimal_places)
  result <- round(rnorm(sample_size, mean_value, sd_value),decimal_places)
  result <- paste0(result,sep="",collapse="|")
  return(result)
}
##############     R-script_1.py     ##############