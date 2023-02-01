class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white = 0
        for i in range(k):
            if blocks[i]=='W':
                white +=1
        minRecolor = white
        
        for j in range(k, len(blocks)):
            if blocks[j]=='W':
                white +=1
            if blocks[j-k]=='W':
                white -=1
            minRecolor = min(white, minRecolor)
        
        return minRecolor

