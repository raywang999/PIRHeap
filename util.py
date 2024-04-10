from math import ceil, log

def distance(v1, v2): 
  result = 0
  for x,y in zip(v1,v2): 
    result += (x-y)**2
  return result

def countbits(val: int) -> int: 
  return ceil(log(val,2))

# reads a csv of vectors into a list of vectors
def readCsvDataset(name: str) -> list[list[int]]: 
  import csv
  csvfile = open(name, newline='')
  vectors  = map(lambda vs: map(lambda v: int(float(v)), vs), list(csv.reader(csvfile)))
  return vectors