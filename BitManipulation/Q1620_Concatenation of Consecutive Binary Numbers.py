
# 思路: 每次加入一个数字, 需要当前res左移该数字的长度位, 然后 |此数
# 但是无需每次用bin求当前数字二进制长度, 当1111 - > 10000时, 才会发生size的增加, 用i&(i-1)==0判断即可

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        size = 0
        res = 0
        mod = 10**9+7
        for i in range(1, n + 1):
            if i & (i - 1) == 0:
                size += 1
            res = ((res << size) | i) % mod
        return res%mod


a=Solution()
print(a.concatenatedBinary(1))
print(a.concatenatedBinary(3))
print(a.concatenatedBinary(12))
print(a.concatenatedBinary(10000))