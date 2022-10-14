class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans=[]
        for i in range(len(l)):
            temp = nums[l[i]:r[i]+1]
            temp.sort()
            # print(temp)
            if len(temp)<=2:
                ans.append(True)
                continue
            diff = temp[1]-temp[0]
            for i in range(1,len(temp)):
                if diff!=(temp[i]-temp[i-1]):
                    ans.append(False)
                    break
            else:
                ans.append(True)
        return ans