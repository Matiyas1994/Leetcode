#User function Template for python3
class Solution:
    def check(self, N, M, Edges): 
        #code here
        from collections import defaultdict
        graph = defaultdict(list)
        visited = set()
        
        for e in Edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
          
        
        def dfs(node, count, prev):
            visited.add(node)
            if count==N:
                return True
            
            for neghbour in graph[node]:
                if neghbour == prev or neghbour==node: continue
                if neghbour not in visited:
                    if dfs(neghbour, count+1, node): return True
                    
            visited.remove(node)
            return False
                
            
        
    
        
        for node in range(1, N+1):
            if dfs(node, 1, -1):
                return True
        False
            

            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N,M = map(int,input().strip().split())
        Edges=[]
        e = list(map(int,input().strip().split()))
        for i in range(M):
            Edges.append([e[2*i],e[2*i+1]])
        ob = Solution()
        if ob.check(N, M, Edges):
            print(1)
        else:
            print(0)
# } Driver Code Ends