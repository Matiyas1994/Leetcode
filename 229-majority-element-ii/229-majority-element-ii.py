class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        limit = n//3
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0
        
        for num in nums:
            if candidate1 !=None and candidate1 == num:
                count1 +=1
            elif candidate2 !=None and  candidate2 == num:
                count2 +=1
            elif count1==0:
                candidate1 = num
                count1 = 1
            elif count2==0:
                candidate2 = num
                count2 = 1
            else:
                count1 -=1
                count2 -=1
                
        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1:
                count1 +=1
            elif num == candidate2:
                count2 +=1
        ans = []
        if count1 > limit:
            ans.append(candidate1)
        if count2 > limit:
            ans.append(candidate2)
        return ans
        
        