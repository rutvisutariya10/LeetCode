        self.makeSet(root)

    def makeSet(self,root):
        if not root:
            return 
        self.vals.add(root.val)
        if root.left:
            root.left.val =   (2*root.val) + 1
            self.makeSet(root.left)
        if root.right:
            root.right.val = (2*root.val) + 2    
            self.makeSet(root.right)    

    def find(self, target: int) -> bool:
        if target in self.vals:
            return True
        return False
        

