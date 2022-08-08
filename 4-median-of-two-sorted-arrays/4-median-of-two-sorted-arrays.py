class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        if n2 < n1 : return self.findMedianSortedArrays(nums2, nums1)
        low, high = 0, n1
        
        while low<=high:
            cut1 = low + (high-low)//2
            cut2 = ((n1+n2+1)//2) - cut1 
            
            left1 =  float("-inf") if cut1==0 else nums1[cut1-1]
            left2 =  float("-inf") if cut2==0 else nums2[cut2-1]
            right1 = float("inf") if cut1==n1 else nums1[cut1]
            right2 = float("inf") if cut2==n2 else nums2[cut2]
            
            if left1 <= right2 and left2 <= right1:
                # print(left1, left2, right1, right2)
                if (n1+n2)%2:
                    return max(left1,left2)
                else:
                    return (max(left1,left2) + min(right1, right2))/2
                
            elif left1 > right2:
                high = cut1 - 1
                
            else:
                low = cut1 + 1
        
                
        
                
        
        
        
        
        
  