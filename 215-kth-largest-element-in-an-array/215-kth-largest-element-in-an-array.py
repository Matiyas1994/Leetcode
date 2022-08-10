class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def partion(L,R,pivot):
            while R < pivot:
                if nums[R] < nums[pivot]:
                    nums[R], nums[L] = nums[L], nums[R]
                    L +=1
                    
                R +=1
            nums[L], nums[pivot] = nums[pivot], nums[L]
            return L
        
        left, right, pivot = 0,0,len(nums)-1
        
        while True:
            idx = partion(left,right,pivot)
            
            if idx == len(nums)-k:
                return nums[idx]
            
            elif idx < len(nums)-k:
                left = idx+1
                right = idx+1
            else:
                pivot = idx-1
                right = 0
                left = 0
            
            
            
            
        
        
        
        