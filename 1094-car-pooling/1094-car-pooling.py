class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key= lambda x: x[1])
        pq = []
        totalPeople = 0
        for pas in trips:
            while pq and pq[0][0] <= pas[1]:
                droped = heapq.heappop(pq)
                totalPeople -=droped[1] 
            if pas[0]+totalPeople > capacity:
                return False
            heapq.heappush(pq, (pas[2],pas[0]))
            totalPeople +=pas[0]
           
        
        return True
        