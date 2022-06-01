class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1] 
            
        Lans = -1
        L = 0
        R = len(nums) - 1
        
        while L<=R:
            mid = L + (R-L)//2
            
            if nums[mid] == target:
                Lans = mid
                R = mid -1
            elif nums[mid] > target:
                R = mid - 1
            else:
                L = mid + 1
        
        if Lans == - 1:
            return [-1,-1]
         
        L = Lans
        R = len(nums) - 1
        Rans = Lans
        while L<=R:
            mid = L + (R-L)//2
            
            if nums[mid] == target: 
                Rans = mid 
                L = mid + 1
            elif nums[mid] > target:
                R = mid - 1
        
        return [Lans,Rans]
                
                
        
        