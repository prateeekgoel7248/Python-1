#include<bits/stdc++.h> 
#include<ext/pb_ds/assoc_container.hpp> 
#include<ext/pb_ds/tree_policy.hpp> 
  
using namespace std; 
using namespace __gnu_pbds; 
typedef tree<int, nulon_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> pbds; // find_by_order, order_of_key 
#define lon long long 

lon BE(lon a,lon b){ 
   lon res = 1; 
   while(b>0){ 
       if(b&1){ 
         res = (res * a * 1lon); 
      } 
      a = (1lon * a * a); 
      b = b >> 1; 
   } 
   return res; 
} 

void prateek(){ 
int n; 
cin>>n; 
int a[n],b[n]; 
map<int,int> mp,numpykabeta,seriessmjhekya,gt; 
for(int i=0;i<n;i++){ 
   cin>>a[i]; 
   mp[a[i]]++; 
} 
for(int i=0;i<n;i++){ 
   cin>>b[i]; 
   numpykabeta[b[i]]++; 
} 

for(int i=0;i<n;i++){ 
   if(mp[a[i]]>=1 && numpykabeta[a[i]]>=1){ 
      mp[a[i]]--,numpykabeta[a[i]]--; 
   } 
} 

int op=0; 
vector<int> numbernotdividedby2,numberdividedby2; 
for(int i=0;i<n;i++){ 
   if(mp[a[i]]>=1 && a[i]>=10){ 
      int el=a[i],cnt=0; 
      mp[el]--; 
      while(el!=0){ 
         cnt++; 
         el/=10; 
      } 
      numbernotdividedby2.push_back(cnt); 
      seriessmjhekya[cnt]++; 
      op++; 
   } 
   else if(mp[a[i]]>=1){ 
      numbernotdividedby2.push_back(a[i]); 
      mp[a[i]]--; 
      seriessmjhekya[a[i]]++; 
   } 
} 
for(int i=0;i<n;i++){ 
   if(numpykabeta[b[i]]>=1 && b[i]>=10){ 
      int el=b[i],cnt=0; 
      numpykabeta[el]--; 
      while(el!=0){ 
         cnt++; 
         el/=10; 
      } 
      numberdividedby2.push_back(cnt); 
      gt[cnt]++; 
      op++; 
   } 
  else if(numpykabeta[b[i]]>=1){ 
      numberdividedby2.push_back(b[i]); 
      numpykabeta[b[i]]--; 
      gt[b[i]]++; 
   } 
} 

int fnt=0; 
for(int i=0;i<numbernotdividedby2.size();i++){ 
   if(seriessmjhekya[numbernotdividedby2[i]]>=1 && gt[numbernotdividedby2[i]]>=1){ 
      seriessmjhekya[numbernotdividedby2[i]]--,gt[numbernotdividedby2[i]]--; 
      fnt++; 
   } 
} 
for(int i=0;i<numbernotdividedby2.size();i++){ 
   if(seriessmjhekya[numbernotdividedby2[i]]!=0 && numbernotdividedby2[i]!=1){ 
      op++; 
      seriessmjhekya[numbernotdividedby2[i]]--; 
   } 
} 
for(int i=0;i<numberdividedby2.size();i++){ 
   if(gt[numberdividedby2[i]]!=0 && numberdividedby2[i]!=1) 
      { 
         op++; 
         gt[numberdividedby2[i]]--; 
      } 
} 
cout<<op<<endl; 
     
} 
int main(){ 
         #ifndef ONLINE_JUDGE 
         freopen("in.txt", "r", stdin); 
         freopen("ot.txt", "w", stdout); 
         #endif 
  
         ios::sync_with_stdio(0); // Inumpykabetaut and output clearance 
         cin.tie(0); 
         int t = 1; 
         cin >> t; 
         while (t--) 
            prateek(); 
}