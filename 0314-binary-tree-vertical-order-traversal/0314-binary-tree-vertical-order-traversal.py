# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return [] 
        answer = []
        queue = deque()
        queue.append((root, 0))
        columns = defaultdict(list)
        
        while queue:
            
            node, col = queue.popleft()
            
            if node:
                columns[col].append(node.val)
                
                queue.append((node.left,  col-1))
                queue.append((node.right, col+1))
        
        for col in sorted(columns):
            answer.append(columns[col])
                
        return answer
                
            
        
            
        
        