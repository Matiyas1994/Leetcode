class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        time = []
        
        for t in  timePoints:
            inttime = int(t[:2])*60 + int(t[3:])
            time.append(inttime)
            time.append(24*60 + inttime)
        
        time.sort()
        minn = float(inf)
        
        for i in range(len(time)-1):
            minn = min(minn, time[i+1] - time[i])
        
        return minn
        