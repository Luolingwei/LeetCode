class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic={'(':')','{':'}','[':']'}
        stack=[]
        for char in s:
            if char in '({[':
                stack.append(char)
            if char in ')}]':
                if not stack or dic[stack.pop()]!=char:
                    return False
        return not stack

a=Solution()
print(a.isValid("()[]{}"))
print(a.isValid("([)]"))
print(a.isValid("{[]}"))
print(a.isValid("(({["))
print(a.isValid(")]}"))
print(a.isValid("()["))
