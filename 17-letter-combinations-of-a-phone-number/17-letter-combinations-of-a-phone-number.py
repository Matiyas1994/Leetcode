class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        reference = {
            "2" : ["a","b","c"],
            "3" : ["d","e","f"],
            "4" : ["g","h","i"],
            "5" : ["j","k","l"],
            "6" : ["m","n","o"],
            "7" : ["p","q","r","s"],
            "8" : ["t","u","v"],
            "9" : ["w","x","y","z"]
        }
        
        ans = []
        def backtrack(i, ds):
            nonlocal digits
            if i == len(digits):
                ans.append("".join(ds[:]))
                
            else:
                for ch in reference[digits[i]]:
                    ds.append(ch)
                    backtrack(i+1, ds)
                    ds.pop()
        backtrack(0, [])
        return ans 
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

#         def rec(i):
#             if i == len(digits)-1:
#                 return reference[digits[i]]
#             a2 = []
#             for ch in reference[digits[i]]:
#                 temp = rec(i+1)
#                 for t in temp:
#                     a2.append(ch + t)
                    
#             return a2[:]
                 
#         return rec(0)
      
        
   