class Solution:
    def findComplement(self, num: int) -> int:
        stack = []
        while num:
            if num&1:
                stack.append("0")
            else:
                stack.append("1")
            num = num>>1
        return int("".join(stack[::-1]), 2)
        