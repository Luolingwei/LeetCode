class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic={}
        for key,value in enumerate(numbers):
            if target-value in dic.keys():
                return [dic[target-value]+1,key+1]
            else:
                dic[value] = key

a=Solution()
print(a.twoSum([2,7,11,15],9))
print(a.twoSum([2,3,4],6))