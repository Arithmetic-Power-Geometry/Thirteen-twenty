#include <algorithm>
#include <fstream>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;
int main(int argc,char**argv){ofstream out(argc>1?argv[1]:"certificate.csv");out<<"a,b,numerator,denominator,equality\n";int count=0,viol=0,eq=0;
for(int b=1;b<=196;b++)for(int a=1;a<=b;a++){if(gcd(a,b)!=1)continue;int c=a+b;long long D=16LL*a*b*c;vector<long long> p={0,D};for(int v:{a,b,c}){long long s=D/(16LL*v);for(int j=0;j<v;j++){p.push_back((16LL*j+1)*s);p.push_back((16LL*j+15)*s);}}sort(p.begin(),p.end());p.erase(unique(p.begin(),p.end()),p.end());long long N=0;for(size_t i=1;i<p.size();i++){long long m=p[i-1]+p[i],period=2*D;bool ok=true;for(int v:{a,b,c}){long long r=v*m%period;if(16*min(r,period-r)<period){ok=false;break;}}if(ok)N+=p[i]-p[i-1];}count++;viol+=20*N<13*D;eq+=20*N==13*D;out<<a<<","<<b<<","<<N<<","<<D<<","<<(20*N==13*D)<<"\n";}
cerr<<"tested="<<count<<" violations="<<viol<<" equality="<<eq<<"\n";return viol?1:0;}