class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        groups = []
        for i in range(len(intervals)):
            if groups and intervals[i][0] > groups[0]:
                heapq.heappop(groups)
            heapq.heappush(groups, intervals[i][1])
          
        
        return len(groups)
        