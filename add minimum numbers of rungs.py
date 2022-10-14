class Solution:
    def addRungs(self, rungs: List[int], k: int) -> int:
        cnt=0
        prev=0
        for i in rungs:
            if i-prev <=k:
                prev=i
            else:
                cnt+=(i-1-prev)//k
                prev=i
        return cnt
            