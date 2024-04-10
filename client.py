from database import Database
from server import Server

# Class represnting client methods 
class Client: 
  # query ANN using a database's getKthAncestor method
  def query(vector: list[int], database: Database, server: Server) -> list[int]: 
    queryIDs: list[int] = []
    for k in range(database.getHeight()): 
      queryIDs.append(database.encode(Database.getKthAncestor(vector,k)))
    for result in Client.pir(queryIDs, server): 
      if result is not None: 
        return database.decode(result)[0]
  
  # returns a list 
  def pir(queryBuckets: list[int], server: Server) -> list[int | None]: 
    # TODO 
    return map(server.buckets.get, queryBuckets)
    