class Solution:
    def maxProduct(self, words: List[str]) -> int:
        res = 0
        dictionary = { chr(97 + i) : 1<<i for i in range(26)}        
        binaryEquvalent = []
        
        
        def BEBuilder(word):
            binary = 0
            for let in word:
                binary |= dictionary[let]
            binaryEquvalent.append(binary)
            
        for word in words:
            BEBuilder(word)
     
    
        for i in range(len(words)-1):
            for j in range(i + 1, len(words)):
                if  binaryEquvalent[i] &  binaryEquvalent[j]:
                    continue
                res = max(res, (len(words[i]) * len(words[j]))) 
        
        return res
        
        