int dp[501][501][2];


int helper(vector<int> &A, int curr, int n, int K, bool hasBought){

    if(curr==n){

        return 0;

    }

    if(K==0){

        return 0;

    }

    if(dp[curr][K][hasBought]!=-1){

        return dp[curr][K][hasBought];

    }

    int profit=0;

    if(hasBought==false){

        int BUY=(-A[curr])+helper(A,curr+1,n,K,true);

        int NOT_BUY=helper(A,curr+1,n,K,hasBought);

        profit=max(BUY,NOT_BUY);

    }

    else{

        int SELL=A[curr]+helper(A,curr+1,n,K-1,false);

        int NOT_SELL=helper(A,curr+1,n,K,hasBought);

        profit=max(SELL,NOT_SELL);

    }

    return dp[curr][K][hasBought]=profit;

}
int Solution::solve(vector<int> &A, int B) {
    memset(dp,-1,sizeof(dp));

    int n=A.size();

    B=min(B,n);

    return helper(A,0,n,B,false);
}
