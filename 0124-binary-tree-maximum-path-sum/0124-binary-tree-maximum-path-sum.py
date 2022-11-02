# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float(-inf)
        def go(node):
            nonlocal ans
            if not node:
                return 0
            
            l = go(node.left)
            r = go(node.right)
            cur = l + r + node.val
            ans = max(ans, cur , l+node.val , r+node.val, node.val)
            
            return max(l+node.val, r+node.val, node.val)
        go(root)
        return ans
        