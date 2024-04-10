from client import Client 
from database import Database
from random import randint
from server import Server
from util import distance

# randomly generates a vector with 'q' bits in each component, and 'dim' dimensions
def genVector(dim: int, q: int) -> list[int]: 
  vector = []
  for i in range(dim): 
    vector.append(randint(0,2**q-1))
  return vector

# randomly generates a database of feature vectors
def genDatabase(size: int, dim: int, q: int) -> Database: 
  featureVectors: list[list[int]] = []
  for i in range(size): 
    featureVectors.append(genVector(dim,q))
  return Database(featureVectors, q)

# finds nearestNeighbour to q in a set of feature vectors 'vectors'
def getNearestNeighbour(vectors, q): 
  result = vectors[0]
  for v in vectors: 
    if (distance(v, q) < distance(result,q)): 
      result = v
  return result

# Builds a database + server using featureVectors  
# then runs a client query using each queryVector from 'queries' 
# q is the number of bits in each component of any vector
def runBatch(featureVectors: list[list[int]], queries: list[list[int]], q: int): 
  database = Database(featureVectors, q)
  server = Server(database)
  csvformat = "distance from query to ANN" + "distance from query to NN" + "ratio of dANN/dNN"
  
  print(csvformat)

  for query in queries: 
    query = list(query)
    ann = Client.query(query, database, server)
    nn = getNearestNeighbour(featureVectors, query)
    d1 = distance(ann,query)
    d2 = distance(nn,query)
    print(d1,d2,d1/d2)


# A few small sanity checks 
def initialTests(): 
  runBatch([[0,0],[1,1]], [[0,0],[1,1],[5,5]],8)
  runBatch([[3],[7]],[[4]],8)

# executes runBatch using the first 'featureVectorCnt' vectors in 'datasetname' 
# as feature vectors, and the rest as query vectors
# datasetname: name of the csv file storing the dataset
# featureVectorCnt: number of vectors to use as feature vectors
# q: number of bits in each dimension of the vector (defaults to 32)
def runCSV(datasetname: str, featureVectorCnt: int, queryVectorCnt: int, q: int = 32): 
  from util import readCsvDataset
  vectors = readCsvDataset(datasetname)

  featureVectors = []
  queryVectors = []

  cnt = 0
  
  def mod(x): return (x%(2**q)+2**q)%(2**q)
  for vector in vectors: 
    vector = list(map(mod, vector))  # ensure all coordinates are positive, fit in q bits
    if cnt < featureVectorCnt: 
      featureVectors.append(vector)
    elif cnt < featureVectorCnt + queryVectorCnt: 
      queryVectors.append(vector)
    else: 
      break
    cnt = cnt + 1

  runBatch(featureVectors, queryVectors,q)

# run tests based on CSV datasets
def main():
  # name of csv files of datasets (sets of vectors)
  datasets = ['datasets/mnist-784-euclidean_test.csv']
  for dataset in datasets:
    # 20 feature vectors, 50 query vectors, 32 bits of precision
    runCSV(dataset, 20, 50, 32) 




#initialTests()
main()

