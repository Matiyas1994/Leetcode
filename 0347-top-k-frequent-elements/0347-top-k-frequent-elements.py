class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        pq =[]
        
        for key, frq in freq.items():
            heapq.heappush(pq, (frq,key))
            if len(pq) > k:
                heapq.heappop(pq)
        ans = []
        for f, k in pq:
            ans.append(k)
        return ans
            
                
#         ans = []
#         while k:
#             ans.append(heapq.heappop(pq)[1])
#             k -=1
#         return ans
            
        
        
            
        
        
        
        
        
        