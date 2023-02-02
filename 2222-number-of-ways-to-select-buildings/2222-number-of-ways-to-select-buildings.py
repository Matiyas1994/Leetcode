class Solution:
    def numberOfWays(self, s: str) -> int:
        zeroes, ones = 0, 0
        counts01, counts10 = 0, 0
        counts010, counts101 = 0, 0
        for val in s:
            if val == '0':
                zeroes += 1
                counts10 += ones
                counts010 += counts01         
            else:
                ones += 1
                counts01 += zeroes
                counts101 += counts10
        
        return counts010 + counts101
    