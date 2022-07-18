# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        LenA = 0
        LenB = 0
        L1, L2 = headA, headB
        while L1:
            LenA +=1
            L1 = L1.next
        while L2:
            LenB +=1
            L2 = L2.next
        L1, L2 = headA, headB
        if LenA > LenB:
            for i in range(LenA-LenB):
                L1 = L1.next
        else:
            for i in range(LenB-LenA):
                L2 = L2.next
        while L1 and L2:
            if L1 == L2:
                return L1
            L1 = L1.next
            L2 = L2.next
            
        
        
        
        
        
        
        
        
        
#         visited = set()
#         L1 = headA
#         L2 = headB
#         while L1 or L2:
#             if L1 in visited: return L1
#             if L2 in visited: return L2
#             if L1:
#                 visited.add(L1)
#                 L1 = L1.next
#             if L2: 
#                 visited.add(L2)
#                 L2 = L2.next
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         p1 = headA
#         p2 = headB
#         c = 0
#         c2 = 0
#         while p1:
#             c += 1
#             p1 = p1.next
            
#         while p2:
#             c2 +=1
#             p2 = p2.next
#         p1 = headA
#         p2 = headB
        
#         if c <= c2:
#             for _ in range(c2-c):
#                 p2 = p2.next
#         else:
#             for _ in range(c-c2):
#                 p1 = p1.next
        
#         while p1 and p2:
#             if p1 == p2:
#                 return p1
#             p1 = p1.next
#             p2 = p2.next
            
            
        
            
        
        
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