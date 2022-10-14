def allocateBooks(arr, n, m):

    # Write your code here
    # Return the minimum number of pages
    def valid(val):
        s=0
        cnt=1
        for i in arr:
            s+=i
            if s>mid:
                cnt+=1
                s=i
        return cnt<=m 
    low=max(arr)
    high=sum(arr)
    ans=high
    while low<=high:
        mid=low+(high-low)//2
        if valid(mid):
#             print(mid)
            ans=min(ans,mid)
            high=mid-1
        else:
            low=mid+1
    return ans
 