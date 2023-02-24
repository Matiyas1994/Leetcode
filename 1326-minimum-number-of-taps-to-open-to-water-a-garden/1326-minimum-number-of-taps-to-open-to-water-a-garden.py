class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        """
        class Solution {
public:
    int minTaps(int n, vector<int>& r) {
        vector<vector<int>> a;
		//Take out the ranges from each index and sort them on the basis of leftmost point
        for(int i=0;i<r.size();i++){
            int x=max(0,i-r[i]);
            int y=min(n,i+r[i]);
            a.push_back({x,y});
        }
        sort(a.begin(),a.end());
      
        int st=0,end=0,ans=1;
        // Try to reach to maximum index to right which contains current end point i.e "st" and keep on updating variable "end" till which you can already reach from current answer count
        for(int i=0;i<=n;i++){
            if(st>=a[i][0]){
                end=max(end,a[i][1]);
            }
            else{
			//check if already reached to target
                if(end>=n){
                    return ans;
                }
				//as we have sorted our array ,below condition means we have a gap which implies no solution 
                if(end<a[i][0]){
                    return -1;
                }
				//We haven't processes this index so to process it in next iteration 
                i--;
				//increment the answer
                ans++;
				//For the next iteration, update st
                st=end;
            }
        }
        if(end<n)
            return -1;
        return ans;
        
    }
};
        """
        
        realRange = []
        
        for i in range(len(ranges)):
            leftBound = max(0, i-ranges[i])
            rightBound = min(n,i+ranges[i])
            realRange.append([leftBound, rightBound])
        
        realRange.sort()
        # print(realRange)
        start= 0
        end = 0
        taps = 1
        i = 0
        while i <= n:
            leftBound, rightBound = realRange[i]
            if end >= n:
                break
            if start >= leftBound:
                end = max(rightBound, end)
            elif end < leftBound:
                return -1
            else:
                start = end
                taps +=1
                i -=1
                
            i +=1
    
        return taps if end >=n else -1
                
        