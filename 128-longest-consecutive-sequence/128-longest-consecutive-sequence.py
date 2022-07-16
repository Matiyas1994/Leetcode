class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        MaxxLength = 0
        foundInNums = set(nums)
        noneed = set()
        
        for num in foundInNums:
            if num not in noneed:
                t = num+1 
                while  t in foundInNums:
                    noneed.add(t)
                    t +=1
                MaxxLength = max(MaxxLength, t-num) 

        return MaxxLength 
        