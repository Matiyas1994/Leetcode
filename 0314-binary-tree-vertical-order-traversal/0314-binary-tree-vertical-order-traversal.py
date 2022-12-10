# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        temp = []
        queue = deque()
        queue.append((0,0,root))
        
        while queue:
            arr = 0
            for _ in range(len(queue)):
                col, lev, node = queue.popleft()
                temp.append((col, lev, arr, node.val))
                
                if node.left:
                    queue.append((col-1, lev+1, node.left))
                if node.right:
                    queue.append((col+1, lev+1, node.right))
                
                arr +=1
        
        temp.sort()
        
        for i in range(len(temp)):
            if i != 0 and temp[i][0]==temp[i-1][0]:
                ans[-1].append(temp[i][3])
            else:
                ans.append([temp[i][3]])
                
        return ans
                
            
        
            
        
        