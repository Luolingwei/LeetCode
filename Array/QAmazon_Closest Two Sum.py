# Intput: [1,6,4,2], 7
# Output: 6,2

# 思路: 先排序，然后two pointers寻找closest pair

class Solution:
    def closest_two(self,nums,target):
        nums.sort()
        l,r=0,len(nums)-1
        mingap=float('inf')
        n1,n2=0,0
        while l<r:
            v=nums[l]+nums[r]
            if abs(v-target)<mingap:
                mingap=abs(v-target)
                n1,n2=nums[l],nums[r]
            if v==target:
                return [n1,n2]
            elif v>target:
                r-=1
            else:
                l+=1
        return [n1,n2]

a=Solution()
print((a.closest_two([1,6,4,2],2)))
print(a.closest_two([6,4,0,29,5,5,1,2],19))