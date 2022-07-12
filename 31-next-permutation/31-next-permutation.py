class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rStartIdx = 0
        n = len(nums)
        for i in range(n-1,0,-1):
            if nums[i] > nums[i-1]:
                rStartIdx = i
                for j in range(n-1,i-1,-1):
                    if nums[j] > nums[i-1]:
                        nums[i-1], nums[j] = nums[j], nums[i-1]
                        break
                else:
                    continue
                break
                
#         reversing     
        s =rStartIdx
        e = n-1
        while s < e:
            nums[s], nums[e] = nums[e], nums[s]
            s +=1
            e -=1
 