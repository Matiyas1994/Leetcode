class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        lastPosition = -1
        t, j= 1, 0
        for i in range(len(nums)):
            if nums[i]==0 and t > 0:
                t -=1  
                lastPostion = i
            elif nums[i]==0:
                j = lastPostion+1
                lastPostion = i
            ans = max(i-j, ans)

        return ans
