class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         def colFindFor(targ):
#             left, right = 0, len(matrix)
#             ans = right
#             while left<=right:
#                 mid = left + (right-left)//2
                
#                 if matrix[mid][0] <= targ:
#                     ans = mid
#                     left = mid+1
#                 else:
#                     right = mid-1
            
#             return ans
        def bs (row, targ):
            left, right = 0, len(matrix[0])-1
            
            while left<=right:
                mid = left + (right-left)//2
                
                if matrix[row][mid] == targ:
                    return True
                
                elif matrix[row][mid] > targ:
                    right = mid-1
                else:
                    left = mid+1
                          
            return False
        
        
        if matrix[0][0] <= target <= matrix[-1][-1]:
            for row in range(len(matrix)):
                if bs(row, target): return True
            
            return False
        else:
            return False
        
        
      