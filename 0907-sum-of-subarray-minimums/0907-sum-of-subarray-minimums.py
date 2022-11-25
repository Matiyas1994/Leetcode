class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mostack = []
        ans = 0
        mod = 10**9 + 7
        n = len(arr)
        for i in range(n):
            while mostack and arr[mostack[-1]] >= arr[i]:
                idx = mostack.pop()
                if mostack:
                    ans += (i-idx)*(idx-mostack[-1])*arr[idx]  
                else:
                    ans += (idx+1)*(i-idx)*arr[idx]
                    
            mostack.append(i)
            
        for j in range(len(mostack)):
            if j==0:
                ans += (mostack[j]+1)*(n-mostack[j])*arr[mostack[j]]
            else:
                ans += (mostack[j]-mostack[j-1])*(n-mostack[j])*arr[mostack[j]]
        
        return ans%mod
    