class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        mod = (10**9)+7 
        zipped = list(zip(speed, efficiency))
        zipped.sort( key = lambda x :x[1], reverse= True)
        pq = []
        s = 0  
        maxPerformance = 0
        for aspeed, anEfficiency in zipped:
            s += aspeed
            heapq.heappush(pq,(aspeed,anEfficiency))
            while len(pq) > k:
                popped = heapq.heappop(pq)
                s -= popped[0]
            maxPerformance = max(maxPerformance, s*anEfficiency)
        
        return maxPerformance % mod