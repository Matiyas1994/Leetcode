class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0, 0
        begin = True
        while fast != slow or begin:
            fast = nums[nums[fast]]
            slow = nums[slow]
            begin = False
        
        slow = 0
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]

        return fast
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         slow = 0
#         fast = 0
#         slow = nums[slow]
#         fast = nums[nums[fast]]
        
#         while slow != fast:
#             slow = nums[slow]
#             fast = nums[nums[fast]]
        
#         slow = 0
#         while nums[slow] != nums[fast]:
#             slow = nums[slow]
#             fast = nums[fast]
        
#         return nums[fast] 