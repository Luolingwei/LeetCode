
# n&(n-1)表示去掉最末尾的1, n^(n-1)表示最末尾1到最后都是1的二进制数表示

class Solution:
    def minimumOneBitOperations(self, n):
        res, sign = 0, 1
        while n>0:
            res += n^(n-1)*sign
            n &= (n-1)
            sign = -sign
        return abs(res)


a=Solution()
print(a.minimumOneBitOperations(0))
print(a.minimumOneBitOperations(3))
print(a.minimumOneBitOperations(6))
print(a.minimumOneBitOperations(9))
print(a.minimumOneBitOperations(333))