from collections import Counter

# 思路: 统计各个字符出现的频率
# 从a-z, 以每个字符为分界, 统计a和b需要改变的字符个数, (a中都>分界字符，b中都<=分界字符 || b中都>分界字符，a中都<=分界字符)
# 同时计算condition3

class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        Ca, Cb = [0]*26, [0]*26
        for c in a: Ca[ord(c) - 97] += 1
        for c in b: Cb[ord(c) - 97] += 1
        m, n = len(a), len(b)
        res = float('inf')
        for i in range(26):
            res = min(res, m+n-Ca[i]-Cb[i]) # condition 3
            if i>0:
                Ca[i] += Ca[i-1]
                Cb[i] += Cb[i-1]
            if i!=25:
                res = min(res,m-Ca[i] + Cb[i])
                res = min(res,n-Cb[i] + Ca[i])
        return res


a=Solution()
print(a.minCharacters("aba", "caa"))
print(a.minCharacters("dabadd", "cda"))
print(a.minCharacters("azzzz", "bzzzz"))
print(a.minCharacters("a", "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"))