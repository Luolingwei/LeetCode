# Input: "((("
# Output: 3

# 思路: left和right分别表示没有配对的左括号和右括号的个数.

class Solution:
    def minAddToMakeValid(self, S):
        left=right=0
        for char in S:
            if char==')':
                if not left:right+=1
                else: left-=1
            else:
                left+=1
        return left+right

a=Solution()
print(a.minAddToMakeValid("())"))
print(a.minAddToMakeValid("((("))
print(a.minAddToMakeValid('()'))
print(a.minAddToMakeValid("()))(("))