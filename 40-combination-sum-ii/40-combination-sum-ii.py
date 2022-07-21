class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        
        def backtracking(start=0, curTarget=target, temp=[]):
            if curTarget == 0:
                ans.append(temp[:])
            
            else:
                for i in range(start, len(candidates)):
                    if i > start and candidates[i] == candidates[i-1]: continue
                    if curTarget - candidates[i] >=0:
                        temp.append(candidates[i])
                        backtracking(i+1, curTarget - candidates[i], temp)
                        temp.pop()
                        
        backtracking()
        return ans