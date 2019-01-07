class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic={}
        for index,number in enumerate(nums):
            if number in dic:
                if index-dic[number]<=k:
                    return True
            dic[number]=index
        return False

a=Solution()
print(a.containsNearbyDuplicate([1,2,3,1],3))
print(a.containsNearbyDuplicate([1,0,1,1],1))
print(a.containsNearbyDuplicate([1,2,3,1,2,3],2))
print(a.containsNearbyDuplicate([9,9],5))
