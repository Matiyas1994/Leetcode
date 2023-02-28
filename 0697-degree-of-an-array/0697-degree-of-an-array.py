class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        degree = 0
        dic = defaultdict(list)
        
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]][0] +=1
                dic[nums[i]][2] = i
            else:
                dic[nums[i]].extend([1,i,i])
            degree = max(degree, dic[nums[i]][0])
        ans = float(inf)
        for key, val in dic.items():
            if val[0]==degree:
                ans = min(ans, val[2]-val[1] + 1)
        
        return ans
    
        