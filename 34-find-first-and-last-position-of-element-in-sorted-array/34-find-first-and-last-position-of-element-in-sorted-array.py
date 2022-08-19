class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bs(flag):
            L, R =0, len(nums)-1
            
            ans =-1
            
            while L<=R:
                mid = L + (R-L)//2
                
                if nums[mid]==target:
                    ans = mid
                    if flag:
                        R = mid-1
                    else:
                        L = mid+1
                elif nums[mid] > target:
                    R = mid-1
                else:
                    L = mid+1
                    
            return ans
    
        return [bs(True), bs(False)]
        
                
            
            
            
            
            
                    
            
            