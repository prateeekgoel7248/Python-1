import sys
def maxProfit(values, weights, n, w):

    def solve(ind,target,dp):
        if ind==0:
            if target>=weights[ind]:
                return values[ind]
            return 0
        if dp[ind][target]!=-1:
            return dp[ind][target]
        take=-sys.maxsize
        if target>=weights[ind]:
            take = values[ind]+solve(ind-1,target-weights[ind],dp)
        notTake = solve(ind-1,target,dp)
        dp[ind][target]=max(take,notTake)
        return dp[ind][target]
    dp=[[0 for _ in range(w+1)] for i in range(n+1)]
    prev = [0 for _ in range(w+1)]
#     cur = [0 for _  in range(w+1)]
#     return solve(n-1,w,dp)
    for i in range(weights[0],w+1,1):
        prev[i]=values[0]
    for ind in range(1,n):
        for target in range(w,-1,-1):
            take=-sys.maxsize
            if target>=weights[ind]:
                take = values[ind]+prev[target-weights[ind]]
            notTake = prev[target]
            prev[target]=max(take,notTake)
#         prev = cur[:]
    return prev[w]
            
            
    
    


