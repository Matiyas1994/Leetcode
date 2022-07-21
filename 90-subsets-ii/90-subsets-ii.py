class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        
        def backtracking(start=0, temp=[]):
            ans.append(temp[:])
            
            for i in range(start,len(nums)):
                if i != start and nums[i] == nums[i-1]: continue
                temp.append(nums[i])
                backtracking(i+1, temp)
                temp.pop()
        
        backtracking()
        return ans
        