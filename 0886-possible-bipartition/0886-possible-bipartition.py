class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        color = [-1]*(n+1)
        #build the graph
        for person1 , person2 in dislikes:
            graph[person1].append(person2)
            graph[person2].append(person1)
        
        pq = deque()
        visited = set()
        
        def bipartite(node, c):
        
            pq.append(node)
            visited.add(node)
            color[node] = c
            
            while pq:
                node = pq.popleft()
                
                for negbour in graph[node]:
                    if color[negbour]==color[node]: return False
                    if negbour not in visited:
                        pq.append(negbour)
                        visited.add(negbour)
                        color[negbour] = abs(color[node]-1)
            return True
        
        for i in range(1,n+1):
            if i not in visited:
                if not bipartite(i, 0):
                    return False
        return True
                    
        
            
        