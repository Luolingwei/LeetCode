import bisect
class Solution:
    def increasingTriplet(self, nums):
        tails=[float('inf')]*2
        for num in nums:
            index=bisect.bisect_left(tails,num)
            if index>=2:return True
            tails[index]=num
        return False

a=Solution()
print(a.increasingTriplet([10,9,2,5,3,7,101,18]))
print(a.increasingTriplet([5,4,3,2,1]))