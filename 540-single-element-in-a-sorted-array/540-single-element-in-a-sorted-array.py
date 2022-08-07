class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        def dif(mid):
            if mid%2:
                return nums[mid] != nums[mid-1]
            else:
                return mid == len(nums)-1 or nums[mid] != nums[mid+1]
        
        
        left, right = 0 , len(nums)-1
        ans = nums[-1]
        
        while left<= right:
            mid = left +(right-left)//2
            
            if dif(mid):
                ans = nums[mid]
                right = mid - 1
            else:
                left = mid + 1
        
        return ans 