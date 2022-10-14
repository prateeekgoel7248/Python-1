# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.ans = []
        self.func(root1)
        self.func(root2)
        return(sorted(self.ans))
    
    def func(self, root):
        
        if not root:
            return
        
        self.func(root.left)
        self.ans.append(root.val)
        self.func(root.right)