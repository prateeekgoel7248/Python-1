class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, nums, target):
        # from collections import Counter,defaultdict
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return [d[m], i+1]
            else:
                if n not in d:
                    d[n] = i+1
        return []
