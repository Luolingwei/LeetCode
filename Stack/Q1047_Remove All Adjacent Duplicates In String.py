# Input: "abbaca"
# Output: "ca"

# 思路: 用stack存储字符，新来的字符与stack中的相等时，pop

class Solution:
    def removeDuplicates(self, S):
        stack=[]
        for char in S:
            if stack and stack[-1]==char:
                stack.pop()
            else: stack.append(char)
        return ''.join(stack)

a=Solution()
print(a.removeDuplicates("abbaca"))
print(a.removeDuplicates("abcddeecfe"))
print(a.removeDuplicates("aa"))