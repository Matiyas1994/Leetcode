class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        queue = deque()
        visited = {}
        
        def checkBipartie(node):
            
            queue.append(node)
            visited[node[0]]= node[1] 
            
            while queue:
                
                node = queue.popleft()
                
                for neg in graph[node[0]]:
                    if neg not in visited:
                        visited[neg] = abs(node[1]-1) 
                        queue.append((neg, abs(node[1]-1)))
                    elif neg in visited and visited[neg]==node[1]:
                        return False
            
            return True
            
        for node in range(len(graph)):
            if node not in visited:
                if not checkBipartie((node,1)): return False
                                     
        return True
                    
                
                
        