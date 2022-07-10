class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
            }
        ans = 0
        
        for i in range(1,len(s)):
            if dic[s[i-1]] < dic[s[i]]:
                ans -=dic[s[i-1]]
            else:
                ans +=dic[s[i-1]]
        ans += dic[s[-1]]
        return ans
        