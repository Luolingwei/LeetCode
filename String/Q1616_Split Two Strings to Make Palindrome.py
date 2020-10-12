
# 思路: a,b 在同一位置切割, 考虑prefixA + suffixB.
# a的首部一定和b的尾部要匹配, 如果不匹配, 那么剩下的需要A或者B中间的部分自己构成回文
# a,b greedy匹配首尾, check 两者剩下的middle部分是否Palindrome即可
# prefixB + suffixA 调用check(b,a)即可

class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def pal(s):
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]: return False
                i += 1
                j -= 1
            return True

        def check(a, b):
            L = len(a)
            i, j = 0, L - 1
            while i < j and a[i] == b[j]:
                i += 1
                j -= 1
            return pal(a[i:j + 1]) or pal(b[i:j + 1])

        return check(a, b) or check(b, a)


a=Solution()
print(a.checkPalindromeFormation("x","y"))
print(a.checkPalindromeFormation("abdef","fecab"))
print(a.checkPalindromeFormation("ulacfd","jizalu"))
print(a.checkPalindromeFormation("xbdef","xecab"))