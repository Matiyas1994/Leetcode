# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        p2 = headB
        L1 = set()
        while p1:
            L1.add(p1) 
            p1 = p1.next
            
        while p2:
            if p2 in L1:
                return p2
            p2 = p2.next