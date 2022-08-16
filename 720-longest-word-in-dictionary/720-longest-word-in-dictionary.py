class trinode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
  
class Trie:
    def __init__(self):
        self.root = trinode()
        self.root.isEnd = True

    def insert(self, word: str) -> None:
        parent  = self.root
        for char in word:
            if char not in parent.children:
                parent.children[char] = trinode()
            parent = parent.children[char]

        parent.isEnd = True   


class Solution:
    def longestWord(self, words: List[str]) -> str:
        objTrie = Trie()
        
        for word in words:
            objTrie.insert(word)
            
        ans = []
        def dfs(root, ds:list):
            nonlocal ans
            if not root.isEnd:
                return
            
            for child in root.children:
                if root.children[child].isEnd:
                    ds.append(child)
                    dfs(root.children[child],ds)
                    ds.pop()
                    
                    
            if len(ds) > len(ans):
                ans = ds[:]
            elif len(ds) == len(ans):
                if ds < ans:
                    ans = ds[:]
            
                
            
        dfs(objTrie.root, [])
        return "".join(ans)
        