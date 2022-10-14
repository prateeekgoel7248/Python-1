class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        n = len(nums)
        dp, dpPrev = 0, 0
        ans = 0
        for i in range(2, n):
            if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]:
                dp = dpPrev + 1
            ans += dp
            dpPrev = dp
            dp = 0
        return ans
        """
        :type nums: List[int]
        :rtype: int
        """
        