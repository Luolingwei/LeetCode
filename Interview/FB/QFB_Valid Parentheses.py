class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dic={')':'(',']':'[','}':'{'}
        for c in s:
            if c in ')]}':
                if not stack:
                    return False
                if dic[c]!=stack.pop():
                    return False
            else:
                stack.append(c)
        return not stack

a=Solution()
print(a.isValid("()[]{}"))
print(a.isValid("(]"))
print(a.isValid("([)]"))
print(a.isValid("{[]}"))