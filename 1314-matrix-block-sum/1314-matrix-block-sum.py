class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        answer = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        def generate(i,j,k):
            validrow = []
            validcol = []
            
            for i in range(max(0,i-k), min(i+k+1, len(mat))):
                validrow.append(i)
            for j in range(max(0,j-k), min(j+k+1, len(mat[0]))):
                validcol.append(j)
                
            return (validrow, validcol)
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                validrow, validcol = generate(i,j,k)
                summ = 0
                for row in validrow:
                    for col in validcol:
                        summ +=mat[row][col]
                
                answer[i][j] = summ
                
        return answer
        