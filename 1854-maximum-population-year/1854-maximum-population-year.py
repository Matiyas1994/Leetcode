class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        lifeTime = Counter()
        
        for i in range(len(logs)):
            birth, death = logs[i]
            lifeTime[birth] +=1
            lifeTime[death] -=1
        

        maxPopulation = 0
        year = 0
        curPopulation = 0
    
        for key, val in sorted(lifeTime.items()):
            curPopulation += val
            if curPopulation > maxPopulation:
                maxPopulation = curPopulation
                year = key
        
        return year
            
        
        
        
        