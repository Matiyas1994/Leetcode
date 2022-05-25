class Solution:
    def reverse(self, x: int) -> int:
        li = []
        n = abs(x) 
        while(n):
            li.append(n%10)
            n //=10
        ti = len(li) - 1
        
        ans = 0
        for d in li:
            ans += d * (10**ti)
            ti -=1
        if ans > 2147483648:
            return 0
        
        if x < 0:
            return -1* ans
        return ans