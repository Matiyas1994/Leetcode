class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastOcurrance = {}
        Max = 0
        lastInturupt = -1
        
        for i, val in enumerate(s):
            if val in lastOcurrance:
                lastInturupt = max(lastInturupt, lastOcurrance[val])
            
            Max = max(Max, i-lastInturupt)
            lastOcurrance[val] = i
        
            
        return Max 
        