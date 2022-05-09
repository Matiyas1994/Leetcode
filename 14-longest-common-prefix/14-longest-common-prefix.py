class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        myref = strs[0]
        
        for i, char in enumerate(myref):
            for j in range(1,len(strs)):
                if i >= len(strs[j]) or char != strs[j][i]:
                    return myref[:i]        
        
        
        return myref
        