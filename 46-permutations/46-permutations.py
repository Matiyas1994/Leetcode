class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        with constant space
        """
        ans = []
        def backtrack(start,nums):
            if start == len(nums):
                ans.append(nums[:])
            
            else:
                for i in range(start,len(nums)):
                    nums[start], nums[i] = nums[i], nums[start]
                    backtrack(start+1,nums)
                    nums[start], nums[i] = nums[i], nums[start]
                        
        backtrack(0,nums)
        return ans
        
        
        
        
        
#         ans = []
#         exist = [0 for i in range(len(nums))]
#         def permutationGenerator(start=0, temp=[], exist=exist):
#             if len(temp)== len(nums):
#                 ans.append(temp[:])
            
#             else:
#                 for i in range(len(nums)):
#                     if exist[i] !=0 : continue
#                     temp.append(nums[i])
#                     exist[i] = 1
#                     permutationGenerator(i+1,temp, exist)
#                     temp.pop()
#                     exist[i] = 0
                    
#         permutationGenerator()
#         return ans
        