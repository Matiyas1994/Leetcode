class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        onlyOneAdjecent = set()
        for num1, num2 in adjacentPairs:
            graph[num1].append(num2)
            graph[num2].append(num1)
            onlyOneAdjecent.add(num1)
            onlyOneAdjecent.add(num2)
            if len(graph[num1]) > 1:
                onlyOneAdjecent.remove(num1)
            if len(graph[num2]) > 1:
                onlyOneAdjecent.remove(num2)
        ans = []
        visited = set()
        def dfs(node):
            if node not in visited:
                visited.add(node)
                ans.append(node)
                
                for next_num in graph[node]:
                    dfs(next_num)
        
        for startNode in onlyOneAdjecent:
            dfs(startNode)
            return ans
            
        