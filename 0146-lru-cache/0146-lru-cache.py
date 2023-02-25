class Node:
    def __init__(self, key, val, nxt=None, prev = None):
        self.key = key
        self.val = val
        self.next = nxt
        self.prev = prev
        

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        
        self.head.next = self.tail
        self.tail.prev = self.head
        
        

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        
        node = self.dic[key]
        result = node.val
        self.deleteNode(node)
        self.addNextToHead(node)
        
        return result
        

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            self.deleteNode(node)
            self.addNextToHead(node)
            node.val = value
        else:
            if len(self.dic) >= self.capacity:
                delNode = self.tail.prev
                self.deleteNode(delNode)
                del self.dic[delNode.key]
            
            newNode = Node(key, value)
            self.addNextToHead(newNode)
            self.dic[key] = newNode
            
        
        
    
    def addNextToHead(self,node):
        temp = self.head.next
        self.head.next = node
        node.next = temp
        
        temp.prev = node
        node.prev = self.head
        
    
    def deleteNode(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

