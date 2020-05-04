
# 思路: 记录preIndex每次与pre比较即可

class Solution:
    def kLengthApart(self, nums, k: int) -> bool:
        pre=float('-inf')
        for i,n in enumerate(nums):
            if n==1:
                if i-pre<k+1:
                    return False
                pre=i
        return True