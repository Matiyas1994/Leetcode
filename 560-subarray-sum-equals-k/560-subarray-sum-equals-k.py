class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
      #   [1,2,4,6,-5,4,1] k = 10
      # [0 1 3,7,13,8,12,13]
      #               13-10
    
     
        prefixSum , ans= 0, 0
        HashMap = {0 : 1}
        n = len(nums)
        
        
        for i in range(n):
            prefixSum += nums[i]
          
        
            if prefixSum - k in HashMap:
                ans += HashMap[prefixSum - k ] 
            
            HashMap[prefixSum] = HashMap.get(prefixSum , 0) + 1
            
     
                
                
        return ans
            
        
        
        
        