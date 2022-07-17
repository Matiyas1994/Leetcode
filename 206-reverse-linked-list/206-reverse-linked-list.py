# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        p1 = head
        p2 = p1.next
        head.next = None
        
        while p2 != None:
            temp = p2.next
            p2.next = p1
            p1 = p2
            p2 = temp
            
        return p1 
        
        
#         cur = head
#         stack =[]
        
#         while cur:
#             stack.append(cur)
#             cur = cur.next
#         # print(stack)
#         for i in range(len(stack)-1,0,-1):
#             stack[i].next = stack[i-1]
#         head.next = None
#         return stack[-1]
            
        
        
            