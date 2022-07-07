class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        limit = len(nums)//2
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 0
            dic[num] +=1
            if dic[num] > limit:
                return num
   
                