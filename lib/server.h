#ifndef SERVER_H
#define SERVER_H

#include "database.h"
#include <set>

// Implements the server lookup 
// C is the cypher space 
template<typename C, int Q> 
class Server {
 public: 
  static constexpr int height = Q+1;

 private:
  std::array<std::set<C>, height> nodes;
 public:
  
  // construct the Server from a Database using a cypher function CF, 
  template<int D, typename CF>
  Server(const Database<D,Q>& db, const CF& cf) {
    for (const auto& vec: db){
      for (int i=0; i <= height; ++i){
        nodes[i].insert(cf(Database<D,Q>::getKAncestor(vec, i)));
      }
    }
  }

  // returns for each input node whether it is in nodes
  std::bitset<height> pir(const std::array<C, height+1>& query){
    std::bitset<height> res;
    for (int i = 0; i <= height; ++i){
      res[i] = nodes[i].count(query[i]);
    }
    return res;
  }

};

template<int D, int Q, typename CF> 
auto makeServer(const Database<D,Q>& db, const CF& cf){
  return Server<decltype(cf(typename Database<D,Q>::vector_t())), Q>(db, cf);
}

#endif
