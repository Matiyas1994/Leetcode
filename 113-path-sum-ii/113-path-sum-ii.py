# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def go(node, target, ds):            
            if not node: return
            if not node.right and not node.left and target==node.val:
                ds.append(node.val)
                ans.append(ds[::])
                ds.pop()
                return
            
            ds.append(node.val)
            go(node.left,target-node.val, ds)
            go(node.right, target-node.val, ds)
            ds.pop()
            
        go(root, targetSum, [])
        return ans
            
            
            
                
        