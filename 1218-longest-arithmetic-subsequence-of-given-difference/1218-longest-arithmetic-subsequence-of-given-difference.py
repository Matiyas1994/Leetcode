class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        leftOfCurElement = {}
        n = len(arr)
        ans = 1
        
        for i in range(n):
            if (arr[i] - difference) in leftOfCurElement:
                leftOfCurElement[arr[i]] = leftOfCurElement[ arr[i] - difference] + 1
                ans = max(ans, leftOfCurElement[arr[i]])
            else:
                leftOfCurElement[arr[i]] = 1 
                
        return ans
        
        
        
        