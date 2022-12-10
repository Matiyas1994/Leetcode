class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        visited = [0]*n
        ans = []
        
        def dfs(node, path):
            if not visited[node]:
                visited[node] = 1
                path.append(node)
                
                if node==len(graph)-1:
                    ans.append(path[::])
                    
                
                for next_node in graph[node]:
                    dfs(next_node,path)
                
                visited[node] = 0
                path.pop()
        
        dfs(0,[])
        return ans
        
        