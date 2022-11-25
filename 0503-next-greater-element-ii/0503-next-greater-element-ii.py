class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        mostack = []
        n = len(nums)
        ans = [-1]*n
        
        for i in range(n):
            while mostack and nums[mostack[-1]] < nums[i]:
                idx = mostack.pop()
                ans[idx] = nums[i]
            mostack.append(i)
            
        for i in range(n):
            while mostack and nums[mostack[-1]] < nums[i]:
                idx = mostack.pop()
                ans[idx] = nums[i]

        
        return ans
        