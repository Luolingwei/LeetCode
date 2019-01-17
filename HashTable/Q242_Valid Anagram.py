class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(t)==sorted(s)

a=Solution()
print(a.isAnagram("anagram","nagaram"))
print(a.isAnagram("rat","car"))