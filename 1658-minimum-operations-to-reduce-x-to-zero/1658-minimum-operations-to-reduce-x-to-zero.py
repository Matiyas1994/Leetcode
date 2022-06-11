class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        target = sum(nums) - x
        ans = 0
        l, s = 0, 0
        found = False
        
        for r in range(n):
            s +=nums[r]
            while s > target and l <=r:
                s -= nums[l]
                l +=1
            if s == target:
                found = True
                ans = max(ans,(r-l+1))
                
        return n - ans if found else -1 
        
        
