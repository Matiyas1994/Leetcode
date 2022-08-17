class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int: 
        
        tatal = sum (gas[i]-cost[i] for i in range(len(gas)))
        if tatal < 0 : return -1
        
        ans, pref = 0,0
        for i in range(len(gas)):
            pref += gas[i]-cost[i]
        
            if pref < 0:
                ans = i+1
                
            pref = max(0,pref)
                
        return ans
            
        
        