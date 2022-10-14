class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        # if sum(nums[-3:])<=target:
        #     return sum(nums[-3:])
        # if sum(nums[:3])>=target:
        #     return sum(nums[:3])
        ans=[sys.maxsize,0]
        n=len(nums)
        for i in range(n-2):
            low=i+1
            high=n-1
            while low<high:
                temp = nums[low]+nums[high]+nums[i]
                if abs(temp-target)<ans[0]:
                    ans[0]=abs(temp-target)
                    ans[1]=temp
                if temp>target:
                    high-=1
                elif temp<target:
                    low+=1
                else:
                    return temp
        return ans[1]