class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # 1+2+10+10+8 =31
        # [[1,3],[2,4],,[8,9],[10,11],[10,12]]
        # min = max(max(second), sum(first))
        # max = sum(first) + sum(second) 
        # [[1,3],[2,4],[8,9],[10,11],[10,12]]
                  # 31
        tasks.sort(key = lambda x: x[0]-x[1])
        def helper(guss):
            for i in range(len(tasks)):
                if guss < tasks[i][1]:
                    return False
                guss -=tasks[i][0]
            
            return True
        # print(helper(32))
        summ = 0
        for actual, minn in tasks:
            summ += actual + minn
        
        right = summ
        left = 0
        ans = right
        while left <= right:
            guss = left + (right - left) // 2
            
            if helper(guss):
                ans = guss
                right = guss - 1
            
            else:
                left = guss + 1
        
        return ans
        