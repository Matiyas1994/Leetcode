class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        pq =[]
        for key, frq in freq.items():
            heapq.heappush(pq, (-frq,key))
        ans = []
        while k:
            ans.append(heapq.heappop(pq)[1])
            k -=1
        return ans
            
        
        
            
        
        
        
        
        
        