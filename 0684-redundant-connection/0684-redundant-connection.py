class Union_Find:
    def __init__(self, n):
        self.parent = {i:i for i in range(n)}
        self.rank = [1] * n
    
        
    def find(self, node):
        if node == self.parent[node]:
            return node
        
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, node1, node2):
        p1, p2 = self.find(node1), self.find(node2)
        
        if self.rank[p1] < self.rank[p2]:
            p1, p2 = p2, p1
        
        self.parent[p2] = p1
        self.rank[p1] += self.rank[p2]
        
    def same(self, node1, node2):
        return self.find(node1) == self.find(node2)
        
        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        UF = Union_Find(len(edges)+1)
        for node1, node2 in edges:
            if UF.same(node1, node2):
                return [node1, node2]
            UF.union(node1, node2)
            
                
        
        
        
        