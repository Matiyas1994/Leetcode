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
        

        
        def rec(i):
            if i == len(digits)-1:
                return reference[digits[i]]
            a2 = []
            for ch in reference[digits[i]]:
                temp = rec(i+1)
                for k,t in enumerate(temp):
                    a2.append(ch + t)
                    
            return a2[:]
            
        
        return rec(0)
            
        
    #         def dfs(start,i,temp):
#             temp.append(start)
#             if i == len(digits)-1:
#                 ans.append("".join(temp[:]))
#                 return 
           
#             for ch in adjlist[start]:
#                 dfs(ch,i+1,temp[:])
        
        
#         for start in reference[digits[0]]:
#             dfs(start,0,[])
        
#         adjlist = defaultdict(list)
#         for i in range(len(digits)-1):
#             for char in reference[digits[i]]:
#                 # if char not in adjlist:
#                 adjlist[char] = reference[digits[i+1]]
#                 # else:
#                      # adjlist[char] += reference[digits[i+1]]
#         print(adjlist)
#         ans = []
        
        