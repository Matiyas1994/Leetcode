class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int: 
        sumOfGas, sumOfCost, tank, startPoint = 0, 0, 0, 0
        
        for i in range(len(gas)):
            sumOfGas += gas[i]
            sumOfCost += cost[i]
            
            tank += gas[i] - cost[i]
            
            if tank < 0:
                startPoint = i+1
                tank = 0
        
        return -1 if sumOfCost > sumOfGas else startPoint
        