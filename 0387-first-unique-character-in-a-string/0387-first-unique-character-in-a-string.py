class Solution:
    def firstUniqChar(self, s: str) -> int:
        occurance = Counter(s)
        for i in range(len(s)):
            if occurance[s[i]]==1:
                return i
        return -1
        