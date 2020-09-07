
# 思路: 计算出前n个1和后n个1的位置, 然后计算和中间n个1的距离，相乘即可

class Solution:
    def numWays(self, s):
        def find(start, move):
            i, count = start, 0
            while 0 <= i < len(s):
                if s[i] == '1':
                    count += 1
                    if count == n: i0 = i
                    if count == n + 1:
                        i1 = i
                        break
                i += move
            return i0, i1

        mod = 10 ** 9 + 7
        total = s.count('1')
        if total % 3 != 0: return 0
        if total == 0: return ((len(s) - 1) * (len(s) - 2) // 2) % mod
        n = total // 3
        i0, i1 = find(0, 1)
        j0, j1 = find(len(s) - 1, -1)
        return (i1 - i0) * (j0 - j1) % mod


a=Solution()
print(a.numWays("10101"))
print(a.numWays("1001"))
print(a.numWays("0000"))
print(a.numWays("100100010100110"))