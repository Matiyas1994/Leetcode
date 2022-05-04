class TrieNode:
    def __init__(self):
        self.children= {}
        self.isEnd = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        parent = self.root
        
        for char in word:
            if char not in parent.children:
                parent.children[char] = TrieNode()
            parent = parent.children[char]
            
        parent.isEnd = True
    
    def search(self, word: str) -> bool:
        
        def dfs(i,cur):
            if i == len(word):
                if cur.isEnd:
                    return True
                return False
            if word[i] in cur.children:
                if dfs(i+1,cur.children[word[i]]):
                    return True
            elif word[i] == ".":
                for child in cur.children:
                    if dfs(i+1,cur.children[child]):
                        return True 
            
            return False
            
            
        return dfs(0,self.root)
   
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)