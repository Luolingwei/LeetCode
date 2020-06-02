
# 思路: 对balls数组进行dfs, 取一半的ball, 记录取出的数组和剩下的数组
# 对于某个数组, 其组合方法数为A(N,N)/A(n1,n1)/A(n2,n2)... 其中n1,n2...为数组中所有大于1的数
# 分母为cal(balls), 分子为所有符合distinct相等的 cal(curballs) * cal(left)之和

class Solution:
    def getProbability(self, balls):

        #对阶乘计算进行优化
        fac = [1] * 50
        for i in range(1, 50):
            fac[i] = fac[i - 1] * i

        def cal(nums):
            N = sum(nums)
            total = fac[N]
            for n in nums:
                if n > 1:
                    total /= fac[n]
            return total

        left = balls[:]
        curballs = [0] * len(balls)
        maxtake = sum(left) // 2
        self.res = 0

        def dfs(takeidx, maxtake, curballs, left):
            if takeidx >= len(left) or maxtake == 0:
                if sum(c > 0 for c in curballs) == sum(l > 0 for l in left) and maxtake == 0:
                    self.res += cal(curballs) * cal(left)
                return
            for n in range(min(left[takeidx] + 1, maxtake + 1)):
                curballs[takeidx] += n
                left[takeidx] -= n
                dfs(takeidx + 1, maxtake - n, curballs, left)
                # backtracking
                curballs[takeidx] -= n
                left[takeidx] += n

        dfs(0, maxtake, curballs, left)
        return self.res / cal(balls)


a=Solution()
print(a.getProbability([2,1,1]))
print(a.getProbability([1,2,1,2]))
print(a.getProbability([6,6,6,6,6,6,6]))