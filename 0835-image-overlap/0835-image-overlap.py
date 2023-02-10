class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        dic = {}
        cellWith1Inimg1 = []
        cellWith1Inimg2 = []
        ans = 0
        for i in range(len(img1)):
            for j in range(len(img1[0])):
                if img1[i][j] == 1:
                    cellWith1Inimg1.append((i,j))
                if img2[i][j] == 1:
                    cellWith1Inimg2.append((i,j))

        for ax, ay in cellWith1Inimg1:
            for bx, by in  cellWith1Inimg2:
                dif = (bx - ax, by - ay)
                if dif in dic:
                    dic[dif] += 1
                else:
                    dic[dif] = 1
                ans = max(ans, dic[dif])
        return ans