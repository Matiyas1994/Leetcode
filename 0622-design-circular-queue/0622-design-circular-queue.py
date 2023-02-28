class Node:
    def __init__(self, val, nxt=None, prev=None):
        self.val = val
        self.next = nxt
        self.prev = prev
        
class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.curCapacity = 0

    def enQueue(self, value: int) -> bool:
        if self.curCapacity >= self.capacity:
            return False
        newNode = Node(value)
        self.addToTail(newNode)
        self.curCapacity +=1
        return True

    def deQueue(self) -> bool:
        if self.curCapacity == 0:
            return False
        self.deleteNode(self.head.next)
        self.curCapacity -=1
        return True

    def Front(self) -> int:
        return self.head.next.val
        

    def Rear(self) -> int:
        return self.tail.prev.val
        

    def isEmpty(self) -> bool:
        return self.curCapacity==0
        

    def isFull(self) -> bool:
        return self.curCapacity==self.capacity
        
    def addToTail(self, node):
        temp = self.tail.prev
        temp.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = temp
    def deleteNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()