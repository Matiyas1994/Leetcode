class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        left = -1
        minIdx = maxIdx = -1
        ans = 0

        for i in range(len(nums)):
            if nums[i] < minK or nums[i]> maxK:
                left = i
            if nums[i]==minK:
                minIdx = i
            if nums[i]==maxK:
                maxIdx = i
            
            ans += max(0 ,min(minIdx, maxIdx) - left)
            
        return ans
    
       