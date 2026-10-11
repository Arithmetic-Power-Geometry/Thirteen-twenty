#include <algorithm>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <vector>
using i64=std::int64_t;
static bool allowed(i64 x,i64 y,i64 D,int a,int b){
  for(i64 v: {i64(a),i64(b),i64(a+b)}){
    i64 z=(v*(x+y))%(2*D);
    if(16*std::min(z,2*D-z)<2*D) return false;
  }
  return true;
}
int main(){
  i64 N=0,V=0,E=0; int eq_a=0,eq_b=0;
  for(int b=1;b<=196;++b) for(int a=1;a<=b;++a){
    if(std::gcd(a,b)!=1)continue;
    i64 D=16*std::lcm(i64(a),std::lcm(i64(b),i64(a+b)));
    std::vector<i64> xs={0,D};
    for(i64 v:{i64(a),i64(b),i64(a+b)}) for(i64 j=0;j<v;++j){
      xs.push_back((16*j+1)*(D/(16*v)));
      xs.push_back((16*j+15)*(D/(16*v)));
    }
    std::sort(xs.begin(),xs.end());xs.erase(std::unique(xs.begin(),xs.end()),xs.end());
    i64 G=0;
    for(size_t k=1;k<xs.size();++k)if(allowed(xs[k-1],xs[k],D,a,b))G+=xs[k]-xs[k-1];
    ++N;
    if(20*G<13*D){++V;std::cerr<<"VIOLATION "<<a<<" "<<b<<"\n";}
    if(20*G==13*D){++E;eq_a=a;eq_b=b;}
  }
  std::cout<<"primitive_pairs="<<N<<"\nviolations="<<V<<"\nequality_cases="<<E<<"\nequality_pair="<<eq_a<<","<<eq_b<<"\n";
  return (N==11698 && V==0 && E==1 && eq_a==1 && eq_b==14)?0:1;
}
