
from collections import Counter

# 思路: 从左边到右边扫描, 每次在A的map中添加, 在B的map中删除, 更新unique number.

class Solution:
    def split(self, str):
        A, B = Counter(), Counter(str)
        uniqueA, uniqueB = 0, len(B.keys())
        res = 0
        for c in str:
            if A[c] == 0: uniqueA += 1
            A[c] += 1
            B[c] -= 1
            if B[c] == 0: uniqueB -= 1
            if uniqueA == uniqueB: res += 1
        return res


a=Solution()
print(a.split("aaaa"))
print(a.split("bac"))
print(a.split("ababa"))