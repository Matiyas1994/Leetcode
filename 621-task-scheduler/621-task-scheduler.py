class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxFreq = max(freq.values())
        
        numOfMaxFreq = 0 
        for key, val in freq.items():
            if maxFreq == val:
                numOfMaxFreq +=1
        
        emptySlot =(maxFreq-1) * (n - (numOfMaxFreq-1))
        withoutA= len(tasks)- maxFreq*numOfMaxFreq
        numOfIdel = max(0,emptySlot - withoutA)
        
        return len(tasks) + numOfIdel
        
        # A B _ A B _ AB
        