#ifndef DATABASE_H
#define DATABASE_H

#include <vector>
#include <array>
#include <bitset>
#include <initializer_list>

// Implements the quantization tree 
// Q is the granularity of the quantization 
// D is the dimension of the vector space V = N^D\N
// - where N = Z mod 2^Q
// CF is the cypher function F: V -> C
template<int D, int Q> 
class Database {
 public: 
  using vector_t = std::array<std::bitset<Q>, D>;
 private:
  std::vector<vector_t> featureVectors;
 public: 

  // insert feature vector
  template<typename T>
  void insert(const std::initializer_list<T>& l){ 
    vector_t res; int i=0;
    for (auto& v: l){
      res[i++] = std::bitset<Q>(v);
    }
    featureVectors.push_back(res); 
  }

  // return's kth ancestor of a vector
  static vector_t getKAncestor(const vector_t& vec, int k) {
    vector_t res = vec;
    for (auto& i: res){
      i >>= k;
    }
    return res;
  }

  auto begin(){ return featureVectors.begin(); }
  auto end(){ return featureVectors.end(); }

  auto begin() const { return featureVectors.cbegin(); }
  auto end() const { return featureVectors.cend(); }


};

#endif
