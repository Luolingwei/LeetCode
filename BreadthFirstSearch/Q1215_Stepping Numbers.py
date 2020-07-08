from collections import deque

# 思路: 从一位数开始, bfs, 每次给每个数增加一个个位数, 让其范围在low, high之间即可

class Solution:
    def countSteppingNumbers(self, low, high):
        q = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
        res = [] if low > 0 else [0]
        while q:
            n = q.popleft()
            if low <= n <= high: res.append(n)
            if n < high:
                digit = n % 10
                if digit - 1 >= 0: q.append(n * 10 + digit - 1)
                if digit + 1 <= 9: q.append(n * 10 + digit + 1)
        return res

a=Solution()
print(a.countSteppingNumbers(0,120))
