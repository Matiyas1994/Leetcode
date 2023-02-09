class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)        
        ans = right =  right2 = 0
        
        for i in range(len(nums)):
            while len(dic) != k and right2 < len(nums):
                dic[nums[right2]] += 1
                right2 += 1
            
            right = max(right, right2)
            while right < len(nums) and nums[right] in dic:
                right += 1
                
            if len(dic) == k:
                ans += right - right2 + 1
            dic[nums[i]] -= 1
            if dic[nums[i]] == 0:
                del dic[nums[i]]
        
        return ans
    
        