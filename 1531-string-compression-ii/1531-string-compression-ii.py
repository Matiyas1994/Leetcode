class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        N=len(s)
        if N==k:
            return 0
        @lru_cache(None)
        def dp(last,count,i,left):
            if i==N:
                return 0
            min_run_length=float(inf)
            if last!=-1 and s[i]==last:
                score=0
                if count<=1 or count+1==10 or count+1==100:
                    score=1
                    
                min_run_length=min(min_run_length,dp(last,count+1,i+1,left)+score)
                if left>=1:
                    min_run_length=min(min_run_length,dp(last,count,i+1,left-1))
                    
            else:
                min_run_length=min(min_run_length,dp(s[i],1,i+1,left)+1)
                if left>=1:
                    min_run_length=min(min_run_length,dp(last,count,i+1,left-1))
                    
            return min_run_length
        
        return dp(-1,0,0,k)