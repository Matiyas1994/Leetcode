class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ans = []
        graph = defaultdict(list)
        indegree ={r: 0 for r in recipes}
        visited = set()
        queue = deque()
        
        
        for i in range(len(recipes)):
            for ing in ingredients[i]:
                graph[ing].append(recipes[i])
                indegree[recipes[i]] +=1
        
        
        for sup in supplies:
            queue.append(sup)
            visited.add(sup)

        
       
        while queue:
            
            suply = queue.popleft()
            
            for ing in graph[suply]:
                indegree[ing] -=1
                if indegree[ing] <= 0 and ing not in visited:
                    queue.append(ing)
                    visited.add(ing)
                    ans.append(ing)
            
          
        
        return ans