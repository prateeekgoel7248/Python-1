def maximumProfit(prices, n, k):

#         after = [[0 for j in range(k+1)] for _ in range(2)]
#         curr=[[0 for j in range(k+1)] for _ in range(2)]
#         # return solve(0,True,2,dp)
#         for day in range(len(prices)-1,-1,-1):
#             for buy in range(2):
#                 for cap in range(1,k+1):
#                     profit=0
#                     if buy: 
#                         profit  = max(-prices[day]+after[not buy][cap],after[buy][cap])
#                     else:
#                         profit = max(prices[day]+after[not buy][cap-1],after[buy][cap])
#                     curr[buy][cap]=profit
#             after = curr[:]
#         return curr[1][k]
    after = [0]*(2*k+1)
    cur=after[:]
    
    for ind in range(n-1,-1,-1):
        for tranNo in range(2*k-1,-1,-1):
            if tranNo%2==0:
                cur[tranNo] = max(-prices[ind]+after[tranNo+1],after[tranNo])
            else:
                cur[tranNo] = max(prices[ind]+after[tranNo+1],after[tranNo])
        after = cur[:]
    return after[0]
                
                
                
                
                
                
                
                