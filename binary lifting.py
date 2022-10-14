class TreeAncestor:
    
    def __init__(self, n: int, parent: List[int]):
        self.mx = int(log2(n))+1
        self.table = [[-1 for _ in range(n)] for i in range(self.mx)]
        for i in range(n):
            self.table[0][i]=parent[i]
        for i in range(1,self.mx):
            for j in range(n):
                if self.table[i-1][j]!=-1:
                    self.table[i][j]=self.table[i-1][self.table[i-1][j]]

    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(self.mx+1):
            mask = 1<<i
            if mask&k:
                node=self.table[i][node]
                if node==-1:
                    break
        return node


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)