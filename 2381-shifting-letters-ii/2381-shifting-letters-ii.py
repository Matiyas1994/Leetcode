class Solution:
    def shiftingLetters(self, word: str, shifts: List[List[int]]) -> str:
        arr = [0]*(len(word)+1)
        alphabet ="abcdefghijklmnopqrstuvwxyz"
        dic = {alphabet[i]:i for i in range(len(alphabet))}
        
        for s,e,d in shifts:
            if d:
                arr[s] +=1
                arr[e+1] -=1
            else:
                arr[s] -=1
                arr[e+1] +=1
        
        word = list(word)
        t = 0
        for i in range(len(word)):
            t += arr[i]
            word[i]=alphabet[(dic[word[i]]+t)%26]
            
        return "".join(word)
            
                