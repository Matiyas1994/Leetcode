"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return
        
        def createcopy(node):
            new = Node(node.val,node.next)
            node.next = new
    
        cur = head
        
        while cur:
            createcopy(cur)
            cur = cur.next.next
    
        
        cur = head
        new = head.next
       
       
        while cur and cur.next:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
            
        cur = head.next
        
        while cur.next:
            cur.next = cur.next.next
            cur = cur.next
        
        return new
        
        
            