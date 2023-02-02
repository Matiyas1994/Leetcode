class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0
        
        def takeMin():
            minn = float(inf)
            for i in range(len(nums)):
                if nums[i] !=0:
                    minn = min(minn, nums[i])
            
            return minn
        
        while True:
            minn = takeMin()
            if minn == float(inf):
                break
            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[i] -=minn
            operations +=1
        
        return operations
        