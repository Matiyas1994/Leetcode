class UnionFind:
    def __init__(self,size):
        self.parent = defaultdict()
        self.parent = {i: i for i in range(size)}
   
    def find(self,v):
        
        while(self.parent[v] != v):
            v = self.parent[v]
        return v
        # if v == self.parent[v]:
        #     return v
        # self.parent[v] = self.find(self.parent[v])
    def union(self,v1,v2):
        a = self.find(v1)
        b = self.find(v2)
        
        self.parent[b] = a
    

class Solution:
     def findCircleNum(self, isconnected: List[List[int]]) -> int:
        obj = UnionFind(len(isconnected))
        
        for i in range(len(isconnected)):
            for j in range(len(isconnected[0])):
                if i != j and isconnected[i][j]==1:
                    obj.union(i,j)
        num = set()
        print(obj.parent)
        for value in range(len(isconnected)):
            num.add(obj.find(value))
        return len(num)
                