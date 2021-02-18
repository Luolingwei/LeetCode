class Solution:

    # 思路1: 对字符串切割, 对(s,n)的结果进行cache
    def checkPartitioning(self, s: str) -> bool:
        memo = {}

        def pal(s):
            return s == s[::-1]

        def check(s, n):
            if (s, n) in memo: return memo[(s, n)]
            if n == 1: return pal(s)
            for i in range(1, len(s)):
                if pal(s[:i]) and check(s[i:], n - 1):
                    memo[(s, n)] = True
                    return memo[(s, n)]
            memo[(s, n)] = False
            return memo[(s, n)]

        return check(s, 3)


    # 思路2: 对整个字符串的回文情况进行存储, 然后根据2个分割点判断
    def checkPartitioning2(self, s: str) -> bool:
        L = len(s)
        memo = [[False]*L for _ in range(L)]
        for gap in range(L):
            for l in range(L-gap):
                r = l+gap
                if gap<=1:
                    memo[l][r] = s[l]==s[r]
                    continue
                if s[l]==s[r]: memo[l][r] = memo[l+1][r-1]
        for i in range(L):
            for j in range(i+1,L-1):
                if memo[0][i] and memo[i+1][j] and memo[j+1][L-1]: return True
        return False



a=Solution()
print(a.checkPartitioning2("abcbdd"))
print(a.checkPartitioning2("bcbddxy"))