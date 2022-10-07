# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def go(node):
            if not node:
                return 0
            
            left = go(node.left)
            right = go(node.right)
            
            return max(left, right)+1
        
        return go(root)
            
            
        
        
        
        
#         #return int(/2)
#         if not root:
#             return 0
#         return self.find_depth(root, 0)
        
#     def find_depth(self, root, depth_counter):
    
#         if not root:
#             return
#         depth_counter += 1
            
#         if not root.left and not root.right:
#             return depth_counter
                
            
#         left = self.find_depth(root.left, depth_counter)
#         right = self.find_depth(root.right, depth_counter)
        
#         if not left:
#             return right
#         if not right:
#             return left
#         return max(left, right)