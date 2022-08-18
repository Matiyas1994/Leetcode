class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = Counter(arr)
        ans, total = 0, 0
        mid = len(arr)//2
        for key, freq in (sorted(counter.items(), 
                                key= lambda x:x[1], 
                                 reverse = True)):
            if total >= mid:
                break
            total +=freq
            ans +=1
        
        return ans
            
            
        
        
        
        