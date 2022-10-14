class Solution(object):
    def maxProfit(self, prices, fee):
        # def solve(ind,buy,dp):
        #     if ind >= len(prices):
        #         return 0
        #     if dp[ind][buy]!=-1:
        #         return dp[ind][buy]
        #     if buy:
        #         dp[ind][buy] = max(-prices[ind]+solve(ind+1,not buy,dp),solve(ind+1,buy,dp))
        #     else:
        #         dp[ind][buy] = max(prices[ind]-fee+solve(ind+1,not buy,dp),solve(ind+1,buy,dp))
        #     return dp[ind][buy]
        # dp=[[-1,-1] for _ in range(len(prices)+1)]
        # return solve(0,True,dp)
        cur=[0,0]
        next = [0,0]
        n=len(prices)
        for ind in range(n-1,-1,-1):
            cur[1] = max(-prices[ind]+next[0],next[1])
            cur[0] = max(prices[ind]-fee+next[1],next[0])
            
            next=cur[:]
        return next[1]
        
        