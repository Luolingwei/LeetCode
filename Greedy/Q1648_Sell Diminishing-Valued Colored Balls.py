
# 思路: 先卖最大的ball, 然后和第二大的一起卖...
# 每一轮卖出的gain是inventory[i]+.....+inventory[i-1]+1 * times
# times每轮增加1(上一个ball减下来并累加到当前轮)
# 如果orders不够当前轮(times*n), 那么进入单独计算并返回

class Solution:
    def maxProfit(self, inventory, orders):
        inventory.sort(reverse=True)
        inventory += [0]
        i, times = 0, 1
        res, mod = 0, 10**9+7
        while orders > 0 and i < len(inventory) - 1:
            n = inventory[i] - inventory[i + 1]
            if orders < n * times:
                m, reminder = divmod(orders, times)
                gain = m * inventory[i] - m * (m - 1) // 2
                res += gain * times
                res += reminder*(inventory[i]-m)
                return res%mod
            gain = n * inventory[i] - n * (n - 1) // 2
            res += gain * times
            orders -= n * times
            times += 1
            i += 1
        return res%mod


a=Solution()
print(a.maxProfit([2,5],4))
print(a.maxProfit([3,5],6))
print(a.maxProfit([2,8,4,10,6],20))
print(a.maxProfit([1000000000],1000000000))
print(a.maxProfit([773160767],252264991))