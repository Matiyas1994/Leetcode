class DLL:
    def __init__(self, key=0, val=0, nxt=None, prev=None):
        self.key = key
        self.val = val
        self.next = nxt
        self.prev = prev
    
class LRUCache:

    def __init__(self, capacity: int):
        self.numToLinkedList = {}
        self.capacity = capacity
        self.Head = DLL()
        self.Tail = DLL(0, 0, None, self.Head)
        self.Head.next = self.Tail
        

    def get(self, key: int) -> int:
        # print(self.numToLinkedList)
        if key in self.numToLinkedList:
            node = self.numToLinkedList[key]
            # newNode = DLL(node.key, node.val)
            self.deleteNode(node)
            self.addInTheFront(node)
            
            return node.val
            
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.numToLinkedList:
            node = self.numToLinkedList[key]
            node.val = value
            self.deleteNode(node)
            self.addInTheFront(node)
        else:
            newNode = DLL(key, value)
            if len(self.numToLinkedList) >= self.capacity:
                deletedNode = self.Tail.prev
                self.deleteNode(deletedNode)
                del self.numToLinkedList[deletedNode.key]
            self.numToLinkedList[key] = newNode
            self.addInTheFront(newNode)

        # print(self.numToLinkedList)
    def addInTheFront(self, node):
        node.next = self.Head.next
        node.prev = self.Head
        self.Head.next = node
        node.next.prev = node
    
    def deleteNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

