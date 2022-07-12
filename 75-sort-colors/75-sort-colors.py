class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colorsFreq = [0,0,0]
        
        for n in nums:
            colorsFreq[n] +=1
    
        start = 0
        for i in range(3):
            for j in range(start, start+colorsFreq[i]):
                nums[j] = i
            if colorsFreq[i] > 0: 
                start = j+1 
        