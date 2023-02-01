# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        def reverseLinkedList(beforeLeft, left, count):
            prev = beforeLeft
            cur = left
            
            while count:
                nextt = cur.next
                cur.next = prev
                prev = cur
                cur = nextt
                count -=1
        
            left.next = cur
            if beforeLeft:
                beforeLeft.next = prev
            else: 
                return prev
        ans = None
        cur = head
        lleft = 1
        while lleft+1 < left:
            cur = cur.next
            lleft +=1
        if left != 1:
            ans = reverseLinkedList(cur, cur.next, right - left+1)
        else:
            ans = reverseLinkedList(None, cur, right-left+1)
        
        return head if not ans else ans
            
            
        