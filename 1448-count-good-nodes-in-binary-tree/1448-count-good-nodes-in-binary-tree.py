# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def trav(node, _max):
            if not node:
                return 0
            good = False
            if _max <= node.val:
                good = True
            
            _max = max(_max, node.val)
            
            l = trav(node.left, _max)
            r = trav(node.right, _max)
            
            return l+r+1 if good else l+r
        
        return trav(root,root.val)
            
            
        