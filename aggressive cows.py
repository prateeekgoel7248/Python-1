# just an simple question and a variant of allocate books - prefer aaditya verma video for allocate books and striver video for the aggressive cow


def aggressiveCows(stalls, k):
    def valid(val):
        cnt=1
        pos=stalls[0]
        for i in stalls[1:]:
            if i-pos>=val:
                cnt+=1
                pos=i
            if cnt==k:
                return True
        return False
    # Write your code here.
    stalls.sort()
    low=0
    high=stalls[-1]-stalls[0]
    mx=low
    while low<=high:
        mid=low+(high-low)//2
#         print(mid)
        if valid(mid):
#             print(mid)
            mx=max(mx,mid)
            low=mid+1
        else:
            high=mid-1
    return mx