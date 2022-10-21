# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack  = []
        res = []
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            res.append(node.val)
            root = node.right
        
        return res
#         ans = []
#         def trav(r):
#             if r == None:
#                 return
            
#             trav(r.left)
#             ans.append(r.val)
#             trav(r.right)
                
#         trav(root)
#         return ans
        