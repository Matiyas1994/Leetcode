class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        l, r = 0, buckets
        T = (minutesToTest//minutesToDie)+1
        ans = buckets
        while l<=r:
            mid = l + (r-l)//2
            if pow(T, mid) >= buckets:
                ans = mid
                r = mid-1
            else:
                l +=1
        
        return ans
            
        
        