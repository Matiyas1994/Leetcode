class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        ans = 0
        relation = None
        for i in range(1,n):
            if nums[i] > nums[i-1]:
                if relation == -1:
                    ans +=1
                relation = 1 
            elif nums[i] < nums[i-1]:
                if relation == 1:
                    ans +=1
                relation = -1
                
        if relation == None:
            return 1
        return ans + 2  
        
        