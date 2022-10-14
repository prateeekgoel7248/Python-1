#User function Template for python3
from collections import defaultdict,deque
class Solution:
    def findOrder(self,dict, N, K):
        indegree=[0]*K
        def topoS():
            q=deque()
            for i in range(K):
                if indegree[i]==0:
                    q.append(i)
            topo=[]
            while q:
                node = q.popleft()
                topo.append(node)
                for ele in adj[node]:
                    indegree[ele]-=1
                    if indegree[ele]==0:
                        q.append(ele)
            return topo

        adj = defaultdict(list)
        for i in range(N-1):
            s1 = dict[i]
            s2 = dict[i+1]
            length = min(len(s1),len(s2))
            for ptr in range(length):
                if s1[ptr]!=s2[ptr]:
                    adj[ord(s1[ptr])-ord('a')].append(ord(s2[ptr])-ord('a'))
                    indegree[ord(s2[ptr])-ord('a')]+=1
                    break
            
                
        topoSort = topoS()
        ans=""
        for i in topoSort:
            ans+=chr(i+97)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends