class Solution:
    def maximumSwap(self, num: int) -> int:
        withIdx = []
        num = list(map(int, str(num)))
        for idx, d in enumerate(num):
            withIdx.append((d, idx))
        withIdx.sort(key = lambda x: (x[0], -x[1]),reverse=True)
        
        for i in range(len(num)):
            if withIdx[i][0] > num[i]:
                j = i
                while j < len(num)-1 and withIdx[j+1][0]==withIdx[j][0]:
                    j +=1

                num[i], num[withIdx[j][1]] = num[withIdx[j][1]], num[i]
                break
        return int("".join(str(i) for i in num))
    
        
        