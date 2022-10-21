class Union_Find:
    def __init__(self,n):
        self.parent = {i : i for i in range(n)}
        self.rank = [1] * n 
        
    def find(self, node):
        if node == self.parent[node]:
            return node
        
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, node1, node2):
        p1, p2 = self.find(node1), self.find(node2)
        
        if p1 != p2:
            if self.rank[p1] < self.rank[p2]:
                p1, p2 = p2, p1
                
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
            
    def same(self, node1, node2):
        return self.find(node1) == self.find(node2)
        


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        Uf = Union_Find(n)
        ans = 0
        ls = []
        for i in range(n-1):
            for j in range(i+1, n):
                ls.append((abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1]), i, j))
        
        ls.sort()
        for edge in ls:
            if not Uf.same(edge[1], edge[2]):
                Uf.union(edge[1], edge[2])
                ans +=edge[0]
                   
        return ans
                
            