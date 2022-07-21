class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtracking(i=0, temp=[]):
            ans.append(temp[:])
            
            for i in range(i, len(nums)):
                temp.append(nums[i])
                backtracking(i+1,temp)
                temp.pop()
                
        backtracking()       
        return ans
            
            
        
        
        
        
        
        
        
        
        
        
#         res = []
#         n = len(nums)
        
#         for i in range(1<<n):
#             curlist = []
#             for j in range(n-1,-1,-1):
#                 if i&(1<<j):
#                     curlist.append(nums[j])
#             res.append(curlist)
        
#         return res
        
    
#         res = []
#         def rec(cur = [],i = 0):
#             if i >= len(nums):
#                 res.append(cur[:])
#                 return

#             rec(cur[:],i+1)
#             cur.append(nums[i])
#             rec(cur[:],i+1)
#         rec()
#         return res

        
        
        
        