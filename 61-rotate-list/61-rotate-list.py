# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return
        numOfNodes = 0
        cur = head 
        while cur and cur.next:
            numOfNodes +=1
            cur = cur.next
        cur.next = head
        for i in range(numOfNodes+1 - k%(numOfNodes+1)): cur = cur.next
        new = cur.next
        cur.next = None
        
        return new
            
            
            
        