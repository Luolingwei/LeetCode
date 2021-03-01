
# 思路: 将两个数组排序, 大的从大往小减，小的从小往大加， 直到两个index都到末尾, 或者gap变成负数
# 如果最后gap仍大于0, 说明不可能

class Solution:
    def minOperations(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        s1, s2 = sum(nums1), sum(nums2)
        if s1<s2:
            return self.minOperations(nums2,nums1)
        total_gap = abs(s1-s2)
        res = 0
        i, j = len(nums1)-1, 0
        while total_gap>0 and (i>=0 or j<=len(nums2)-1):
            gap1 = nums1[i]-1 if i>=0 else -1
            gap2 = 6-nums2[j] if j<=len(nums2)-1 else -1
            if gap1>gap2:
                i-=1
                total_gap -= gap1
            else:
                j+=1
                total_gap -= gap2
            res += 1
        if total_gap>0: return -1
        return res


a=Solution()
print(a.minOperations([1,2,3,4,5,6], [1,1,2,2,2,2]))
print(a.minOperations([1,1,1,1,1,1,1], [6]))
print(a.minOperations([6,6], [1]))