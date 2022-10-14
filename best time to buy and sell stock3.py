class Solution(object):
    def maxProfit(self, prices):
        # def solve(day,buy,cap,dp):
        #     if day==len(prices):
        #         return 0
        #     if cap==0:
        #         return 0
        #     profit=0
        #     if dp[day][buy][cap]!=-1:
        #         return dp[day][buy][cap]
        #     if buy: 
        #         profit  = max(-prices[day]+solve(day+1,not buy,cap,dp),solve(day+1,buy,cap,dp))
        #     else:
        #         profit = max(prices[day]+solve(day+1,not buy,cap-1,dp),solve(day+1,buy,cap,dp))
        #     dp[day][buy][cap]=profit
        #     return profit
        # dp=[[[0 for j in range(3)] for _ in range(2)] for i in range(len(prices)+1)]
        after = [[0 for j in range(3)] for _ in range(2)]
        curr=[[0 for j in range(3)] for _ in range(2)]
        # return solve(0,True,2,dp)
        for day in range(len(prices)-1,-1,-1):
            for buy in range(2):
                for cap in range(1,3):
                    profit=0
                    if buy: 
                        profit  = max(-prices[day]+after[not buy][cap],after[buy][cap])
                    else:
                        profit = max(prices[day]+after[not buy][cap-1],after[buy][cap])
                    curr[buy][cap]=profit
            after = curr[:]
        return curr[1][2]

                    
        
        