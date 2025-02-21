        if not root:
            return 
        self.vals.add(root.val)
        if root.left:
            root.left.val =   (2*root.val) + 1
            self.makeSet(root.left)
    def makeSet(self,root):

        self.makeSet(root)
        self.vals = set()
        self.tree = root
        root.val = 0 if root else None

    def __init__(self, root: Optional[TreeNode]):
#         self.right = right
class FindElements:
#         self.left = left
#         self.val = val
#     def __init__(self, val=0, left=None, right=None):
