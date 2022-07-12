class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans= [[1],[1,1]]
        if numRows==1:
            return [[1]]
        elif numRows == 2:
            return ans
        
        for j in range(2,numRows):
            temp = [1]
            for i in range(len(ans[-1])-1):
                temp.append(ans[-1][i]+ans[-1][i+1])
            
            temp.append(1)
            ans.append(temp)
        
        return ans