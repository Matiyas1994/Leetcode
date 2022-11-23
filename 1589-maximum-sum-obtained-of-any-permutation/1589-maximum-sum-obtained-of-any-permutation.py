class Solution:
    def maxSumRangeQuery(self, nums: List[int], requists: List[List[int]]) -> int:
        n = len(nums)
        occurance = [0]*(n+1)

        for start, end in requists:
            occurance[start] +=1
            occurance[end+1] -=1

        #building the occurance of the idx
        for i in range(1,len(occurance)):
            occurance[i] += occurance[i-1]
        occurance.pop()
        for i, val in enumerate(occurance):
            occurance[i] = (val, i)
        
        occurance.sort()
        nums.sort()
        PerfectPermituation = [0]*(n)
    
       
        for i in range(n):
            freq, idx = occurance[i]
            PerfectPermituation[idx] = nums[i]

        prefixSum = [0]
        #building prefix sum 
        for i in range(len(PerfectPermituation)):
            prefixSum.append(PerfectPermituation[i] + prefixSum[-1])

        totalMaxSum = 0
        for start, end in requists:
            totalMaxSum += prefixSum[end+1] - prefixSum[start]

        return totalMaxSum  % 1000000007