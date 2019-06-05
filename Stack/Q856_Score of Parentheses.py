
# 思路: 因为给定的括号串是balanced的，所以每出现一个'('加入一个0，表示此处的括号代表的数，遇到')'时，pop出当前尾部的数，乘2或者变为1，加到上一个尾部数字中去.

class Solution:
    # Solution 1 44 ms
    # def scoreOfParentheses(self, S):
    #     stack=[]
    #     for char in S:
    #         cur=0
    #         if char==')':
    #             if stack[-1]=='(':
    #                 stack.pop(),stack.append(1)
    #             else:
    #                 while stack[-1]!='(': cur+=stack.pop()
    #                 stack.pop(),stack.append(2*cur)
    #         else:
    #             stack.append(char)
    #     return sum(stack)

    # Solution 2 36 ms
    def scoreOfParentheses(self, S):
        stack=[0]
        for char in S:
            if char=='(':
                stack.append(0)
            else:
                num=stack.pop()
                stack[-1]+=2*(num or 0.5)
        return int(stack[0])

a=Solution()
print(a.scoreOfParentheses(""))
print(a.scoreOfParentheses("()"))
print(a.scoreOfParentheses("(())"))
print(a.scoreOfParentheses("()()"))
print(a.scoreOfParentheses("(()(()))"))
print(a.scoreOfParentheses("(()()()()()())"))
print(a.scoreOfParentheses("(()(()(()))()(()))"))