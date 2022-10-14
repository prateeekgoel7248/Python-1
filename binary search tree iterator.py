class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.node = root
        self.stack = []
        
    def _traverse(self):
        while self.node:
            self.stack.append(self.node)
            self.node = self.node.left
        
    def next(self) -> int:
        self._traverse()
        node = self.stack.pop()
        self.node = node.right
        return node.val
        
    def hasNext(self) -> bool:
        return self.stack or self.node