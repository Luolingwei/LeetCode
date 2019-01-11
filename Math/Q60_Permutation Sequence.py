import math
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        k -= 1
        char_list=string=[str(i) for i in range(1,n+1)]
        while n>1:
            n -= 1
            index, k = divmod(k, math.factorial(n))
            char_list = char_list[index]
            char_list=[char_list+char1 for char1 in string if char1 not in char_list]
        return ''.join(char_list)

a=Solution()
print(a.getPermutation(4,9))