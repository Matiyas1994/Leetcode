class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m=len(grid)
        n=len(grid[0])
        key_cnt=0
        start=()
        queue=collections.deque()
        visited={}
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='@':
                    start=(i,j)
                if grid[i][j] in 'abcdef':
                    key_cnt+=1

        queue.append(('',start[0],start[1]))
        visited[('',start[0],start[1])]=0
        while queue:
            key,x,y=queue.popleft()
            step=visited[(key,x,y)]
            if len(key)==key_cnt:
                return step
            for i,j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                    if 0<=i<m and 0<=j<n:
                        cell=grid[i][j]
                        if cell=='#':
                            continue
                        elif cell.isupper() and cell.lower() not in key:
                            continue
                        elif cell.islower():
                            new_key=''.join(sorted(cell+key)) if cell not in key else key
                            if visited.get((new_key,i,j),math.inf)<=step+1:
                                continue
                            queue.append((new_key,i,j))
                            visited[(new_key,i,j)]=step+1
                        elif visited.get((key,i,j),math.inf)>step+1:
                            queue.append((key,i,j))
                            visited[(key,i,j)]=step+1
        return -1
