class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        twoNumbers = 0
        
        for num in nums:
            twoNumbers ^= num
        
        i = 0
        while not (twoNumbers & 1<<i):
            i +=1
        
        x = 1<<i
        
        num1, num2 = 0 , 0
        for num in nums:
            if num & x:
                num1 ^=num
            else:
                num2 ^=num
        
        return [num1, num2]
            
        