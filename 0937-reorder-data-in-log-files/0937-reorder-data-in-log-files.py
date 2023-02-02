class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letterLogs = []
        digitLogs = []
        for log in logs:
            temp = log.split()
            if temp[1].isdigit():
                digitLogs.append(log)
            else:
                letterLogs.append([" ".join(temp[1:]),temp[0]])
        
        letterLogs.sort(key=lambda x: (x[0], x[1]))
        
        for i in range(len(letterLogs)):
            letterLogs[i] = letterLogs[i][1] +" "+ letterLogs[i][0]
        
        letterLogs.extend(digitLogs)
        return letterLogs
        
        
            
        