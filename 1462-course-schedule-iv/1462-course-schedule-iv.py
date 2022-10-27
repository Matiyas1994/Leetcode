class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        ans = []
        n = numCourses
        dis =[[False if i!=j else True for i in range(n)] for j in range(n)]

        for s, e in prerequisites:
            dis[s][e] = True


        for i in range(n):
            for j in range(n):
                for k in range(n):
                    dis[j][k] = (dis[j][k]) or(dis[j][i] and dis[i][k])

        for s, e in queries:
            ans.append(dis[s][e])
    
        return ans