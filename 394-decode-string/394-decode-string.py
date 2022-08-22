class Solution:
    def decodeString(self, s: str) -> str:
#     creating stack
        stack = []
    
#  push elements to the stack until i get ]
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                temp = ""
                # pop() from stack put them in temp
                while stack and stack[-1] != "[":
                    temp = (stack.pop()) + temp
                    
                stack.pop()
                num = "" 
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num 
                
                # i will multiply those value by the i get
                temp = temp * int(num)
                
                # i will push them again to the stack  
                stack.append(temp)
                
        
        return "".join(stack)
                                        
        