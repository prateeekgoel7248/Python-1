class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        def vowel(v):
            if v=='a' or  v=='e' or v=='i' or v=='o' or v=='u' or v=="A" or v=="E" or v=='I' or v=="O" or v=="U":
                return True
            else:
                return False
        s=0
        for i in range(len(A)):
            if vowel(A[i]):
                s=s+(len(A)-i)
        return s%10003