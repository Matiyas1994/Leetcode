class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        def backtracking(CurTarget, temp, start):
            if CurTarget==0:
                ans.append(temp[:])
            
            else:
                for i in range(start, len(candidates)):
                    if CurTarget - candidates[i]  >= 0:
                        temp.append(candidates[i])
                        backtracking(CurTarget - candidates[i], temp, i)
                        temp.pop()
                    
        backtracking(target, [], 0)
        return ans
                        
        
        