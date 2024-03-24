from util import distance, countbits

# Contains a set of feature vectors.
# Provides methods to obtain parents of feature vectors 
class Database: 
  _idMap: dict[tuple[list[int],int],int] = {}  # maps (Nodes, k) pairs to their ID
  featureVectors: list[list[int]] = []
  
  # maps each Node to the feature vector closest to its center
  _middle: dict[int,list[int]] = {}

  # q = number of bits for granularity of the quantization
  def __init__(self, featureVectors: list[list[int]], q: int): 
    self.featureVectors = featureVectors
    self.q = q
    for vector in featureVectors: 
      for k in range(self.getHeight()): # go up the heap until the root
        currNodeID = self.toID(Database.getKthAncestor(vector,k))
        if currNodeID not in self._middle: 
          self._middle[currNodeID] = vector
        else: 
          center = self._middle[currNodeID]
          if Database._distanceToCenter(vector,k) < Database._distanceToCenter(center, k):
            self._middle[currNodeID] = vector

  def getHeight(self)-> int: 
    return self.q+3

  def _distanceToCenter(vector, k) -> float: 
    centers = Database._getNodeCenters(vector,k)
    return distance(centers, vector)

  def _getNodeCenters(vector: list[int], k: int) -> list[float]: 
    def getCenter(comp: int) -> float: 
      r = comp*2**k + Database._kthOffset(k)
      l = r - 2**k
      return (r-l)/2
    return map(getCenter, Database.getKthAncestor(vector,k)[0])

  # converts a Node in the heap into its corresponding ID
  def toID(self, node: tuple[list[int],int]) -> int: 
    res = 0
    for val in node[0]:
      res = res*2**self.q + val + 1
    return res*2**countbits(self.getHeight()) + node[1]

  # convert an ID into a Node
  def toNode(self, id: int) -> tuple[list[int],int]: 
    heightbits = countbits(self.getHeight())
    k = id%2**heightbits
    id >>= heightbits
    node = []
    while id != 0: 
      node.append((id-1)%(2**self.q))
      id = (id-1)>>self.q
    node.reverse()
    return (node,k)
  

  def _kthOffset(k: int) -> int: 
    if k == 0: return 0
    return 2**(k-1)-1
  
  def _getKthOneDim(comp: int, k: int) -> int: 
    return (comp + 2**(k-1)+1)//(2**k)

  # precondition: k >= 0
  # returns the Node corresponding to the kth ancestor of 'vector'
  def getKthAncestor(vector: list[int], k: int) -> tuple[list[int],int]: 
    if k == 0: 
      return (vector,k)
    # returns the kth ancestor of one component of the vector
    def getKth(comp: int) -> int: return Database._getKthOneDim(comp, k)
    # computes the final bucket ID
    return (map(getKth, vector),k)
  
  