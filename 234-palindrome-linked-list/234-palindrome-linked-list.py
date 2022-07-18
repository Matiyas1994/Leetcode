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
       
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
          
        if fast:
            slow = slow.next
        
        slow = reverse(slow)
        while slow:
            if slow.val != head.val: return False
            slow = slow.next
            head = head.next
        
        return True
                
        
     
        