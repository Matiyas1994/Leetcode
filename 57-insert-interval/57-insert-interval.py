class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i = 0
        ans = []
        
        while i < n and intervals[i][0] < newInterval[0]:
            ans.append(intervals[i])
            i +=1
        
        if ans and newInterval[0] <= ans[-1][1]:
            ans[-1][1] = max(newInterval[1], ans[-1][1])
        else:
            ans.append(newInterval)
        
        while i < n :  
            if ans and intervals[i][0] <= ans[-1][1]:
                ans[-1][1] = max(intervals[i][1], ans[-1][1])
            else:
                ans.append(intervals[i])
            
            i +=1
                
        return ans
       