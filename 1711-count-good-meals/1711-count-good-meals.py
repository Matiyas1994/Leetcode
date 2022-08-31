class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        
        ans = 0
        for i in range(22):
            dic = defaultdict(int)
            for val in deliciousness:
                if ((1<<i) - val) in dic:
                    ans += dic[((1<<i) - val)]
                dic[val] +=1
                
        
        
        return ans%(10**9 + 7)
                    
        

