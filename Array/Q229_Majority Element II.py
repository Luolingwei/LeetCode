class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic={}
        for number in nums:
            dic[number]=dic.get(number,0)+1
        return [key for key in dic.keys() if dic[key]>(len(nums)/3)]
a=Solution()
print(a.majorityElement([3,2,3]))
print(a.majorityElement([1,1,1,3,3,2,2,2]))
