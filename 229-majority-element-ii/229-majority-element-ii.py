class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0
        
        for num in nums:
            if candidate1 != None and num == candidate1:
                count1 +=1
            elif candidate2 != None and num == candidate2:
                count2 +=1
            
            elif count1 == 0:
                candidate1 = num
                count1 +=1
            elif count2 == 0:
                candidate2 = num
                count2 +=1
            else:
                count1 -=1
                count2 -=1
        
        limit = len(nums)//3
        res = []
        count1, count2 =0, 0
        for num in nums:
            if num == candidate1:
                count1 +=1
            elif num == candidate2:
                count2 +=1
            
        if count1 > limit:
            res.append(candidate1)
        if count2 > limit:
            res.append(candidate2) 
        
        return res
                
                
            
        
         