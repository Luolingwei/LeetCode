
# 思路1: 计算odd和even的preSum数组, 移除1个数组后, 后面的odd和even交换, 前面不变

# 思路2: 动态更新后面和前面的sum

class Solution:
    def waysToMakeFair(self, nums):
        even = [0] * len(nums)
        odd = [0] * len(nums)
        for i, n in enumerate(nums):
            even[i] += even[i-1]
            odd[i] += odd[i-1]
            if i % 2 == 0:
                even[i] += n
            else:
                odd[i] += n

        res = 0
        for i in range(len(nums)):
            evenS = (even[i-1] if i>0 else 0) + odd[-1] - odd[i]
            oddS = (odd[i-1] if i>0 else 0) + even[-1] - even[i]
            if evenS == oddS: res += 1
        return res


    def waysToMakeFair2(self, nums):
        pre, after = [0,0], [sum(nums[::2]), sum(nums[1::2])]
        res = 0
        for i,n in enumerate(nums):
            after[i%2]-=n
            res += (pre[0]+after[1] == pre[1]+after[0])
            pre[i%2]+=n
        return res


a=Solution()
print(a.waysToMakeFair2([2,1,6,4]))
print(a.waysToMakeFair2([1,1,1]))
print(a.waysToMakeFair2([1,2,3]))