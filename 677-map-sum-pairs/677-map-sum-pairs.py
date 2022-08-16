class trinode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.value = 0
  
class Trie:
    def __init__(self):
        self.root = trinode()

    def insert(self, word: str, val) -> None:
        parent  = self.root
        for char in word:
            if char not in parent.children:
                parent.children[char] = trinode()
            parent = parent.children[char]

        parent.isEnd = True
        parent.value = val
        
    def startsWith(self, prefix: str):
        parent = self.root 
        for char in prefix:
            if char not in parent.children:
                return 
            parent = parent.children[char]   
        return parent


class MapSum:

    def __init__(self):
        self.obj = Trie()
        

    def insert(self, key: str, val: int) -> None:
        self.obj.insert(key, val)
        

    def sum(self, prefix: str) -> int:
        start = self.obj.startsWith(prefix)
        
        def dfs(node):
            if not node:
                return 0
            s = 0
            for child in node.children:
                s += dfs(node.children[child])
                
            return s +  node.value
        
        return dfs(start)
            
        
        
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)