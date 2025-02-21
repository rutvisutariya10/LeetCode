#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        i need depth of each node
        then i can check possible or not
        '''
        def dfs(root):
            if not root:
                return [True,-1]
            l, r = dfs(root.left), dfs(root.right)
            x = l[0] and r[0] and abs(l[1]-r[1]) <= 1
            return [x,1+max(l[1],r[1])]

        return dfs(root)[0]
        
