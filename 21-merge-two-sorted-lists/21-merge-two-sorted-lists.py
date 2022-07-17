# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val <= list2.val:
            temp = list1
            L1 = list1.next
            L2 = list2
            head = list1
        else:
            temp = list2
            L2 = list2.next
            L1 = list1
            head = list2
        
        while L1 and L2:
            if L1.val <= L2.val:
                temp.next = L1
                temp = L1
                L1 = L1.next
            else:
                temp.next = L2
                temp = L2
                L2 = L2.next
        if L1:
            temp.next = L1
        if L2:
            temp.next = L2
        
        return head
        
        