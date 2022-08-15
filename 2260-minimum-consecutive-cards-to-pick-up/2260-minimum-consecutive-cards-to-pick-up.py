class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        minn = float("inf")
        lastidx = {}
        for i in range(len(cards)):
            if cards[i] in lastidx:
                minn = min(minn, i-lastidx[cards[i]]+1)
        
            lastidx[cards[i]]= i
        
        return -1 if minn == float(inf) else minn
                
                 
                
        
        
        