class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dic = Counter()
        ans = 0
        for i in range(len(time)):
            temp = time[i]%60
            if temp != 0:
                ans += dic[60-temp]
            else:
                ans += dic[0]
                
            dic[temp] +=1
        return ans