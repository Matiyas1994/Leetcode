class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        haveIncomingEdge = set()
        for edge in edges:
            haveIncomingEdge.add(edge[1])
        ans = []
        for node in range(n):
            if node not in haveIncomingEdge:
                ans.append(node)
        return ans