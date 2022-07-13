class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # num1isGreater = True if m >= n else False
        p1, p2, np = m-1, n-1, m+n-1

        while p1 >= 0  and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[np] = nums1[p1]
                p1 -=1
            else:
                nums1[np] = nums2[p2]
                p2 -=1
            np -=1
        
        while p2 >=0:
            nums1[np] = nums2[p2]
            p2 -=1
            np -=1
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         p1 =m-1
#         p2 =n-1
#         i = m+n - 1
        
#         while p1>=0 and p2>=0:
#             if nums1[p1] > nums2[p2]:
#                 nums1[i] = nums1[p1]
#                 p1, i = p1-1, i-1
                
#             else:
#                 nums1[i] = nums2[p2]
#                 p2, i = p2-1, i-1
            
        
#         while p2 >= 0:
#             nums1[i] = nums2[p2]
#             p2, i = p2-1, i-1
            
        
        
#################################################################
        # k=0
        # for i in range(m,m+n):
        #     nums1[i]=nums2[k]
        #     k+=1
        # nums1.sort()
        
#####################################################################        
#         c = []
#         p1 = 0
#         p2 = 0
        
#         while p1 < m and p2 < n:
#             if nums1[p1] <= nums2[p2]:
#                 c.append(nums1[p1])
#                 p1 +=1
#             else:
#                 c.append(nums2[p2])
#                 p2 +=1
#         if p1 < m:
#             c.extend(nums1[p1:m])
#         if p2 < n:
#             c.extend(nums2[p2:n])
            
#         for i in range(m+n):
#             nums1[i] = c[i]
            
        

        
        