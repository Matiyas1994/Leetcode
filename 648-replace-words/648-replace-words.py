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
        
    def search(self, word: str, ds:list) -> bool:
        parent = self.root 
        for char in word:
            if char in parent.children:
                ds.append(char)
                if parent.children[char].isEnd:
                    return ds
                parent = parent.children[char]
            else:
                return []
            
        return []
            
            
#             if char not in parent.children:
#                 return False
#             parent = parent.children[char]
                
#         return parent.isEnd

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        objTrie = Trie()
        for rw in dictionary:
            objTrie.insert(rw)
        ans = []
        for w in sentence.split():
            res = objTrie.search(w,[])
            if res:
                ans.append("".join(res))
            else:
                ans.append(w)
    
        return " ".join(ans)
        
        
        
        
        
        
        