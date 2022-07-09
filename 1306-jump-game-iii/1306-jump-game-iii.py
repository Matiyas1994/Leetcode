class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque()
        queue.append(start)
        visited = set()
        
        while queue:
            n = queue.popleft()
            if arr[n] == 0:
                return True
            if 0<= n+arr[n] < len(arr) and n+arr[n] not in visited: 
                queue.append(n+arr[n])
                visited.add(n+arr[n])
            if 0<= n-arr[n] < len(arr) and n-arr[n] not in visited:
                queue.append(n-arr[n])
                visited.add(n-arr[n])
        
        
            