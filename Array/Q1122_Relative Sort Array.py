# Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# Output: [2,2,2,1,4,3,3,9,6,7,19]

# 思路: 以arr2中的index为value对arr1进行排序. 不存在arr1中的以1000+n为value顺序放到最后,

class Solution:
    def relativeSortArray(self, arr1, arr2):
        A={n:i for i,n in enumerate(arr2)}
        return sorted(arr1,key=lambda n: A.get(n,1000+n))

a=Solution()
print(a.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19],[2,1,4,3,9,6]))