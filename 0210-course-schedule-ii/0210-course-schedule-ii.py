class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        incomingEdge = {}
        for prerequisit, course in prerequisites:
            graph[course].append(prerequisit)
            incomingEdge[prerequisit] = incomingEdge.get(prerequisit, 0) + 1
        queue = deque()
        for i in range(numCourses):
            if i not in incomingEdge:
                queue.append(i)
        ans = []
    
        while queue:
            
            course = queue.popleft()
            
            ans.append(course)
            
            for neg in graph[course]:
                incomingEdge[neg] -=1
                if incomingEdge[neg] == 0:
                    queue.append(neg)
        
        return ans  if len(ans)==numCourses else []
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         top_sort = []
#         queue = deque()
#         indegre = defaultdict(lambda:0) 
        
      
#         graph = defaultdict(set) 
        
#         for i in prerequisites:
#             indegre[i[0]] = 0
#             indegre[i[1]] = 0
            
          
        
#         for i in prerequisites: 
#             des , src = i[0] , i[1]
#             indegre[des] +=1 
#             graph[i[1]].add(i[0])
    
    
#         for node in range(numCourses):
#             if indegre[node] == 0:
#                 queue.append(node)
        
#         while queue:
#             n = queue.popleft()
#             top_sort.append(n)
            
#             for neb in graph[n]:
#                 indegre[neb] -=1
#                 if indegre[neb] == 0:
#                     queue.append(neb)
                
#         return top_sort if len(top_sort) ==  numCourses else [] 
    
        