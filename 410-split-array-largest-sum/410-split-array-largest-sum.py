class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def helper(guess,m):
            numOfParts, cur_sum=0, 0
            
            for i in range(len(nums)):
                cur_sum += nums[i]
                if cur_sum > guess:
                    numOfParts +=1
                    cur_sum = nums[i]
                if numOfParts > m: return False
                
            if cur_sum > 0:  numOfParts +=1   
            return numOfParts <= m
        
        left, right = max(nums), sum(nums)
        ans = right
        while left<= right:
            mid= left + (right-left)//2
            
            if helper(mid, m):
                ans = mid
                right = mid-1
            else:
                left = mid+1
        
        return ans
        
        
        
        
            