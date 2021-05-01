import random

# 思路: 模拟生成m*n的一维数组, self.end记录当前尾部, 每次random出一个index, 将它与尾部元素交换(memo记录映射, memo[i]表示i位置放的元素)
# 尾部减一, 使尾部元素不可能再出现, 所以每个映射对应的value一定是只出现过一次的, 更新 memo[i] 为 当前end: self.memo.get(self.end,self.end)
# 注意end也有可能是换过1次的

class Solution:

    def __init__(self, n_rows: int, n_cols: int):
        self.m = n_rows
        self.n = n_cols
        self.end = n_rows*n_cols-1
        self.memo = {}

    def flip(self):
        i = random.randint(0,self.end)
        res = self.memo.get(i,i)
        self.memo[i] = self.memo.get(self.end,self.end)
        self.end -= 1
        return [res//self.n, res%self.n]

    def reset(self) -> None:
        self.memo = {}
        self.end = self.m*self.n - 1


a=Solution(1,2)
print(a.flip())
print(a.flip())
a.reset()
print(a.flip())