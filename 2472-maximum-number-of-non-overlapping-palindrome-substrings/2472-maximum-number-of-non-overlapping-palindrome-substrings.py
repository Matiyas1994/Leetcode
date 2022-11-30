class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        def checkpalndrome(start, end):
            if end > len(s):
                return False
            temp = s[start:end]
            if temp == temp[::-1]:
                return True
            return False
        memo = {}
        def recursive(i):
            if i + k > len(s):
                return 0
            if i not in memo:
                count = recursive(i + 1)
                if checkpalndrome(i, i + k):
                    count = max(count,  1 + recursive( i + k))
                if checkpalndrome(i , i + k + 1):
                    count = max(count, 1 + recursive(i + k + 1))
                memo[i] = count
            return memo[i]
        
        return recursive(0)

        