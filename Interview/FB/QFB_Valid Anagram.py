class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1,dic2={},{}
        for c in s:
            dic1[c]=dic1.get(c,0)+1
        for c in t:
            dic2[c]=dic2.get(c,0)+1
        return dic1==dic2

a=Solution()
print(a.isAnagram("anagram","nagaram"))