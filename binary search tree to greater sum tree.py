# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    su=0
    def bstToGst(self, root):
        if not root:
            return None
        self.bstToGst(root.right)
        root.val+=self.su
        self.su=root.val
        self.bstToGst(root.left)
        return root