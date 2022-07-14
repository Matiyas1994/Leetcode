class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) * len(matrix[0]) - 1
        n = len(matrix[0])
        while left <= right:
            mid = left + (right-left)//2
            if target == matrix[mid//n][mid%n]:
                return True
            elif matrix[mid//n][mid%n] > target:
                right = mid-1
            else:
                left = mid+1

        return False
        
      
                