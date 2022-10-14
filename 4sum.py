class Solution(object):
    def fourSum(self, nums, target):
        res, N = set(), len(nums)
        nums.sort()
        for i in range(N-3):
            for j in range(i+1, N-2):
                l, r = j + 1, N - 1
                while l < r:
                    sum4 = nums[i] + nums[j] + nums[l] + nums[r]
                    if sum4 == target:
                        res.add((nums[i],nums[j],nums[l],nums[r]))
                    if sum4 < target: l += 1
                    else: r -=1
        return list(res)