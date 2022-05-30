class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = 0
        sign = False
        if (dividend < 0 and divisor > 0 ) or (dividend > 0 and divisor < 0):
             sign = True
       
        dividend , divisor = abs(dividend), abs(divisor)
           
        
        while dividend - divisor >= 0:
            count  = 0
            while dividend - (divisor <<1<< count) >=0:
                count +=1
            dividend -= divisor<<(count)
            ans +=1<<count
        
        if sign:
            ans *=-1
        if ans > 2147483647:
            return 2147483647
        elif ans < -2147483648:
            return -2147483648
        
        return ans
        