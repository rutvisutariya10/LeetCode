        for i,ele in enumerate(preorder):
            preIndex[ele] = i
            tmap[ele] = TreeNode(ele)
        postIndex = {}
        for i,ele in enumerate(postorder):
            postIndex[ele] = i
        pre = 0
        while pre < N:
            po = postIndex[preorder[pre]]
            # Left Child 
            if pre + 1 < N and postIndex[preorder[pre+1]] < postIndex[preorder[pre]]:
                tmap[preorder[pre]].left = tmap[preorder[pre+1]]
            # Right Child
            if po - 1 > -1 and preIndex[postorder[po]] < preIndex[postorder[po-1]] and tmap[preorder[pre]].left != tmap[postorder[po-1]]:
            
                tmap[postorder[po]].right = tmap[postorder[po-1]]
            pre += 1
        return tmap[preorder[0]]
        
