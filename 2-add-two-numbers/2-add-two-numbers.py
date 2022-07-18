# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        prev = dummy = ListNode()
        while l1 or l2 or carry:
            if l1: carry += l1.val
            if l2: carry += l2.val
                
            new_node = ListNode(carry%10)
            carry //=10
            prev.next = new_node
            prev = new_node
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
                
        return dummy.next
            
        