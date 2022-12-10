# class WebPages:
#     def __init__(self, name, prev=None, nxt=None):
#         self.name = name
#         self.prev =prev
#         self.next = nxt
        
class BrowserHistory:

    def __init__(self, homepage: str):
        self.browseHistory = [homepage]
        self.current_pos = 0
        self.bound = 0
        
    def visit(self, url: str) -> None:
        self.current_pos += 1
        
        if self.current_pos == len(self.browseHistory):
            self.browseHistory.append(url)
        else:
            self.browseHistory[self.current_pos] = url
        
        self.bound = self.current_pos
        

    def back(self, steps: int) -> str:
        self.current_pos = max(0, self.current_pos - steps)
        
        return self.browseHistory[self.current_pos]
        

    def forward(self, steps: int) -> str:
        self.current_pos = min(self.bound, self.current_pos + steps)
        
        return self.browseHistory[self.current_pos]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

