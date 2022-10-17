class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        pq = deque()
        visited = set()
        
        def bfs(node):
            pq.append(node)
            visited.add(node)
            
            while pq:
                node = pq.popleft()
                
                for negbour in rooms[node]:
                    if negbour not in visited:
                        visited.add(negbour)
                        pq.append(negbour)
        
        bfs(0)
        return len(visited)==len(rooms)
        
        