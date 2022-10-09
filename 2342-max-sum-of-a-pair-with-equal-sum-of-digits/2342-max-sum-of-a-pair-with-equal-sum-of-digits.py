class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        # [9,7,9,4,7]
        # 9:[18,36,81]
        # 7:[43,7]
            
        def digitadder(n):
            s = 0
            while n:
                s += n%10
                n //=10
            return s
        
            
        dic = []
        
        for num in nums:
            ds = digitadder(num)
            dic.append((ds,num))
        
        dic.sort()

        ans = -1
        j, i = 0, 1
        while i < len(dic):
            if dic[i][0]==dic[i-1][0]:
                j = i-1
        
                while i < len(dic) and dic[i][0]==dic[j][0]:
                    i +=1
                    j +=1
            
                ans = max(ans, dic[i-1][1]+dic[j-1][1])
            i +=1
            
        return ans
                    
            
         
            
        
            