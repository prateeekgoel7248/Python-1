# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def addOneRow(self, root, val, depth):
        def solve(node,depth,flag):
            if depth==1:
                if flag:
                    node = TreeNode(val,node)
                else:
                    node = TreeNode(val,None,node)
                return node
            if not node:
                return None
            node.left = solve(node.left,depth-1,True)
            node.right = solve(node.right,depth-1,False)
            return node
        return solve(root,depth,True)