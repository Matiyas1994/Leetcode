class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergeSort(left,right):
            if left >= right:
                return 0
            mid= left + (right-left)//2
            count = mergeSort(left, mid)
            count += mergeSort(mid+1, right)
            count += Merge(left, right, mid)
            
            return count
        
        def Merge(left,right,mid):
            count = 0
            j = mid + 1
            
            for i in range(left,mid+1):    
                while j <= right and nums[i] > 2*nums[j]:
                    j +=1
                count += j - (mid+1)
            
            
            temp =[]
            firstarrayptr, secondarrptr = left, mid+1
            
            while firstarrayptr <= mid and secondarrptr <= right:
                if nums[firstarrayptr] <= nums[secondarrptr]:
                    temp.append(nums[firstarrayptr])
                    firstarrayptr +=1
                else:
                    temp.append(nums[secondarrptr])
                    secondarrptr +=1
            while firstarrayptr <= mid:
                temp.append(nums[firstarrayptr])
                firstarrayptr +=1
            while secondarrptr <= right:
                temp.append(nums[secondarrptr])
                secondarrptr +=1
            for i in range(left,right+1):
                nums[i] = temp[i - left]
                    
            return count
       
        
        return mergeSort(0,len(nums)-1)
         
            