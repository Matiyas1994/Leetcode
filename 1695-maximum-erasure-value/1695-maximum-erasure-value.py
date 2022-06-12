class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        Max = 0
        prif = [0]
        n = len(nums) 
        for nu in nums:
            prif.append(prif[-1]+ nu)
        
        p1, p2 = 0, 0
        dic = {}
        
        while p2 < n:
            while p2 < n and (nums[p2] not in dic or dic[nums[p2]] < p1):
                dic[nums[p2]] = p2 
                p2 +=1
                
            Max = max(Max,prif[p2]-prif[p1])
            if p2 >= n:
                break
                
            p1 =dic[nums[p2]] + 1
            dic[nums[p2]] = p2
            p2 +=1
    
        return Max