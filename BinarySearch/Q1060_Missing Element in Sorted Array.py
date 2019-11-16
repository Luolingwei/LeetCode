
# 思路: 对于一个nums[i]，其左边确实的数字个数为nums[i]-nums[0]-i
# 如果左边缺失个数大于等于k，右边不需要再搜索，r=mid-1
# 否则l=mid，搜索出来的l为左边缺失小于k个的rightmost位置，再往右一步则会大于等于k
# 在nums[l]基础上加上右边剩余缺失个数

class Solution:
    def missingElement(self, nums, k):
        l,r=0,len(nums)-1
        while l<r:
            mid=(l+r+1)//2
            if nums[mid]-nums[0]-mid>=k:
                r=mid-1
            else:
                l=mid
        return nums[l]+k-(nums[l]-nums[0]-l)

a=Solution()
print(a.missingElement([4,7,9,10],1))
print(a.missingElement([4,7,9,10],3))
print(a.missingElement([1,2,4],3))