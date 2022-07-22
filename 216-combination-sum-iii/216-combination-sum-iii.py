class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        def backtrack(target=n, start=1, temp=[]):
            if target==0 and len(temp)==k:
                ans.append(temp[:])
                
            else:
                for i in range(start, 10):
                    if target - i >=0 and len(temp)<k:
                        temp.append(i)
                        backtrack(target - i, i+1, temp)
                        temp.pop()
                        
        ans = []
        backtrack()
        return ans
                        
                      