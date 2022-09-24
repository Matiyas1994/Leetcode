class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        A = []
        for f,l,s in bookings:
            A.append([f,s])
            A.append([l+1,-s])
        ans = []
        total = 0
        A.sort()
        j=0
        for i in range(n):
            while j < len(A) and i+1 == A[j][0]:
                total +=A[j][1]
                j +=1
            ans.append(total)
            
        return ans