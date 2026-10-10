// Experiment 30: exact finite certificates for q=5,...,10.
// Build: g++ -O2 -std=c++17 src/experiment_30.cpp -o experiment_30
// Run: ./experiment_30
#include <algorithm>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;
long long measure(int q,int a,int b) {
 int c=a+b;
 long long D=1LL*q*a*b*c,P=2*D;
 vector<long long> v={0,D};
 for(int x:{a,b,c}) {
  long long s=D/(1LL*q*x);
  for(int j=0;j<x;j++) {
   v.push_back((1LL*q*j+1)*s);
   v.push_back((1LL*q*(j+1)-1)*s);
  }
 }
 sort(v.begin(),v.end());
 v.erase(unique(v.begin(),v.end()),v.end());
 long long z=0;
 for(size_t i=1;i<v.size();i++) {
  long long m=v[i-1]+v[i];
  bool ok=true;
  for(int x:{a,b,c}) {
   long long r=(x*m)%P;
   if(q*min(r,P-r)<P) {ok=false;break;}
  }
  if(ok) z+=v[i]-v[i-1];
 }
 return z;
}
int main(){
 cout<<"q,cutoff,finite_pairs,violations,equalities,equality_a,equality_b\n";
 int failures=0;
 for(int q=5;q<=10;q++){
  int B=(2*q*q*(q-1)+3*(q-3)-1)/(3*(q-3));
  long long cases=0,eq=0,viol=0;
  int ea=0,eb=0;
  for(int b=1;b<B;b++)for(int a=1;a<=b;a++)if(gcd(a,b)==1){
   long long n=measure(q,a,b),d=1LL*q*a*b*(a+b);
   cases++;
   long long l=n*q*(q-1),r=d*(q-3)*(q-4);
   if(l<r)viol++;
   if(l==r){eq++;ea=a;eb=b;}
  }
  cout<<q<<","<<B<<","<<cases<<","<<viol<<","<<eq<<","<<ea<<","<<eb<<"\n";
  if(viol || eq!=1 || ea!=1 || eb!=q-2) failures++;
 }
 return failures?1:0;
}
