class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board = ["abcde",
                "fghij",
                "klmno", 
                "pqrst", 
                "uvwxy", 
                "z"]
        def isValidMove(i,j):
            return 0 <= i < 6 and 0 <= j < len(board[i]) 
    
        def bfs(currentPosition, target):
            queue = deque()
            queue.append(currentPosition)
            visited = set()
            visited.add((currentPosition[0],currentPosition[1]))


            directions =[(1,0,'D'),(-1,0,'U'),(0,1,'R'),(0,-1,'L')]

            while queue:
                i, j, path = queue.popleft()
               
             

                if board[i][j] == target:
                    return  (path + "!", (i, j,""))


                for direction in directions:
                    newi, newj, newdir = i + direction[0], j+direction[1], direction[2]

                    if isValidMove(newi, newj) and (newi, newj) not in visited:
                        queue.append((newi, newj, path + newdir))
                        visited.add((newi, newj))

            return 

        currentPosition = (0,0,"")
        ans = ""
        for char in target:
            path, currentLocation = bfs(currentPosition, char)
            ans +=path
            currentPosition = currentLocation

        return ans
