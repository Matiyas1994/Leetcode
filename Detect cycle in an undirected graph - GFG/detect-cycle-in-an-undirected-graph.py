

from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		visited = set()
		def dfs(node,prev):
		    visited.add(node)
		    for next_node in adj[node]:
		        if next_node in visited and next_node != prev:
		            return True
		        elif next_node not in visited:
		            if dfs(next_node, node):
		                return True
		
		
		for node in range(V):
		    if node not in visited:
		        if dfs(node, -1):
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