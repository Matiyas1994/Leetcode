class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank.append(start)
        def cango(s1, s2):
            c = 0
            for i in range(8):
                if s1[i] != s2[i]:
                    c +=1
                if c > 1:
                    return False
            
            return True
        
        graph = defaultdict(list)
        for i in range(len(bank)):
            for j in range(i+1):
                if cango(bank[i], bank[j]):
                    graph[bank[i]].append(bank[j])
                    graph[bank[j]].append(bank[i])
                    
        visited = set()
        queue = deque()
        
        def bfs(node):
            visited.add(node[1])
            queue.append(node)
            
            while queue:
                node, steps = queue.popleft()
                
                if node==end:
                    return steps
                
                for negbour in graph[node]:
                    if negbour not in visited:
                        queue.append((negbour,steps+1))
                        visited.add(negbour)
            return -1
        
        return bfs((start, 0))
                
            
            
     