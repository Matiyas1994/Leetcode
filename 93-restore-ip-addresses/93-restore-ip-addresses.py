class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # 25525511135
        # 012345678910
#         ans = []
#         for i in range(len(s)-9,len(s)-6):
#             for j in range(len(s)-6, len(s)-3):
#                 for k in range(len(s)-3, len(s)):
#                     if 0<= int(s[:i]) <= 255 and 0<= int(s[i:j]) <=255 and 0<=int(s[j:k])<=255:
#                         ans.append(s[:i]+"."+s[i:j]+"."+s[j:k])
                    
#         return ans
        if len(s) < 4 or len(s) > 12: return [] 
        ans = []
        def putdots(rd, path,lp):
            if rd == 0:
                li = path.split(".")
                for num in li:
                    if  int(num) !=0 and num[0]=='0': 
                        return 
                    if int(num)==0 and len(num)>1:
                        return 
                        
                    if not num.isdigit() or int(num) > 255:
                        return

                ans.append(path)
                return

            for i in range(lp ,len(path)):
                path2 = path[:i]+"."+path[i:]
                putdots(rd-1, path2, i+2)

        putdots(3,s,1)
        return ans        





