class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def helper(gussedWeight, dayShouldBe):
            days = 1 
            weight_so_far = 0
            
            for i in range(len(weights)):
                if weight_so_far + weights[i]  <= gussedWeight:
                     weight_so_far += weights[i]
                        
                else:
                    days +=1
                    weight_so_far = weights[i]
            return days <=  dayShouldBe
        
        low, high= max(weights), sum(weights)
        ans = high
        while low<=high:
            mid = low + (high-low)//2
            
            if helper(mid, days):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        
        return ans