class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partion(L,R):
            pivot = nums[R]

            for j in range(L,R):
                if nums[j] <= pivot:
                    nums[j], nums[L] = nums[L], nums[j]
                    L +=1
                    
            nums[L], nums[R] = nums[R], nums[L]
            return L
            

        left, right= 0, len(nums)-1
        kth = len(nums)-k
        
        while left < right:
            idx = partion(left,right)    
            if idx == kth:
                break
                
            elif idx < len(nums)-k:
                left = idx+1
            else:
                right = idx-1
                
        return nums[kth]
            
            
            
            
        
        
        
        