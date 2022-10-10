class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        visited = set()
        ans = [-1]*n
        dic = defaultdict(list)
        
        for e in redEdges:
            dic[e[0]].append((e[1],"r"))
        
        for e in blueEdges:
            dic[e[0]].append((e[1],"b"))
        
        queue = deque()
        
        queue.append((0,0,"z"))
        visited.add((0,-1,"z"))
        
        while queue:
    
            node, level, color = queue.popleft()
            
            if ans[node]==-1: ans[node] = level
            for end in dic[node]:
                if color != end[1] and (node,end[0], end[1]) not in visited:
                    queue.append((end[0], level+1, end[1]))
                    visited.add( (node,end[0], end[1]))
        
        return ans
            
            
        
        
        
        