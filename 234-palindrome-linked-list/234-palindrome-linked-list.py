# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(start):
            prev = None  
            while start:
                temp = start.next
                start.next = prev
                prev = start
                start = temp
            return prev
                
            
       
        dummy = fast = slow = ListNode()
        dummy.next = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
          
        
        new_start = None
        if fast==None:
            dummy = ListNode(slow.val, slow.next)
            slow.next = None
            new_start = reverse(dummy)
            
        else:
            new_start = reverse(slow.next)
            slow.next = None
        
        
        while new_start and head:
            if new_start.val != head.val: return False
            new_start = new_start.next
            head = head.next
        
        return True
                
        
     
        