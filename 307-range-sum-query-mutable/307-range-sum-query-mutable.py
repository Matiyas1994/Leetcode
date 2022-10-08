class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.nums = nums
        self.seg = [0]*(4*n)
        self.build(0,n-1,0)
        
        

    def update(self, index: int, val: int) -> None:
        n = len(self.nums)
        self.updateSeg(0,n-1,0,val,index)
        self.nums[index]=val
        
        

    def sumRange(self, left: int, right: int) -> int:
        n = len(self.nums)
        return self.query(left,right,0,n-1,0)
    
    def build(self,low,high,idx):
        if low==high:
            self.seg[idx] = self.nums[low]
            return 
            
        mid = low + (high-low)//2
        
        self.build(low, mid, (2*idx)+1)
        self.build(mid+1, high, (2*idx)+2)
        
        self.seg[idx] = self.seg[(2*idx)+1] + self.seg[(2*idx)+2]
    
    def updateSeg(self, low, high, idx, val, i):
        if low==high:
            self.seg[idx] = val
            return
        
        mid = low + (high-low)//2
        
        if  i <= mid: self.updateSeg(low, mid, (2*idx)+1, val, i)
        else: self.updateSeg(mid+1, high, (2*idx)+2, val, i)
            
        self.seg[idx] = self.seg[(2*idx)+1] + self.seg[(2*idx)+2]
        
    def query(self, l, r, low, high, idx):
        if low > r or high < l: 
            return 0
        
        if low >= l and high<=r: 
            return self.seg[idx]
        
        mid = low + (high-low)//2
        
        left  = self.query(l, r, low, mid, (2*idx)+1)
        right = self.query(l, r, mid+1, high, (2*idx)+2)

        return left + right
        
        
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)