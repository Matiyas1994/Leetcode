class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pref = 0
        Myhash = {0:-1}
        for i in range(len(nums)):
            pref += nums[i]
            pref %=k
            
            if pref in Myhash:
                if i-Myhash[pref] >=2:
                    return True
            
            else: Myhash[pref] = i
        
        return False
            
        