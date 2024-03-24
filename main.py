from client import Client 
from database import Database
from random import randint
from server import Server
from util import distance

def genVector(dim: int, q: int) -> list[int]: 
  vector = []
  for i in range(dim): 
    vector.append(randint(0,2**q-1))
  return vector

def genDatabase(size: int, dim: int, q: int) -> Database: 
  featureVectors: list[list[int]] = []
  for i in range(size): 
    featureVectors.append(genVector(dim,q))
  return Database(featureVectors, q)

def getNearestNeighbour(vectors, q): 
  result = vectors[0]
  for v in vectors: 
    if (distance(v, q) < distance(result,q)): 
      result = v
  return result

def runBatch(featureVectors: list[list[int]], queries: list[list[int]], q: int): 
  database = Database(featureVectors, q)
  server = Server(database)
  for query in queries: 
    ann = Client.query(query, database, server)
    nn = getNearestNeighbour(featureVectors, query)
    d1 = distance(ann,query)
    d2 = distance(nn,query)
    print(ann, nn, d1,d2)


def main(): 
  runBatch([[0,0],[1,1]], [[0,0],[1,1],[5,5]], 8)
  runBatch([[3],[7]],[[4]],8)
  


main()

