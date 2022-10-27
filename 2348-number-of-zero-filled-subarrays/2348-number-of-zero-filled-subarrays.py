class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        l, ans = 0, 0
        n = len(nums)
        for r in range(n):
            if nums[r]:
                l = r + 1
            ans += r-l+1
        return ans
                
        
        
        