class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def par(o,c,ds,i):
            nonlocal n
            if o ==0 and c==0:
                ans.append("".join(ds[:]))
                return 
            if i < 0:
                return 
            
            if i!=(2*n)-1 and o>c and o > 0:
                ds[i] = "("
                par(o-1,c,ds,i-1)
            if i!=0 and c > 0:
                ds[i] = ")"
                par(o,c-1,ds,i-1)
        ds = [0]*(2*n)
        par(n,n,ds,(2*n)-1)
        return ans