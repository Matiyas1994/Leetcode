class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        relation = []
        n = len(nums)
        if n < 2:
            return n
        for i in range(1,n):
            if nums[i] > nums[i-1]:
                relation.append(1)
            elif nums[i] < nums[i-1]:
                relation.append(-1)
        k = len(relation)
        ans = 0
        if not relation:
            return 1
        for j in range(1,k):
            if relation[j] != relation[j-1]:
                ans +=1
        return ans + 2 
        
        