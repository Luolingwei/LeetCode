
# 思路: 从左往右扫描, 碰到重复的数字就从左开始remove, 一直到不含重复数字, 得到以当前数字结尾的最大sum数组

class Solution:
    def maximumUniqueSubarray(self, nums):
        visited = set()
        curS, l, res = 0, 0, 0
        for n in nums:
            while n in visited:
                visited.remove(nums[l])
                curS-=nums[l]
                l+=1
            curS+=n
            visited.add(n)
            res = max(res, curS)
        return res


a=Solution()
print(a.maximumUniqueSubarray([4,2,4,5,6]))
print(a.maximumUniqueSubarray([5,2,1,2,5,2,1,2,5]))