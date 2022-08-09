class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def helper(guss):
            res = 0
            for num in nums:
                res +=math.ceil(num/guss)
            
            return res<=threshold 
             
        low, high = 1, max(nums)  
        ans = high
        
        while low<=high:
            mid = low + (high-low)//2
            
            if helper(mid):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def answergiver(n):
#             nonlocal threshold
#             s = 0
#             for i in nums:
#                 s +=ceil(i/n)
                
#             if s <= threshold:
#                 return True
#             return False
        
        
#         saved  = float(inf)
#         left = 1
#         right = max(nums)
        
#         while left <= right:
            
#             mid  = (right + left)//2
            
#             if answergiver(mid):
#                 saved = min(saved,mid)
#                 right = mid -1
#             else:
#                 left = mid + 1
        
#         return saved
        