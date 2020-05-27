
# 思路: 将第一个不是'a'的字母换成'a', 如果全部都是'a', 将最后一个字母换成'b'
# 如果长度为1, 不能换

class Solution:
    def breakPalindrome(self, palindrome):
        if len(palindrome)==1: return ""
        for i in range(len(palindrome)//2):
            if palindrome[i]!='a':
                return palindrome[:i]+'a'+palindrome[i+1:]
        return palindrome[:-1]+"b"


a=Solution()
print(a.breakPalindrome("a"))
print(a.breakPalindrome("aa"))
print(a.breakPalindrome("abccba"))