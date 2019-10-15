
# 思路: 建立原数和新数的映射关系，按func排序即可.

class Solution:
    def strangsort(self,mapping,nums):
        dic={str(n):str(i) for i,n in enumerate(mapping)}
        def func(num):
            newnum=""
            for c in num:
                newnum+=dic[c]
            return int(newnum)
        return sorted(nums,key=lambda num: func(num))

a=Solution()
print(a.strangsort([3,5,4,6,2,7,9,8,0,1],["990","32","332"]))