class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        lenPref = len(pref)
        ans = 0
        for w in words:
            if w[:lenPref]==pref:
                ans +=1
        
        return ans
            
        