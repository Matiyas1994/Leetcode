class Solution:
    def numSplits(self, s: str) -> int:
        n = len(s)
        prefix1 = []
        prefix2 = [0]*n
        
        se = set() 
        for i in range(n):
            se.add(s[i])
            prefix1.append(len(se))
        se = set()
        for j in range(n-1,-1,-1):
            se.add(s[j])
            prefix2[j] = len(se)
        
        ans = 0
        for i in range(n-1):
            if prefix1[i] == prefix2[i+1]:
                ans +=1
                
        return ans