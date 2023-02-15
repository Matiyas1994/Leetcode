class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber <= 0:
            return ''
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ans = ''
        base = 0    
        while columnNumber > 0:
            tmp = int(columnNumber / (26 ** base))    ## everytime first devided by 26^base
            val = tmp % 26
            if val == 0:
                char = 'Z'
                columnNumber = columnNumber - 26*(26**base)
            else:
                char = alphabet[val-1]
                columnNumber = columnNumber - val*(26**base)
            ans = char + ans
            base += 1
        return ans
