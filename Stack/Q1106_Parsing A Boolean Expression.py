# Input: expression = "|(&(t,f,t),!(t))"
# Output: false

# 思路: 用stack模拟入栈过程.

class Solution:
    def parseBoolExpr(self, expression):
        stack=[]
        for char in expression:
            if char==')':
                t,f=0,0
                while stack[-1]!='(':
                    c=stack.pop()
                    if c=='t':t+=1
                    if c=='f':f+=1
                stack.pop()
                symbol=stack.pop()
                if symbol=='&':
                    if f!=0: stack.append('f')
                    else: stack.append('t')
                if symbol=='|':
                    if t!=0: stack.append('t')
                    else: stack.append('f')
                if symbol=='!':
                    if t!=0: stack.append('f')
                    else: stack.append('t')
            else:
                stack.append(char)
        return stack[-1]=='t'

a=Solution()
print(a.parseBoolExpr("|(&(t,f,t),!(t))"))
print(a.parseBoolExpr("&(t,f)"))
print(a.parseBoolExpr("|(f,t)"))
print(a.parseBoolExpr("!(f)"))