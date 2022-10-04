class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count, ans = 0, 0
        prefix = {0:1}
        n = len(nums)
        
        for i in range(n):
            if nums[i]%2:
                count +=1
            
            if count - k in prefix:
                ans += prefix[count - k]
            
            prefix[count] = prefix.get(count, 0) + 1
            
        
        return ans
        
        