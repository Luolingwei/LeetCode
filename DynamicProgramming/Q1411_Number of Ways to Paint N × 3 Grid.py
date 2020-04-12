
# 思路: 一行一行地考虑，每一行只可能涂2种或者3种颜色
# 下一行涂2种颜色的方法 = 上一行涂2种*3 + 上一行涂3种*2
# 下一行涂3种颜色的方法 = 上一行涂2种*2 + 上一行涂3种*2
# 迭代到n次结束

class Solution:
    def numOfWays(self, n: int) -> int:
        two,three = 6,6
        for _ in range(n-1):
            two,three = 3*two + 2*three, 2*two + 2*three
        return (two+three)%(10**9+7)

a=Solution()
print(a.numOfWays(1))
print(a.numOfWays(2))
print(a.numOfWays(3))
print(a.numOfWays(5000))