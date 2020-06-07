
# 思路1: 用zip, 提取前一半和后一般对应位置的pair
# 思路2: 用index进行填充

class Solution:
    # def shuffle(self, nums, n: int):
    #     return [x for (u,v) in zip(nums[:n],nums[n:]) for x in (u,v)]

    def shuffle(self, nums, n: int):
        res = [0]*(2*n)
        for i in range(n):
            res[2*i] = nums[i]
            res[2*i+1] = nums[i+n]
        return res


a=Solution()
print(a.shuffle([2,5,1,3,4,7],3))
print(a.shuffle([1,2,3,4,4,3,2,1],4))