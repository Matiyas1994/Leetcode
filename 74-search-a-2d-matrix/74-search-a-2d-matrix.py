class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bs(lst,target):
            left = 0
            right = len(lst)-1
            
            while left <= right:
                mid = left + (right-left)//2
                if target == lst[mid]:
                    return True
                elif lst[mid] > target:
                    right = mid-1
                else:
                    left = mid+1
        
            return False
        
        def bestRowTosearch(target):
            left = 0
            right = len(matrix)-1
            ans = 0
            
            while left <= right:
                mid = left + (right-left)//2
                
                if matrix[mid][0] <= target:
                    ans = mid
                    left = mid+1
                else:
                    right = mid-1
            return ans
                
                    
        row = bestRowTosearch(target)
        return bs(matrix[row],target)
        
                