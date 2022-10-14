#User function Template for python3

class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        # code here
        q=[0]
        res=[]
        visited=[False for _ in range(V)]
        while q:
            for _ in range(len(q)):
                val=q.pop(0)
                if not visited[val]:
                    res.append(val)
                    visited[val]=True
                    for ne in adj[val]:
                        q.append(ne)
        return res


#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends