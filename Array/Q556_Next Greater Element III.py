
# 为了使n变大，必须要用后面的大数换前面的小数，所以从后往前搜索，找到第一个下降的点，用后面的比它大的min替换它，然后把后面排序即可

class Solution:
    def nextGreaterElement(self, n):
        nums=[c for c in str(n)]
        r=len(nums)-1
        while r>=1 and nums[r]<=nums[r-1]:
            r-=1
        if r==0: return -1
        else:
            idx=len(nums)-1
            while nums[idx]<=nums[r-1]:
                idx-=1
            nums[r-1],nums[idx]=nums[idx],nums[r-1]
            nums[r:]=sorted(nums[r:])
        ans=int(''.join(nums))
        return ans if -2 ** 31 <= ans <= 2 ** 31 - 1 else -1


a=Solution()
print(a.nextGreaterElement(1524332))
print(a.nextGreaterElement(134285))
print(a.nextGreaterElement(321))
print(a.nextGreaterElement(1999999999))