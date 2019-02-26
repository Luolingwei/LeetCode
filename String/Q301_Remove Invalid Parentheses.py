class Solution:
    def is_valid(self,str):
        stack=[]
        for char in str:
            if char=='(':
                stack.append(char)
            if char==')':
                if not stack:
                    return False
                stack.pop()
        return not stack

    def removeInvalidParentheses(self, s):
        set={s}
        while True:
            valid=list(filter(self.is_valid,set))
            if valid: return valid
            set={s[:i]+s[i+1:] for s in set for i in range(len(s))}

a=Solution()
print(a.removeInvalidParentheses(")("))
print(a.removeInvalidParentheses("(a)())()"))
print(a.removeInvalidParentheses("()())()"))