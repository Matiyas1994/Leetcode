# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        prev = dummy = ListNode()
        while l1 and l2:
            summ= carry + l1.val + l2.val
            if summ > 9:
                summ = summ%10
                carry = 1
            else:
                carry = 0
            new_node = ListNode(summ)
            prev.next = new_node
            prev = new_node
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            summ= carry + l1.val 
            if summ > 9:
                summ = summ%10
                carry = 1
            else:
                carry = 0
            new_node = ListNode(summ)
            prev.next = new_node
            prev = new_node
            l1 = l1.next
        while l2:
            summ= carry  + l2.val
            if summ > 9:
                summ = summ%10
                carry = 1
            else:
                carry = 0
            new_node = ListNode(summ)
            prev.next = new_node
            prev = new_node
            l2 = l2.next
        if carry:
            new_node = ListNode(carry)
            prev.next = new_node
        
        return dummy.next
            
        