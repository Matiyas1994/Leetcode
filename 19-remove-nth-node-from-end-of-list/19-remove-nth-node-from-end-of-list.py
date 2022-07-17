# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         cur_node = head
#         while n:
#             cur_node = cur_node.next
#             n -=1
#         if not cur_node or not cur_node.next:
#             return cur_node
        
#         change = head
        
#         while cur_node.next:
#             cur_node = cur_node.next
#             change = change.next
        
#         change.next = change.next.next
        
#         return head
        
        
        
        
        
        if not head or not head.next: return
        count = 0
        cur_node = head
        while cur_node:
            count +=1
            cur_node = cur_node.next
        if count==n:
            return head.next
        startOver = 0
        cur_node = head
        while startOver < count-n-1:
            startOver +=1
            cur_node = cur_node.next
   
        cur_node.next = cur_node.next.next
        
        return head
        