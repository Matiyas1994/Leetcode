class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        OneLine = []
        numOfcharSoFar = 0
        ans = []
        
        for word in words:
            spacesSoFar = numOfwords = len(OneLine)
            lengthIfAdded = numOfcharSoFar + spacesSoFar + len(word)
            
            if lengthIfAdded > maxWidth:
                spaces = maxWidth - numOfcharSoFar
                i = 0
                spacePositions =  numOfwords - 1
                while spaces > 0:
                    OneLine[i] += ' '
                    spaces -= 1
                    if numOfwords > 1:
                        i =  (i+1) % spacePositions
                    
                ans .append(''.join(OneLine))
                OneLine, numOfcharSoFar = [], 0
            
            OneLine.append(word)
            numOfcharSoFar += len(word)
        
        ans.append(' '.join(OneLine))        
        remainingSpace = maxWidth - numOfcharSoFar - (len(OneLine)-1)
        ans[-1] += ' '*remainingSpace
        return ans