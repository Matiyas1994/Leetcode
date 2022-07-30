class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def permutationGenerator(start=0, temp=[]):
            if len(temp)== len(nums):
                ans.append(temp[:])
            
            else:
                for i in range(len(nums)):
                    if nums[i] in temp: continue
                    temp.append(nums[i])
                    permutationGenerator(i+1,temp)
                    temp.pop()
                    
        permutationGenerator()
        return ans
        