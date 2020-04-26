
# 思路: 从底部网上遍历即可，根据x,y坐标将数字放入对应的数组位置, 最后顺序取出排列即可

class Solution:
    def findDiagonalOrder(self, nums):
        m = len(nums)
        n = max(map(len, nums))
        memo = [[] for _ in range(m + n)]
        for x in range(m)[::-1]:
            for y, num in enumerate(nums[x]):
                memo[x + y].append(num)
        return [n for ls in memo for n in ls]


a=Solution()
print(a.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(a.findDiagonalOrder([[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]))