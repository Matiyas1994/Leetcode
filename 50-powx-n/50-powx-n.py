class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x,n):
            if n==0:
                return 1
            temp=power(x,n//2)
            if n%2==1:
                return x*temp*temp
            return temp*temp
    
        return power(x,n) if n >=0 else 1/power(x,-1*n)