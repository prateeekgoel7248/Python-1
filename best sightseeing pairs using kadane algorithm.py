class Solution(object):
    def maxScoreSightseeingPair(self, a):
        max_so_far,result = a[0],0
        
        for i in range(1,len(a)):
            result = max(result, max_so_far + a[i] - i)
            max_so_far = max(max_so_far, a[i] + i)
			
        return result