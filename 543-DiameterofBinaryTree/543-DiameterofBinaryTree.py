    /\
     B
   C  D
  /    \ 
 E      F
/        \
G         I
'''
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return [-1,-1]
            l, r = dfs(root.left), dfs(root.right)
            height =  max(l[0],r[0]) + 1
            return [height,max(l[1],r[1],l[0] + r[0] + 2)]
        return max(dfs(root))
        
