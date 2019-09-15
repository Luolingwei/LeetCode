# Input: s = "(ed(et(oc))el)"
# Output: "leetcode"

# 思路: 经典stack做法

class Solution:

    # Solution 1 用'('作为判断符号
    # def reverseParentheses(self, s):
    #     stack=[]
    #     for c in s:
    #         if c==')':
    #             temps=''
    #             while stack[-1]!='(':
    #                 temps+=stack.pop()[::-1]
    #             stack.pop()
    #             stack.append(temps)
    #         else:
    #             stack.append(c)
    #     return ''.join(stack)

    # Solution 2 用一个新的''代替'('作为分隔符
    def reverseParentheses(self, s):
        stack=['']
        for c in s:
            if c=='(':
                stack.append('')
            elif c==')':
                add=stack.pop()[::-1]
                stack[-1]+=add
            else:
                stack[-1]+=c
        return ''.join(stack)


a=Solution()
print(a.reverseParentheses(""))
print(a.reverseParentheses("(abcd)"))
print(a.reverseParentheses("(u(love)i)"))
print(a.reverseParentheses("(ed(et(oc))el)"))
print(a.reverseParentheses("a(bcdefghijkl(mno)p)q"))