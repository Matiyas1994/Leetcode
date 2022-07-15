class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        constant = [0 for _ in range((5*10**5)+1)]
        constant[0]=1
        for num in nums:
            if num > 0 and num < (5*10**5)+1:
                constant[num] = 1
        for i,val in enumerate(constant):
            if val==0:
                return i
            
        return 500001
