# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        Max = -1
        def rightSideView(root,depth):
            nonlocal Max
            if not root:
                Max = max(Max,depth-1)
                return
          
            if depth > Max:
                ans.append(root.val)
           
            rightSideView(root.right,depth+1)
            rightSideView(root.left,depth+1)
        
        rightSideView(root,0)
        return ans