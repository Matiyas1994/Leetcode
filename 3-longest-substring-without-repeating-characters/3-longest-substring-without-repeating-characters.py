class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return n
        p1 = 0
        p2 = 0
        Max = float("-inf")
        
        
        while p2 < n:
            visited = set()
            while p2 < n and s[p2] not in visited:
                visited.add(s[p2])
                p2 +=1
                
                
            Max = max(Max,p2-p1)
            p1 +=1
            p2 = p1
        
        return Max