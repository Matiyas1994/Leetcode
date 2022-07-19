class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 1
        p2  = 1
        n = len(nums)
        
        while p2 < n:
            while p2 < n and nums[p2]==nums[p1-1]:
                p2 +=1
                
            if p2 < n:   
                nums[p1] = nums[p2]
                p1 +=1
                
        return p1
            

            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        if len(nums)==0 or len(nums)==1:
            return len(nums)
        k=0
        for i in range(len(nums)-1):
            if nums[i]!=nums[i+1]:
                nums[k] = nums[i]
                k+=1                  
        
        nums[k] = nums[len(nums)-1] 
        k+=1
        return k
           
  