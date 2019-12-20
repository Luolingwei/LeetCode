class Solution:
    def Binary_sort(self,nums):
        return sorted(nums,key=lambda x: (bin(x)[2:].count('1'),x))

a=Solution()
print(a.Binary_sort([7,8,5,6]))
print(a.Binary_sort([3,1,2]))