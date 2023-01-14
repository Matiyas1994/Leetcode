class Union_Find:
    def __init__(self):
        self.parent ={ chr(i): chr(i) for i in range(97,97+26)}
    
    def find(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, nodeA, nodeB):
        pa = self.find(nodeA)
        pb = self.find(nodeB)
        
        if pa <= pb:
            pa, pb = pb, pa
            
        self.parent[pa] = pb
    
    def same(self,nodeA, nodeB):
        return self.find(nodeA) == self.find(nodeB)
    
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        Uf = Union_Find()
        
        for i in range(len(s1)):
            if not Uf.same(s1[i], s2[i]):
                Uf.union(s1[i], s2[i])
        ans = []
        for ch in baseStr:
            ans.append(Uf.find(ch))
        
        return "".join(ans)
        
        