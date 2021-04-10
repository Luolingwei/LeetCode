
# 思路: 对于一个repeat pattern, 可以用 (s+s).find(s,1)找到repeat的最小单位, 为s[:i], 如果i>=N, 则没有repeat pattern
# case 1: 如果有repeat pattern, 则可以对整个s 生成 "%d[%s]"
# case 2: 可以分多个部分分别生成 "%d[%s]"
# case 3: 不生成 "%d[%s]", 原s最短
# 取三种方法的最小length即可

class Solution:
    def encode(self, s: str) -> str:
        memo = {}
        def cal(s):
            if s not in memo:
                N = len(s)
                i = (s+s).find(s,1)
                one = "%d[%s]"%(N//i, cal(s[:i])) if i<N else s
                multis = [cal(s[:x]) + cal(s[x:]) for x in range(1,N)]
                memo[s] = min([one, s] + multis, key = len)
            return memo[s]
        return cal(s)


a=Solution()
print(a.encode("aaa"))
print(a.encode("aaaaa"))
print(a.encode("aaaaaaaaaa"))
print(a.encode("aabcaabcd"))
print(a.encode("abbbabbbcabbbabbbc"))