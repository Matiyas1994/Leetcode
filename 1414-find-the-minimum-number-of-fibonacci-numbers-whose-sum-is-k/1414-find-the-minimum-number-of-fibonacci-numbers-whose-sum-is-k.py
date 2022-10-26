class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib = [1,1]
        
        while fib[-1] + fib[-2] <= k:
            fib.append(fib[-1] + fib[-2])
        j = len(fib)-1
        steps = 0
        while k:
            while k//fib[j]:
                steps += k//fib[j]
                k %=fib[j]
            j -=1
        return steps
            
        