class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def compute(left, right, op):
            if op == '+':
                return left + right
            elif op == '-':
                return left - right
            else:
                return left * right
        
        def helper(s):
            if s.isdigit():
                return [int(s)]
            
            ans = []
            for i in range(len(s)):
                if s[i] in ['+', '-', '*']:
                    left_res = helper(s[:i])
                    right_res = helper(s[i+1:])
                    # print(left_res)
                    # print(right_res)
                    for left in left_res:
                        for right in right_res:
                            temp = compute(left, right, s[i])
                            # print(temp)
                            ans.append(temp)
            
            return ans
        
        return helper(expression)
    
       