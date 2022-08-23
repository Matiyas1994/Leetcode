class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans =0
        while maxDoubles > 0 and target > 1:
            ans += 1 +  target%2
            target //=2
            maxDoubles -=1
            
        return (target - 1) + ans
        