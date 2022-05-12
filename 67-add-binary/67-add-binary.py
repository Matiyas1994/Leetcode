class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = []
        cary = "0" 
        if len(a) > len(b):
            b = "0"* (len(a) - len(b)) + b
        elif len(b) > len(a):
            a = "0"* (len(b) - len(a)) + a        
        
        pa = len(a)- 1
        pb = len(b) - 1
        
        while pa >= 0 or pb >= 0:
            if a[pa] == b[pb] =="1":
                if cary == "1":
                    ans.append("1")
                    cary = "1" 
                else:
                    ans.append("0")
                    cary = "1"
            elif a[pa] == b[pb] == "0":
                if cary == "1":
                    ans.append("1")
                    cary = "0"
                else:
                    ans.append("0")
                    cary = "0"
            elif a[pa] == "0" or b[pb] == "0":
                if cary == "1":
                    ans.append("0")
                    carry = "1"
                else:
                    ans.append("1")
                    cary = "0"
            
            
            pa -=1
            pb -=1
            
        if cary == "1":
            ans.append(cary)
        return "".join(reversed(ans))
        
        
        
        