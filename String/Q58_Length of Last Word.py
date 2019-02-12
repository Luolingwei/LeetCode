class Solution:
    def lengthOfLastWord(self, s):
        str=s.split()
        return len(str[-1]) if str else 0

a=Solution()
print(a.lengthOfLastWord("Hello World"))
print(a.lengthOfLastWord("HelloWorld"))
print(a.lengthOfLastWord(""))
print(a.lengthOfLastWord(" "))