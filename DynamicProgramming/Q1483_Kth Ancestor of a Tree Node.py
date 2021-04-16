

# 思路: 每次将当前parent升级并存储, 1级parent -> 2级parent -> 4级parent ->8级parent
# 找的时候从最大级开始往下减, 直到 k变为0 或者找到 -1
# j的p层parent = j的p-1层parent 的 p-1层parent
# p层parent代表路径长度为2^p

import math

class TreeAncestor:

    def __init__(self, n: int, parent):
        self.max_pow_d = int(math.log2(n))
        self.jump = [[-1] * n for _ in range(self.max_pow_d + 1)]
        self.jump[0] = parent

        for p in range(1, self.max_pow_d + 1):
            for j in range(n):
                pre_parent = self.jump[p - 1][j]
                if pre_parent != -1: self.jump[p][j] = self.jump[p - 1][pre_parent]
        print(self.jump)


    def getKthAncestor(self, node: int, k: int) -> int:
        max_pow_d = self.max_pow_d
        while k > 0 and node != -1:
            if k >= (1 << max_pow_d):
                node = self.jump[max_pow_d][node]
                k -= (1 << max_pow_d)
            else:
                max_pow_d -= 1
        return node


a=TreeAncestor(7,[-1,0,0,1,1,2,2])
print(a.getKthAncestor(3,1))
print(a.getKthAncestor(5,2))
print(a.getKthAncestor(6,3))