class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
       
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]: continue
            j, k = i+1, n-1
            
            while j < k:
                curSum = nums[i]+nums[j]+nums[k]
                if curSum == 0:
                    ans.append([nums[i],nums[j],nums[k]])
                
                    while j<k and nums[j+1]==nums[j]:
                        j +=1
                    j +=1
                    while j<k and nums[k] == nums[k-1]:
                        k -=1
                    k -=1
                    
                elif curSum > 0:
                    k -=1
                else:
                    j +=1
        return ans
                
            
        