class MyStack:

    def __init__(self):
        self.que = deque()
        
        

    def push(self, x: int) -> None:
        self.que.append(x)
        for _ in range(len(self.que)-1):
            self.que.append(self.que.popleft())
        

    def pop(self) -> int:
        return self.que.popleft()
    
    

    def top(self) -> int:
        return self.que[0]

    def empty(self) -> bool:
        return not self.que
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()