#User function Template for python3

class Solution:
    def isPossible(self,N,prerequisites):
        
        from collections import defaultdict, deque
        graph = defaultdict(list)
        indegree = [0]*N
        pq = deque()
        visited = set()
        
        #constracting a graph
        for task in prerequisites:
            graph[task[1]].append(task[0])
            indegree[task[0]] += 1
        
        # appending nodes which have no incoming edges
        for i in range(N):
            if indegree[i] ==0:
                pq.append(i)

        
        #topsort
        
        while pq:
            
            node = pq.popleft()
            visited.add(node)
            
            for negbour in graph[node]:
                indegree[negbour] -=1
                
                if indegree[negbour] == 0:
                    pq.append(negbour)
        
        return len(visited) == N
                
                
            
        
        
        
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        N=int(input())
        P=int(input())

        prerequisites=[]
        for _ in range(P):
            pair = [int(x) for x in input().split()]
            prerequisites.append(pair)
        ob=Solution()
        if(ob.isPossible(N,prerequisites)):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends