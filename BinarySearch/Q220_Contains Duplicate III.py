class Solution:
    # Input: nums = [1, 2, 3, 1], k = 3, t = 0
    # Output: true
    #
    # Input: nums = [1, 0, 1, 1], k = 1, t = 2
    # Output: true
    # k -> index  t -> value

    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
        # if t<0: return False
        # dic={}
        # for i in range(len(nums)):
        #     m=nums[i]//(t+1)
        #     if m in dic or (m-1 in dic and nums[i]-dic[m-1]<=t) or (m+1 in dic and dic[m+1]-nums[i]<=t):
        #         return True
        #     dic[m]=nums[i]
        #     if i>=k: dic.pop(nums[i-k]//(t+1))
        # return False

        dic=set()
        for i in range(len(nums)):
            for n in dic:
                if abs(nums[i]-n)<=t:
                    return True
            dic.add(nums[i])
            if len(dic)>k: dic.remove(nums[i-k])
        return False


a=Solution()
print(a.containsNearbyAlmostDuplicate( [1, 2], 1, 2))
print(a.containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0))
print(a.containsNearbyAlmostDuplicate([1, 0, 1, 1], 1, 2))
print(a.containsNearbyAlmostDuplicate([5, 8, 1, 20], 2, 2))