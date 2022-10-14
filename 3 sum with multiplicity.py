class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        from collections import defaultdict
        d=defaultdict(int)
        ans=0
        for i in range(len(arr)):
            ans=(ans+d[target-arr[i]])%(pow(10,9)+7)
            for j in range(i):
                d[arr[i]+arr[j]]+=1
        return ans
        