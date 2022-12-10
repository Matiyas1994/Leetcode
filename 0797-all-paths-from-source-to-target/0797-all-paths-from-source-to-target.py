class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        answer = []
        
        def dfs(node, path):
            path.append(node)
            
            if node==len(graph)-1:
                answer.append(path[:])


            for next_node in graph[node]:
                dfs(next_node,path)
                
            path.pop()

        dfs(0,[])
        return answer
        
        