# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def markParent(self,root,d):
        d[root]=None
        q=[root]
        while q:
            
            node = q.pop(0)
            if node.left:
                q.append(node.left)
                d[node.left] = node
            if node.right:
                q.append(node.right)
                d[node.right]=node   
        
    def distanceK(self, root, target, k):
        d=defaultdict(TreeNode)
        self.markParent(root,d)
        visited = defaultdict(bool)
        visited[target]=True
        q=[]
        q.append(target)
        level=0
        while q:
            s = len(q)
            if level==k:
                break
            level+=1
            
            for i in range(s):
                node=q.pop(0)
                if node.left and not visited[node.left]:
                    q.append(node.left)
                    # print("l",node.left.val)
                    visited[node.left]=True
                if node.right and not visited[node.right]:
                    # print("r",node.right.val)
                    q.append(node.right)
                    visited[node.right]=True
                if d[node] and not visited[d[node]]:
                    q.append(d[node])
                    # print(d[node].val)
                    visited[d[node]]=True
        res=[]
        for i in q:
            res.append(i.val)
        return res
                
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        