#User function Template for python3

class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    
    def bfsOfGraph(self, V, adj):
        from collections import  deque 
        # code here
        ans = []
        visited = set()
        queue = deque()
        queue.append(0)
        
        visited.add(0)
        
        while queue:
            pop = queue.popleft()
            ans.append(pop)
            
            for neghbour in adj[pop]:
                if neghbour not in visited:
                    visited.add(neghbour)
                    queue.append(neghbour)
        
        return ans
            
        


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
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends