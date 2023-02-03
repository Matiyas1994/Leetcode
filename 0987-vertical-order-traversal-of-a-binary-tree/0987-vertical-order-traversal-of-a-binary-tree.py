# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = defaultdict(list)
        
        def dfs(node, i, j):
            if not node:
                return
            
            dic[j].append((i,node.val))
            
            dfs(node.left, i+1, j-1)
            dfs(node.right, i+1, j +1)
    
        dfs(root, 0,0)
        
        ans = []
        for key in sorted(dic):
            temp = []
            for row, val in sorted(dic[key], key = lambda x: (x[0],x[1])):
                temp.append(val)  
            ans.append(temp)
           
        return ans
        