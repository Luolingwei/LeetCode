
# dfs分割字符串, 并记录已经分割的Set即可

class Solution:
    # 写法1, 用全局变量
    def maxUniqueSplit(self, s: str) -> int:
        self.res = 0
        def dfs(s, path):
            if not s: self.res = max(self.res, len(path))
            for i in range(1,len(s)+1):
                if s[:i] not in path: dfs(s[i:],path|{s[:i]})
        dfs(s,set())
        return self.res

    # 写法2, 不用全局变量
    def maxUniqueSplit2(self, s: str) -> int:
        def dfs(s, path):
            res = 0
            if not s: return len(path)
            for i in range(1,len(s)+1):
                if s[:i] not in path: res = max(res, dfs(s[i:],path|{s[:i]}))
            return res
        return dfs(s,set())


a=Solution()
print(a.maxUniqueSplit("aa"))
print(a.maxUniqueSplit("ababccc"))
print(a.maxUniqueSplit("aaaaaaaaaaaaaaaa"))

print(a.maxUniqueSplit2("aa"))
print(a.maxUniqueSplit2("ababccc"))
print(a.maxUniqueSplit2("aaaaaaaaaaaaaaaa"))