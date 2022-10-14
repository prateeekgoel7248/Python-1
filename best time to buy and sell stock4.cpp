class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        vector<vector<int>> after(2,vector<int>(k+1,0));
        vector<vector<int>> cur(2,vector<int>(k+1,0));
        int n=prices.size();
        for(int ind=n-1;ind>=0;ind--){
            for(int buy=0;buy<=1;buy++){
                for(int cap=1;cap<=k;cap++){
                    if(buy==1){
                        cur[buy][cap]=max(-prices[ind]+after[0][cap],0+after[1][cap]);
                    }
                    else{
                        cur[buy][cap]=max(prices[ind]+after[1][cap-1],after[0][cap]);
                    }
                }
            }
            after=cur;
        }
        return after[1][k];
    }
};