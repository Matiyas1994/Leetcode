class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            
            else:
                temp = []
                while stack and not stack[-1].isdigit():
                    ch = stack.pop()
                    if ch !='[':
                        temp.append(ch)
                    
                multiplyFactor = 1    
                if stack:
                    t = ""
                    while stack and stack[-1].isdigit():
                        t +=stack[-1]
                        stack.pop()
                    multiplyFactor = int(t[::-1])
                    
                
                stack.extend(temp[::-1]*multiplyFactor)
        
        return "".join(stack)
                
                
            
        
        