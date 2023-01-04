class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        c = Counter(tasks)
        answer = 0 
        for key, val in c.items():
            if val < 2:
                return -1
            answer += (val//3)
            answer += 1 if val%3 else 0
            
        
        return answer
        