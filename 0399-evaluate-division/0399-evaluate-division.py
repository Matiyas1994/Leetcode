class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i, eq in enumerate(equations):
            graph[eq[0]].append((eq[1],values[i]))
            graph[eq[1]].append((eq[0],1/values[i]))
        
        visited = set()
        def equationEvaluator(s,e):
            if s in visited: return float(inf)
            if s==e:
                return 1
            
            visited.add(s)
       
            ans = float("inf")
            for neg in graph[s]:
                t = equationEvaluator(neg[0],e)
                if t != float(inf):
                    ans = equationEvaluator(neg[0],e)*neg[1]
               
            visited.remove(s)
     
            return ans
          
        
        res = []
        for i in range(len(queries)):
            if queries[i][0] not in graph or queries[i][1] not in graph:
                res.append(-1)
            else:
                u = equationEvaluator(queries[i][0], queries[i][1])
                if u >= float(inf):
                    res.append(-1)
                else: res.append(u)
                
        return res
            
                