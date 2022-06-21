class Solution:
    def isPalindrome(self, x: int) -> bool:
        number = []
        if x < 0:
            return False
        
        while x > 0:
            number.append(x%10)
            x //=10
 
        return number==number[::-1]
        