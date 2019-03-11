class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ans=1
        for num in nums:
            if num<ans:
                continue
            elif num==ans:
                ans+=1
                continue
            else:
                break
        return ans

a=Solution()
print(a.firstMissingPositive([1,2,0]))
print(a.firstMissingPositive([3,4,-1,1]))
print(a.firstMissingPositive([7,8,9,11,12]))
print(a.firstMissingPositive([-2,1,2,4,5]))
print(a.firstMissingPositive([-8,8,-2,2,2]))
print(a.firstMissingPositive([-1,0,1,1,1,2,4]))