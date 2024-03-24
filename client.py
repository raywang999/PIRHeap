from database import Database
from server import Server

# Class represnting client methods 
class Client: 
  # query ANN using a database's getKthAncestor method
  def query(vector: list[int], database: Database, server: Server) -> list[int]: 
    queryIDs: list[int] = []
    for k in range(database.getHeight()): 
      queryIDs.append(database.toID(Database.getKthAncestor(vector,k)))
    for result in server.pir(queryIDs): 
      if result is not None: 
        return database.toNode(result)[0]
    