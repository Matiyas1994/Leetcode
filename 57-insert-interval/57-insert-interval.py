class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        - iterate throught the list and find the right idx to put the new interval
        - if the new interval conflicts with the one of the old intervals i would merge it              with the left and right interval
        -else i will palace where it suppose to be 
        
        -finanally i will shift the intervals to next index
        -at the start, at the end, merge with two,   
        
        """
        n = len(intervals)
        i = n - 1
        ans = []
        
        while i >= 0 and intervals[i][0] > newInterval[0]: i -=1
        
        if i == -1:
            intervals.insert(0, newInterval)
        else:
            intervals.insert(i+1, newInterval)
    
        
        for idx in range(n+1):
            if ans and intervals[idx][0] <= ans[-1][1]:
                ans[-1][1] = max(intervals[idx][1],ans[-1][1])
            else:
                ans.append(intervals[idx])
        
        return ans
            
        
        
        
                
        
            
            
        
        