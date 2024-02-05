#include "lib/database.h"
#include "lib/server.h"


template<typename T>
T identity(const T& t){return t;}

template<int D, int Q>
int sumhash(const std::array<std::bitset<Q>, D>& vec){
  int res=0;
  for (auto& bs: vec){
    res += bs.to_ulong();
  }
  return res;
}


int main(){
  Database<1,32> db;
  db.insert({0ll});
  db.insert({1ll});
  //auto srv = makeServer(db, &identity<std::array<std::bitset<32>, 1>>);
  auto srv = makeServer(db, &sumhash<1,32>);


}
