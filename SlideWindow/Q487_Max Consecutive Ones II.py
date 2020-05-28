
# 思路: sliding window, 往右走到k<0, 此时需要左边i开始右移
# 一直保持这个size, 直到碰到k>0时size又会扩张, 返回最后的size即可

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        i, k = 0, 1
        for j,n in enumerate(nums):
            k-=(1-n)
            if k<0:
                k+=(1-nums[i])
                i+=1
        return j-i+1

a=Solution()
print(a.findMaxConsecutiveOnes([1,0,1,1,0]))