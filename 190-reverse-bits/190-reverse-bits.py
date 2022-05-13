class Solution:
    def reverseBits(self, n: int) -> int:
        s = bin(n)
        s = s[::-1] 
        s = s[:-2] + "0"*(34-len(s))
        return int(s ,2)