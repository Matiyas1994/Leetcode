class UnionFind:
    def __init__(self,size):
        self.parent = {i: i for i in range(size)}      
        self.rank = {i: 0 for i in range(size)}
        self.num = size
    def find(self,v):
        
        # while(self.parent[v] != v):
        #     v = self.parent[v]
        # return v
        if v == self.parent[v]:
            return v
        self.parent[v] = self.find(self.parent[v])
        return self.parent[v]
    def union(self,v1,v2):
        a = self.find(v1)
        b = self.find(v2)
        
        if a!=b:
            
            if self.rank[a] < self.rank[b]:
                a, b = b, a
                
            self.parent[b] = a
            self.num -=1
            # if self.rank[a] == self.rank[b]:
            self.rank[b] += 1

class Solution:
     def findCircleNum(self, isconnected: List[List[int]]) -> int:
        obj = UnionFind(len(isconnected))
        
        for i in range(len(isconnected)):
            for j in range(len(isconnected[0])):
                if i != j and isconnected[i][j]==1:
                    obj.union(i,j)
    
    
      
        return obj.num
                