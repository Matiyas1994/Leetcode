class Solution:
    def countPrimes(self, n: int) -> int:
        nums = [1] * (n)
        if n < 2:
            return 0
        
        for i in range(2,int(math.sqrt(n))+1):
            if nums[i]:
                for j in range(i**2, n, i):
                    nums[j] = 0
        
        return sum(nums)-2
        
        