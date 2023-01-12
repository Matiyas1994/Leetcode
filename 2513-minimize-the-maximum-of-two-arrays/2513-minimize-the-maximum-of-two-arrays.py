class Solution:
    def minimizeSet(self, D1: int, D2: int, C1: int, C2: int) -> int:
        
        L, R, G = 0, 10**10, lcm(D1, D2)

        while L < R:
            
            M = (L+R)//2               
            
            x = M - M//D1 >= C1        
            y = M - M//D2 >= C2        
            z = M - M//G  >= C1 + C2               
            if x and y and z : R = M    
            else: L = M+1  
        return L