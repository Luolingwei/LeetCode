class Solution:
    def reverseWords(self, s):
        return ' '.join(s.split()[::-1])

a=Solution()
print(a.reverseWords("the sky is blue"))
print(a.reverseWords("  hello world!  "))