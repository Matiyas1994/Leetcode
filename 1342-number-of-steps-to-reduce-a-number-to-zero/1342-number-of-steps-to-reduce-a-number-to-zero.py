class Solution:
    def numberOfSteps(self, num: int) -> int:
        ans = 0
        while num:
            if num & 1 == 0:
                num //=2
            else:
                num -=1
            ans +=1
        return ans
    
#         14 // 2 = 7  
#         7 - 1 = 6
#         6//2 =3
#         3-1 = 2
#         2//2 =1
#         1-1=0
        
#         16 ---8
#         8-----4
#         4-----2
#         2-----1
#         1-----0