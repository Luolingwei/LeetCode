from collections import deque

# 思路: bfs, 每次有两种操作, add或者rotate, 直到遍历完所有可能的string

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        def rotate(s):
            return s[-b:] + s[:-b]

        def add(s):
            res = ""
            for i, c in enumerate(s):
                if i % 2 != 0:
                    res += str((int(c) + a) % 10)
                else:
                    res += c
            return res

        q, visited, res = deque([s]), set(), s
        while q:
            curs = q.popleft()
            if curs not in visited:
                res = min(res, curs)
                visited.add(curs)
                q.append(rotate(curs))
                q.append(add(curs))
        return res


a=Solution()
print(a.findLexSmallestString("5525", 9 ,2))
print(a.findLexSmallestString("74", 5, 1))
print(a.findLexSmallestString("0011", 4, 2))
print(a.findLexSmallestString("43987654", 7, 3))