
from collections import defaultdict
from typing import List
class UnionFind:
    def __init__(self, numNode):
        self.parent = {i: i for i in range(numNode)}
    
    def find(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
        
    def union(self, node1, node2):
        node1 = self.find(node1)
        node2 = self.find(node2)
        
        if node1 != node2:
            self.parent[node2] = node1
        
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        parent = {}
        visited = set()
        
        for i in range(V):
            parent[i] = i
            
        def find(node):
            if parent[node] == node:
                return node
            parent[node] = find(parent[node])
            
            return parent[node]
        
        def union(u, v):
            root1, root2 = find(u), find(v)
            
            if root1 != root2:
                parent[root1] = root2
                return False
            else:
                return True
		
		for u,v  in enumerate(adj):
		    for i in range(len(v)):
		        if (u, v[i]) not in visited:
                    points = union(u, v[i])
                    visited.add((u, v[i]))
                    visited.add((v[i], u))
                    if points:
                        return True
        return False
		        
		    
		


#{ 
 # Driver Code Starts


if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends