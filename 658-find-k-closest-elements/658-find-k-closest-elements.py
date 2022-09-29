class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        pq= []
        ans = []
        for num in arr:
            heapq.heappush(pq,(abs(num-x),num))
        for i in range(k):
            ans.append(heapq.heappop(pq)[1])
            
        return sorted(ans)
        
        
        
#         L, R =0, len(arr)-1
#         Lans = 0
# #         maximum of numbers which is <= target
#         while L<=R:
#             mid = L + (R-L)//2
#             if arr[mid] <= x:
#                 Lans = mid
#                 L = mid + 1
#             else:
#                 R = mid - 1
                
#         L, R =0, len(arr)-1
#         Rans = R
#         # min of numbers which is >=target
#         while L<=R:
#             mid = L + (R-L)//2
#             if arr[mid] >=x:
#                 Rans = mid
#                 R = mid - 1
#             else:
#                 L = mid + 1
        
#         for i in range(k):
#             if 0 <=Lans and Rans <= len(arr) - 1:
#                 Ldif = abs(arr[Lans] - x)
#                 Rdif = abs(arr[Rans] - x)
#                 if Ldif < Rdif :
#                     Lans -=1
#                 elif Rdif < Ldif:
#                     Rans +=1
#                 else:
#                     if Lans == Rans:
#                         Lans -=1
#                         Rans +=1
#                     else:
#                         Lans -=1
#             elif Lans < 0:
#                 Rans += k - i
#                 break;
#             else:
#                 Lans -= k - i
#                 break;
                    
#         return arr[Lans+1:Rans] 
        