class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        memo = {}
        def helper(cm,cn,rmove):
            nonlocal n,m
            if (cm,cn,rmove) in memo:
                return memo[(cm,cn,rmove)]
            if cm < 0 or cm >= m or cn < 0 or cn>=n:
                return 1
            if rmove <= 0:
                return 0
            
            d = helper(cm+1,cn,rmove-1)
            u = helper(cm-1,cn,rmove-1)
            l = helper(cm,cn+1,rmove-1)
            r = helper(cm,cn-1,rmove-1)
            
            memo[(cm,cn,rmove)] = d+u+l+r
            return memo[(cm,cn,rmove)]
            
        return helper(startRow, startColumn, maxMove) % 1000000007
            
            