class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(dict)
        for u, v, w in roads:
            graph[u][v] = graph[v][u] = w
        
        res = inf
        vis = set()
        dq = deque([1])

        while dq:
            node = dq.popleft()
            for adj, scr in graph[node].items():
                if adj not in vis:
                    dq.append(adj)
                    vis.add(adj)
                res = min(res,scr)
                
        return res
                
        
        
#         distance = [float(inf) for _ in range(n+1)]
#         distance[1] = 0
#         graph = defaultdict(list)
#         for node1, node2, dis in roads:
#             graph[node1].append((node2, dis))
#             graph[node2].append((node1, dis))
#         hp = []
#         visited = set()
#         hp.append((0,1))
        
#         while hp:
#             dis, node = heapq.heappop(hp)
#             visited.add(node)
            
#             if node==n:
#                 return distance[n]
            
#             for next_node, cost in graph[node]:
                
#                 if next_node not in visited and  dis + cost < distance[next_node]:
#                     distance[next_node] =  distance[node] + cost
#                     heapq.heappush(hp, (distance[next_node], next_node))
        
#         return distance[n]