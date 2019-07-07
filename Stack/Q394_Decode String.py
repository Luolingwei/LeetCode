# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

# 思路: stack，碰到']'的时候进行判断，提取字符串strs和n，并加入stack

class Solution:
    def decodeString(self, s):
        stack=[]
        for char in s:
            if char==']':
                n,strs='',''
                while stack[-1]!='[':
                    strs=stack.pop()+strs
                stack.pop()
                while stack and stack[-1].isdigit():
                    n=stack.pop()+n
                stack.append(int(n)*strs)
            else:
                stack.append(char)
        return ''.join(stack)

a=Solution()
print(a.decodeString("3[a]2[bc]"))
print(a.decodeString("3[a2[c]]"))
print(a.decodeString("2[abc]3[cd]ef"))
print(a.decodeString('3[leetcode]'))