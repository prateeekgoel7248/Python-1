# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self,root):
        if not root:
            return 0
        l = self.dfs(root.left)
        if l==-1:
            return -1
        r = self.dfs(root.right)
        if r==-1:
            return -1
        if abs(l-r)>1:
            return -1
        return max(l,r)+1
    def isBalanced(self, root):
        return self.dfs(root)!=-1