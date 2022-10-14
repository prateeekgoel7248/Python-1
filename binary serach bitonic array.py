class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, Alc, B):

        def BinarySearchASC(A,t):
            s=0
            e=len(A)-1
            
            while s<=e:
                m=s+(e-s)//2
                if A[m]==t:
                    return m
                elif A[m]<t:
                    s=m+1
                else:
                    e=m-1
            return -1
        
        def BinarySearchDESC(A,t):
            s=0
            e=len(A)-1
            
            while s<=e:
                m=s+(e-s)//2
                if A[m]==t:
                    return m
                elif A[m]>t:
                    s=m+1
                else:
                    e=m-1
            return -1
        def PeakElement(A):
            # A=Alpha
            s=0
            e=len(A)-1
            # print(s,e)
            while s<=e:
                m=s+(e-s)//2
                if m>0 and m<len(A)-1:
                    if A[m] > A[m-1] and A[m]>A[m+1]:
                        return m
                    elif A[m-1]>A[m]:
                        e=m-1
                    else:
                        s=m+1
                elif m==0:
                    if A[0] > A[1]:
                        return 0
                    else:
                        return 1
                elif m==len(A)-1:
                    if A[len(A)-1]>A[len(A)-2]:
                        return len(A)-1
                    else:
                        return len(A)-2
                
        p=PeakElement(Alc)
        # print(p)
        a=BinarySearchASC(Alc[:p],B)
        d=BinarySearchDESC(Alc[p+1:],B)
        if a!=-1:
            return a
        elif d!=-1:
            return d+p+1
        else:
            return -1

