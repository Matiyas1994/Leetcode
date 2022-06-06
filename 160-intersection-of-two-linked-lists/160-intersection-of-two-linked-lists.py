# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        p2 = headB
        c = 0
        c2 = 0
        while p1:
            c += 1
            p1 = p1.next
            
        while p2:
            c2 +=1
            p2 = p2.next
        p1 = headA
        p2 = headB
        
        if c <= c2:
            for _ in range(c2-c):
                p2 = p2.next
        else:
            for _ in range(c-c2):
                p1 = p1.next
        
        while p1 and p2:
            if p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next
            
            
        
            
        
        
#         p1 = headA
#         p2 = headB
#         L1 = set()
#         while p1:
#             L1.add(p1) 
#             p1 = p1.next
            
#         while p2:
#             if p2 in L1:
#                 return p2
#             p2 = p2.next