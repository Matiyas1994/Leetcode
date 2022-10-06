class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 1
        j, j2  = 0, 0
        for i in range(1, n):
            if i%2:
                if arr[i] <= arr[i-1]:
                    j = i
                if arr[i] >= arr[i-1]:
                    j2 = i
            else:
                if arr[i] >= arr[i-1]:
                    j = i
                if arr[i] <= arr[i-1]:
                    j2 = i
                    
            ans = max(ans, i-j+1, i-j2+1)
         
        return ans
       
        
        
        
#      [9<4>2<10>7<8>8<1>9]
#      [9>4<2>10<7>8<8>1<9]
          
                    
        
        
#         sign=[]
#         ans = 0
#         for i in range(len(arr)-1):
            
#             if arr[i] < arr[i+1]:
#                 cursign ="<"
#             elif  arr[i] > arr[i+1]:
#                 cursign =">"
#             else:
#                 cursign = "="
        
#             if sign and sign[-1] != cursign and cursign !="=":
#                 sign.append(cursign)
                
#             else:
#                 ans = max(ans,len(sign))
#                 sign = []
#                 if cursign != "=":
#                     sign.append(cursign)
                    
#         ans = max(ans,len(sign))  
#         return ans+1
    
