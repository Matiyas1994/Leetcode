class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
            "IV":4,
            "IX":9,
            "XL":40,
            "XC":90,
            "CD":400,
            "CM":900
            }
        if s in dic:
            return dic[s]
        ans = 0
        jump = False
        for i,ch in enumerate(s):
            if jump:
                jump = False
                continue
            if i != len(s)-1:
                if s[i:i+2] in dic:
                    ans +=dic[s[i:i+2]]
                    jump = True
                    continue
                
            ans +=dic[ch]
                    
        return ans
        