class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxFromLeft = [height[0]] * n
        maxFromRight = [height[-1]] * n
        
        for i in range(1,n):
            maxFromLeft[i] = max(maxFromLeft[i-1], height[i])
        
        for j in range(n-2, -1,-1):
            maxFromRight[j] = max(maxFromRight[j+1], height[j])
        ans = 0
        for i in range(n):
            ans += min(maxFromLeft[i], maxFromRight[i]) - height[i]
        
        return ans
            
        
        