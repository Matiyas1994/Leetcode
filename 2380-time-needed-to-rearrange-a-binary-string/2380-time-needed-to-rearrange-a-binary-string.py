class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        ans = 0
        s = list(s)
        while True:
            i = 0
            zeroOneExist = False
            while i < len(s)-1:
                if s[i]=='0' and s[i+1]=='1':
                    s[i],s[i+1] = s[i+1], s[i]
                    i+=1
                    zeroOneExist = True
                i +=1
            if not zeroOneExist:
                break
            ans  +=1
        return ans
        zeroOneExist = False
        
        