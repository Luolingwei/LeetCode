class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #solution1
        dic1,dic2={},{}
        for index,char in enumerate(s):
            dic1[char]=dic1.get(char,[])+[index]
        for index,char in enumerate(t):
            dic2[char] = dic2.get(char, []) + [index]
        return sorted(dic1.values())==sorted(dic2.values())

        #solution2
        # return len(set(zip(s,t)))==len(set(s))==len(set(t))

        #solution3
        # return map(s.find, s) == map(t.find, t)

a=Solution()
print(a.isIsomorphic("egg","add"))
print(a.isIsomorphic("ab","aa"))