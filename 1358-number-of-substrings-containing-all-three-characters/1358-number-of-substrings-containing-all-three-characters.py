class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l, ans, n = 0, 0, len(s)
        dic = {}
        
        for r in range(n): 
            dic[s[r]] = dic.get(s[r], 0) + 1
            
            while len(dic) >=3 and dic[s[l]] - 1 > 0:
                dic[s[l]] -=1
                l +=1
            
            if len(dic)==3:
                ans +=l+1
        
        return ans
        