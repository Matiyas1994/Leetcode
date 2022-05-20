class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        
        for i in range(1<<n):
            curlist = []
            for j in range(n-1,-1,-1):
                if i&(1<<j):
                    curlist.append(nums[j])
            res.append(curlist)
        
        return res
        
        
        
        