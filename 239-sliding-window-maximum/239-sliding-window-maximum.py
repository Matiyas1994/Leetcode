class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # [1,3,-1,-3,5,3,6,7]
        # [3,3,5]
#         heap[(1,0),(3,1),(-1,2)(-3,3)(5,4)]
# push new element 
#  while max index <= i-k pop it 
        pq = []
        ans = []
        for i in range(k):
            heappush(pq, (-nums[i], i))
        ans.append(-pq[0][0])
        for i in range(k,len(nums)):
            
            heappush(pq, (-nums[i],i))
            while pq and pq[0][1] <= i-k:
                heappop(pq)
                
            ans.append(-pq[0][0])
            
        return ans
        