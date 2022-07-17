# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p_fast = head
        p_slow = head
        
        while True:
            if p_fast and p_fast.next:
                p_fast = p_fast.next.next
                p_slow = p_slow.next
            else:
                return 
            
            if p_fast == p_slow:
                p_fast = head    
                while p_fast != p_slow:
                    p_fast = p_fast.next
                    p_slow = p_slow.next

                return p_slow 


