#User function Template for python3

from collections import defaultdict
class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code her
        state = [0] * V
        path = []
        def dfs(node):
            if state[node]==1: return True
            if state[node]==2: return False
            state[node]= 1
            path.append(node)
            
            for next_node in adj[node]:
                if dfs(next_node): return True
                
            state[node] = 2
            
            return False
        for node in range(V):
            if dfs(node):
                return True

        return False
        
    
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends