class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        def dfs(node=0, path=[0]):
            
            if node == len(graph)-1:
                ans.append(path[:])
                return
            
            for nxt in graph[node]:
                path.append(nxt)
                dfs(nxt,path[:])
                path.pop()
        dfs()
        return ans