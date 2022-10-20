# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def helper(node, robeble):
            if not node: return 0
            
            not_robe = helper(node.left, True) + helper(node.right, True)
            robeIt = 0
            if robeble:
                robeIt = helper(node.left, False) + helper(node.right, False) + node.val
                
            return max(not_robe, robeIt)
        
        return helper(root, True)
            
            