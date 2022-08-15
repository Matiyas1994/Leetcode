class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        d = set()
        for i in range(len(nums)):
            c = 0
            for j in range(i,len(nums)):
                if nums[j]%p==0:
                    c +=1
                    if c <= k:
                        d.add(tuple(nums[i:j+1]))
                    else:
                        break
                elif c <= k:
                    d.add(tuple(nums[i:j+1]))
                
                   
        return len(d)
    