
from database import Database

# Stores a mapping of 
class Server: 
  buckets: dict[int,int] = {} 
  def __init__(self, database: Database):
    for k,v in database._middle.items(): 
      self.buckets[k] = database.encode((v,0))

  # returns a list 
  def preco(self, queryBuckets: list[int]) -> list[int | None]: 
    # TODO 
    return map(self.buckets.get, queryBuckets)