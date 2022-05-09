class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        time = []
        
        for t in  timePoints:
            time.append(int(t[:2])*60 + int(t[3:]))
           
        
        time.sort()
        minn = float(inf)
        
        for i in range(len(time)-1):
            minn = min(minn, time[i+1] - time[i])
        
        return min(minn, time[0]+ 24*60 - time[-1])
        