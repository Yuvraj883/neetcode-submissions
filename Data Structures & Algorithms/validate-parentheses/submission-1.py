class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        
        stack = []

        
        for i in range(0,len(s)):
            ch = s[i]
            if ch in ['{', '[', '(']:
                stack.append(ch)
            
            elif not stack and ch in ['}', ']', ')']:
                return False
            
            elif ((ch == '}' and stack[-1]=='{') or (ch==']' and stack[-1]=='[') or (ch==')' and stack[-1]=='(')):
                stack.pop()
            else :
                stack.append(ch)
        
        return True if len(stack)==0 else False
            