class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [float("-inf") for i in range(n)]
        dp[0] = nums[0]
        heap = [(-1*dp[0],0)]
        heapq.heapify(heap)
        
        for i in range(1,n):
            while heap[0][1] < i-k:
                heapq.heappop(heap)
                
            dp[i] = -1*heap[0][0] + nums[i]
            heapq.heappush(heap,(-1*dp[i],i))
                
        return dp[-1]
                    