from math import ceil, log

def distance(v1, v2): 
  result = 0
  for x,y in zip(v1,v2): 
    result += (x-y)**2
  return result

def countbits(val: int) -> int: 
  return ceil(log(val,2))