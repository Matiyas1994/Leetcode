class Node:
    def __init__(self, s="", val=0, nxt=None, prev=None):
        self.str = s
        self.val = val
        self.next = nxt
        self.prev = prev
        
class AllOne:
    def __init__(self):
        self.head = Node("",float("inf"),)
        self.tail = Node("",float("-inf"))
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dic = {}
        
    def inc(self, key: str) -> None:
        if key not in self.dic:
            newNode = Node(key, 1)
            self.createAtTail(newNode, self.tail)
            self.dic[key] = newNode
        else:
            node = self.dic[key]
            node.val +=1
            while node.val > node.prev.val:
                self.swap(node.prev, node)
                
    def dec(self, key: str) -> None:
        node = self.dic[key]
        node.val -=1
        if node.val == 0:
            self.deleteNode(node)
            del self.dic[key]
        elif node.val < node.next.val:
            self.swap(node, node.next)
                        
    def getMaxKey(self) -> str:
        return self.head.next.str

    def getMinKey(self) -> str:
        return self.tail.prev.str
    
    def createAtTail(self,newNode, tail):
        tail.prev.next = newNode
        newNode.next = tail
        newNode.prev = tail.prev
        tail.prev = newNode
    def createAtHead(self, newNode, head):
        newNode.next = head.next
        newNode.next.prev = newNode
        newNode.prev = head
        head.next = newNode
    def deleteNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def swap(self, node1, node2):
        node1.prev.next = node2
        node2.next.prev = node1
        node2.prev = node1.prev
        node1.prev = node2
        node1.next = node2.next
        node2.next = node1
    
    

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()