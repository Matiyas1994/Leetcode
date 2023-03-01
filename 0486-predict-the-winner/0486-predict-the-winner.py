class Solution:
    def PredictTheWinner(self, arr: List[int]) -> bool:
        
        def f(l,r,p1):
            if l==r:
                if p1:
                    return [arr[l], 0]
                return [0,arr[r]]
            
            if p1:
                right = f(l,r-1,not p1)
                right[0] += arr[r]
                left = f(l+1, r, not p1)
                left[0] +=arr[l]
                if right[0] >= left[0]:
                    return right
                return left
            else:
                right = f(l, r-1, not p1)
                right[1] += arr[r]
                left = f(l+1, r, not p1)
                left[1] +=arr[l]
                if right[1] >= left[1]:
                    return right
                return left
                
        final = f(0, len(arr)-1, True)
        return final[0] >= final[1]
                
        