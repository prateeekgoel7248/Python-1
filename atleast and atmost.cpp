#include <bits/stdc++.h>
using namespace std;

#define int long long

using ull = uint64_t;
using ii = pair<int, int>;
using iii = tuple<int, int, int>;
using i4 = tuple<int, int, int, int>;
using ll = long long;
const int mod = 1e9+7;
const int ms = 1e6+5;
const int inf = 1e9;

void solve() {
  int n;
  cin >> n;
  vector<int> v(n);
  for(int &x : v) {
    cin >> x;
  }
  sort(v.begin(), v.end());
  if(n == 1) {

  } else if(n == 2) {

  }
  int resp1 = 0, resp2 = 0;
  vector<int> ans(n+1);
  for(int x : v) {
    ans[x]++;
    resp1 += n-x+1;
    resp2++;
  }
  for(int i = 0; i < n; i++) {
    resp1 -= ans[i];
    resp2 -= ans[i];
    int tmp = ans[i] * (n-i);
    cout << resp2 << " " << resp1-tmp << '\n';
  }
}

int32_t main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  cout << fixed << setprecision(3);
   #ifdef ONLINE_JUDGE
    // freopen("boysgirls.in", "r", stdin);
    // freopen("boysgirls.out", "w", stdout);
  #endif
  int t = 1;
  cin >> t;
  while (t--) {
    solve(); 
  }
  return 0;
}
	   		 		   	 			   		 	 		 		