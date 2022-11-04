class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic = {0: 1}
        p = 0
        ans = 0
        for num in nums:
            p += num
            if p%k in dic:
                ans += dic[p%k]
         
            dic[p%k] = dic.get(p%k, 0) + 1
        
        return ans
        