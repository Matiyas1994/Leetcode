class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        reqNumberOfSubsets = (2**k) 
        seen = set()
        for i in range(len(s)- k+1):
            curStr = s[i: i + k]
            if curStr not in seen:
                seen.add(curStr)
                reqNumberOfSubsets -=1
            if  reqNumberOfSubsets == 0:
                return True
        return False
        
        
        
        
        
#         _len = len(bin((2**k)-1)) - 2
#         _set = set()
        
#         for i in range(len(s)):
#             _set.add(s[i:i + _len])
        
#         for i in range(2**k):
#             b = bin(i) 
#             curLen = len(b) - 2
#             _str = "0" * (_len - curLen) + b[2:] 
#             if _str not in _set:
#                 return False
            
#         return True
        
        