# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):
    def __init__(self, root):
        self.res = []
        p = root
        stack = []
        while p or stack:
            if p:
                stack.append(p)
                p = p.left
            else:
                s = stack.pop()
                self.res.append(s.val)
                p = s.right
        self.n = len(self.res)
        self.i = 0      
    def next(self):
        c = self.res[self.i]
        self.i+=1
        return c
    def hasNext(self):
        return self.i<self.n
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()