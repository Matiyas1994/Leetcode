class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self.isq1 = True
        

    def push(self, x: int) -> None:
        if self.isq1:
            while self.q1:
                self.q2.append(self.q1.popleft())
            self.q1.append(x)
            self.isq1 = False
        else:
            while self.q2:
                self.q1.append(self.q2.popleft())
            self.q2.append(x)
            self.isq1 = True
            

    def pop(self) -> int:
        if not self.isq1:
            x = self.q1.popleft()
            if self.q2:
                self.q1.append(self.q2.popleft())
        else:
            x = self.q2.popleft()
            if self.q1:
                self.q2.append(self.q1.popleft())

        return x
    

    def top(self) -> int:
        # print(self.q1, self.q2, self.isq1)
        if not self.isq1:
            return self.q1[0]
        else:
            return self.q2[0]
        

    def empty(self) -> bool:
        return not self.q1 and not self.q2
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()