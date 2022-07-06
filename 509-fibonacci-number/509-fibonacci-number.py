class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        
        prev = 0
        cur = 1
        
        for num in range(2,n+1):
            res = prev + cur
            prev = cur
            cur = res
            
        return res
        
        
        