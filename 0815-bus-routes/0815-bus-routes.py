class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        queue = deque([(source, 0)])
        graph = defaultdict(set)
        visited = set()
        
        for bus, route in enumerate(routes):
            for busStop in route:
                graph[busStop].add(bus)
                        
        while queue:
            curStation, curDist = queue.popleft()

            if curStation == target:
                return curDist
            
            visited.add(curStation)
            
            for bus in graph[curStation]:
                for next_station in routes[bus]:
                    if next_station not in visited:
                        queue.append((next_station, curDist + 1))
						
                routes[bus] = set()

        return -1