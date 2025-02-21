            return 
        self.makeSet(root.left, (2*currVal) + 1)

        self.vals.add(currVal)
    def find(self, target: int) -> bool:
        if target in self.vals:
            return True
        return False
        self.makeSet(root.right, (2*currVal) + 2)   
        if not root:
    def makeSet(self,root,currVal):

        self.makeSet(root,0)
        self.vals = set()
        self.tree = root
    def __init__(self, root: Optional[TreeNode]):
        


# Your FindElements object will be instantiated and called as such:
