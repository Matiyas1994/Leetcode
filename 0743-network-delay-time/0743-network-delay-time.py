class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        #buildig the network 
        graph = defaultdict(list)
        visited = set()
        
        for i in range(len(times)):
            source, destination, time = times[i]
            graph[source].append((destination, time))
            
        
        def shortestpath(startNode):
            dis = [float(inf)]*(n+1)
            dis[startNode] = 0
            
            pq  = [(0, startNode)]
            visited.add(startNode)
            mx = float(-inf)
            
            while pq:
                
                curNode = heapq.heappop(pq)
                
                visited.add(curNode[1])
                mx = max(mx, dis[curNode[1]])
                
                for negbour, distance in graph[curNode[1]]:
                    if negbour not in visited:
                        if dis[curNode[1]]+ distance < dis[negbour]:
                            dis[negbour] = dis[curNode[1]] + distance
                            heapq.heappush(pq, (dis[negbour], negbour))
                        
                            
                        
            return mx
        res = shortestpath(k)               
        return res if len(visited)==n else -1    
                
    
            
        