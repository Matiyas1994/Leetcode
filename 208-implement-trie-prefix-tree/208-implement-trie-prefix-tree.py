class trinode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
  
class Trie:
    def __init__(self):
        self.root = trinode()
        
    def insert(self, word: str) -> None:
        parent  = self.root
        for char in word:
            if char not in parent.children:
                parent.children[char] = trinode()
            parent = parent.children[char]
            
        parent.isEnd = True   

    def search(self, word: str) -> bool:
        parent = self.root 
        for char in word:
            if char not in parent.children:
                return False
            parent = parent.children[char]
                
        return parent.isEnd

    def startsWith(self, prefix: str) -> bool:
        parent = self.root 
        for char in prefix:
            if char not in parent.children:
                return False
            parent = parent.children[char]   
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)