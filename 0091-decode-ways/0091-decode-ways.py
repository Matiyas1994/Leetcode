class Solution:
    def numDecodings(self, s: str) -> int:
        
        @cache
        def f(i):
            if i>=len(s):
                return 1
            
            if s[i]=="0":
                return 0
                
            goOne = f(i+1)  
            goTwo = 0
            
            if i+2 <= len(s) and 1<=int(s[i:i+2])<=26: 
                goTwo = f(i+2) 
            
            return  goOne + goTwo
        
        return f(0)
            
                