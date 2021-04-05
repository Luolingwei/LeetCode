
# 思路: 如果s[l]==s[r], 确定一个c, 两边pointer相对走, 直到不等于c

class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s)-1
        while l<r and s[l]==s[r]:
            c = s[l]
            while l<=r and s[l]==c:
                l+=1
            while l<=r and s[r]==c:
                r-=1
        return r-l+1


a=Solution()
print(a.minimumLength("ca"))
print(a.minimumLength("aa"))
print(a.minimumLength("abaa"))
print(a.minimumLength("aabccabba"))