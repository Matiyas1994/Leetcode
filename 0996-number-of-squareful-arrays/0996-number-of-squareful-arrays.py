class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        @cache
        def isPerfectSquare(x):
            sr = int(math.sqrt(x))
            return (sr*sr) == x
        

        ans = 0
        @cache
        def dp(prev, lenn, s):
            nonlocal ans
            if lenn == len(nums): 
                ans += 1
                return

            for i in range(len(nums)):
                if nums[i] > -1 and (prev == None or isPerfectSquare(nums[i] + prev)):
                    temp = nums[i]
                    nums[i] = -1
                    dp(temp, lenn + 1, s + f"{temp}-")
                    nums[i] = temp

        dp(None, 0, '')
        return ans