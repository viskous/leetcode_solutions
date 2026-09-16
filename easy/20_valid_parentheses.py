class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        top  = None
        brackets = {")": "(", "}": "{","]" : "[" }

        for brac in s:
            if brac in brackets:
                if top == brackets[brac]:
                    stack.pop()
                else:
                    return False
                if len(stack) > 0:
                    top  = stack[-1]
                else:
                    top = None
                    
            else:
                stack.append(brac)
                if len(stack) > 0:
                    top  = stack[-1]
                else:
                    top = None
            
        return len(stack) == 0
            
        
