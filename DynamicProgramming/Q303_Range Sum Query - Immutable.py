# Given nums = [-2, 0, 3, -5, 2, -1]
#
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3

class NumArray:

    def __init__(self, nums):
        self.sum=[0]*(len(nums)+1)
        for i in range(len(nums)):
            self.sum[i+1]=self.sum[i]+nums[i]
    def sumRange(self, i: int, j: int):
        return self.sum[j+1]-self.sum[i]


# Your NumArray object will be instantiated and called as such:
obj = NumArray([-2, 0, 3, -5, 2, -1])
print(obj.sumRange(0,2))
print(obj.sumRange(2,5))
print(obj.sumRange(0,5))
obj = NumArray([-1])
print(obj.sumRange(0,0))