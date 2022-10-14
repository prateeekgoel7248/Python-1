class Solution:
    # @param A : integer
    # @return a list of integers
    def allFactors(self, A):
        from math import sqrt
        ans=[]
        ans2=[]
        #we are taking the square root of a like sqrt(6)=2 so we are taking 1,2 and we got 1,2, and 6 and 3 also
        for i in range(1,int(sqrt(A)+1)):
            if A%i==0:
                ans.append(i)
                if i!=A//i:
                    ans2.append(A/i)
        ans2=ans2[::-1]
        for i in ans2:
            ans.append(i)
        return ans
        
