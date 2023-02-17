# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        ans = []
        
        def dfs(node):
            nonlocal ans
            if not node:
                return 
       
            
            if node.left: dfs(node.left)
            ans.append(node.val)
            if node.right: dfs(node.right)
        dfs(root)
        res = float(inf)
        for i in range(len(ans)-1):
            res = min(res, (ans[i+1]-ans[i]))
        return res
            
        