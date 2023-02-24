class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        userTime = defaultdict(set)
        timeUser = [0 for _ in range(k)]
        
        for U_id, minn in logs:
                userTime[U_id].add(minn)
                
        
        for key, val in userTime.items():
            numOfUser = len(val)
            timeUser[numOfUser-1] +=1
        return timeUser
                
        
        
        