class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = {('L','L'):'D',
                    ('L','R'):'U',
                    ('R','L'):'U',
                    ('R','R'):'D',
                    ('U','L'):'L',
                    ('U','R'):'R',
                    ('D','L'):'R',
                    ('D','R'):'L'}
        prevDir = 'U'
        position = [0,0]
        for d in instructions:
            if d !='G':
                prevDir = direction[(prevDir,d)]
            else:
                if prevDir == 'U':
                    position[0] -=1
                elif prevDir =='D':
                    position[0] +=1
                elif prevDir =='L':
                    position[1] -=1
                else:
                    position[1] +=1
        
        return (position==[0,0] and prevDir=='U') or (prevDir!='U')
        