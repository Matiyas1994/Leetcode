class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = []
        nums.sort()
        
        for i in range(n-3):
            if i == 0 or nums[i] != nums[i-1]:
                for j in range(i+1,n-2):
                    if j==i+1 or nums[j] != nums[j-1]:  
                        cur_target = target - (nums[i] + nums[j])
                        low, high = j+1, n-1

                        while low < high:
                            cur_sum = nums[low] + nums[high]
                            if cur_sum < cur_target:
                                low +=1
                            elif cur_sum > cur_target:
                                high -=1
                            else:
                                ans.append([nums[i],nums[j],nums[low],nums[high]])
                                while low < high and nums[low] == nums[low+1]:
                                    low +=1
                                while low < high and nums[high] == nums[high-1]:
                                    high -=1
                                low +=1
                                high -=1
        return ans
        
        
        
        
        
        
        
        # ans = []
        # n = len(nums)
        # st = set()
        # for i in range(n):
        #     for j in range(i+1,n):
        #         for k in range(j+1,n):
        #             for ll in range(k+1,n):
        #                 if nums[i]+nums[j]+ nums[k]+ nums[ll] == target:
        #                     if(nums[i],nums[j],nums[k],nums[ll]) not in st:
        #                         ans.append([nums[i],nums[j],nums[k],nums[ll]])
        #                         st.add((nums[i],nums[j],nums[k],nums[ll]))
        # return ans