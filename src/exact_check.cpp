#include <algorithm>
#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>
using namespace std;
struct Result {int a,b; long long good,D;};
Result measure(int a,int b) {
 const int c=a+b;
 const long long D=16LL*a*b*c;
 vector<long long> ends={0,D};
 for (int v: {a,b,c}) {
   const long long step=D/(16LL*v);
   for (int j=0;j<v;++j) {
     ends.push_back((16LL*j+1)*step);
     ends.push_back((16LL*j+15)*step);
   }
 }
 sort(ends.begin(),ends.end());
 ends.erase(unique(ends.begin(),ends.end()),ends.end());
 long long good=0,period=2*D;
 for (size_t i=1;i<ends.size();++i) {
   const long long L=ends[i-1],U=ends[i],middle2=L+U;
   bool safe=true;
   for (int v: {a,b,c}) {
     const long long r=(v*middle2)%period;
     if (16*min(r,period-r)<period) {safe=false;break;}
   }
   if (safe) good+=U-L;
 }
 return {a,b,good,D};
}
int main(int argc,char **argv) {
 const string dest = argc>1 ? argv[1] : "exact_results.csv";
 ofstream out(dest);
 if (!out) {cerr<<"Cannot open output: "<<dest<<"\n";return 2;}
 out<<"a,b,numerator,denominator,decimal,equal_13_20\n";
 int total=0,violations=0,equality=0;
 long double best=2;
 Result minr{};
 for (int b=1;b<=196;++b) for(int a=1;a<=b;++a) {
   if (gcd(a,b)!=1) continue;
   auto r=measure(a,b);
   ++total;
   if (20*r.good<13*r.D) {++violations;cerr<<"VIOLATION "<<a<<" "<<b<<"\n";}
   if (20*r.good==13*r.D) ++equality;
   long double f=(long double)r.good/r.D;
   if (f<best) {best=f;minr=r;}
   out<<a<<","<<b<<","<<r.good<<","<<r.D<<","<<setprecision(16)<<f<<","<<(20*r.good==13*r.D)<<"\n";
 }
 cerr<<"tested="<<total<<" violations="<<violations<<" equality="<<equality
 <<" minimum="<<minr.a<<","<<minr.b<<"="<<minr.good<<"/"<<minr.D<<"\n";
 return violations?1:0;
}
