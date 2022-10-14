class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        mx=0
        start=0
        end=len(tokens)-1
        tokens.sort()
        ans=0
        while start<=end:
            if tokens[start]<=power:
                power-=tokens[start]
                start+=1
                ans+=1
            else:
                if ans>0:
                    power+=tokens[end]
                    end-=1
                    ans-=1
                else:
                    break
            mx=max(mx,ans)
        return mx
            
            