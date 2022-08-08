# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        posiblePositionsToStart = []
        
        def findPosibleStartPositions(node):
            if node:
                if node.val == head.val:
                    posiblePositionsToStart.append(node)
                
                findPosibleStartPositions(node.left)
                findPosibleStartPositions(node.right)
        
        def linkedlistInTree(linkedList, node):
            if not linkedList: return True
            if not node: return False
            
            if node.val != linkedList.val:
                return False
            
            L = linkedlistInTree(linkedList.next, node.left)
            R = linkedlistInTree(linkedList.next, node.right)
            
            return L or R
        
        
        findPosibleStartPositions(root)
        # print(posiblePositionsToStart)
        for startNodes in posiblePositionsToStart:
            if linkedlistInTree(head, startNodes): return True
        
        return False
            
            
              