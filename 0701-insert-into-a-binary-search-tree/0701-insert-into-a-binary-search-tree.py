# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            return TreeNode(val)
        
        def insert(node, val):
            if not node: return
            
            if node.val < val:
                if not node.right:
                    newNode = TreeNode(val)
                    node.right = newNode
                    return 
                
                insert(node.right, val)
            
            else:
                if not node.left:
                    newNode = TreeNode(val)
                    node.left = newNode
                    return 
                
                insert(node.left, val)
                
        insert(root, val)
        return root