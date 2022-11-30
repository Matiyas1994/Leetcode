

from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		visited = set()
		def cycledetect(node, previousNode, visited):
		  
		    visited.add(node)
		    
		    for neigbour in adj[node]:
		        if neigbour in visited and neigbour==previousNode: continue
		        if neigbour in visited: return True
		        else:
		            if cycledetect(neigbour, node, visited): return True
		            
		for node in range(V):
		    if node not in visited:
    		    if cycledetect(node,-1, visited):
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