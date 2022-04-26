class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = [i for i in range(len(accounts))] 
        rank = [1 for li in accounts]
        
        def find(email):
            if parent[email] == email:
                return email
            parent[email] = find(parent[email])
            return parent[email]
    
        
        def union(i,j):
            pi = find(i)
            pj = find(j)
            
            if pi != pj:
                if rank[pi] > rank[pj]:
                    parent[pj] = pi
                    rank [pj] += rank[pi]
                else:
                    parent[pi] = pj
                    rank[pi] += rank[pj]
                                   
        emailtoParent = {}
        for i in range(len(accounts)): 
            for j in range(1,len(accounts[i])):
                if accounts[i][j] in  emailtoParent:
                    union(i,emailtoParent[accounts[i][j]])
                
                else:
                    emailtoParent[accounts[i][j]] = find(i)
                  
        mergeddict= defaultdict(set)
        for i,p in enumerate(parent):
            mergeddict[find(p)].update(accounts[i][1:])
        
        res = []
        for key,val in mergeddict.items():
            t = [accounts[key][0]]
            for semail in sorted(list(val)):
                t.append(semail)
            res.append(t)
        
        return res

        
