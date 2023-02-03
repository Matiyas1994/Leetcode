class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left <= right:
            if s[left] != s[right]:
                    new_s1 = s[:left]+s[left+1:]
                    new_s2 = s[:right]+s[right+1:]
                    return new_s1==new_s1[::-1] or new_s2==new_s2[::-1]
            left +=1
            right -=1
            
        return True
        
        
        
