class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxFreq = max(freq.values())  #3
        
        lastposition = (maxFreq-1) * (n+1) #6
        
        numOfMaxFreq = 0 
        
        for key, val in freq.items():
            if maxFreq == val:
                numOfMaxFreq +=1
    
        return max(lastposition + numOfMaxFreq, len(tasks))
    

        
        
        
    
                                

        
        
        
        
        
       
        
        