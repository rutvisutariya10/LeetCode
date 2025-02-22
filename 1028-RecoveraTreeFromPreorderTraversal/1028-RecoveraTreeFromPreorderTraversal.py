            # tree done when nodes empty. if expected depth != current depth then reached leaf
        def makeTree(depth): 

    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        # make tuples of (depth, value) for each node in tree. reverse to pop starting from root
        nodes = [(len(node[1]), int(node[2])) for node in re.findall("((-*)(\d+))", traversal)][::-1]

'''
class Solution:

    90


    /
            if not nodes or depth != nodes[-1][0]: return None 

