import collections
class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        #solution1
        # dic={}
        # for char in s:
        #     dic[char]=dic.get(char,0)+1
        # for char in t:
        #     if dic.get(char):
        #         dic[char]-=1
        #     else:
        #         return char

        #solution2
        counter=collections.Counter(s+t)
        for key,value in counter.items():
            if value%2==1:
                return key

a=Solution()
print(a.findTheDifference("abcd","abcde"))
print(a.findTheDifference("","b"))