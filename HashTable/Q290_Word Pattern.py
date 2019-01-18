class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        #solution1
        dic1,dic2={},{}
        str=str.split()
        if len(str)!=len(pattern): return False
        for i in range(len(str)):
            if dic1.get(pattern[i])!=None and dic1.get(pattern[i])!=str[i]: return False
            dic1[pattern[i]]=str[i]
            if dic2.get(str[i])!=None and dic2.get(str[i])!=pattern[i]: return False
            dic2[str[i]]=pattern[i]
        return True

        #solution2
        # str=str.split()
        # if len(str)!=len(pattern): return False
        # return len(set(zip(pattern,str)))==len(set(pattern))==len(set(str))

a=Solution()
print(a.wordPattern("abba","dog cat cat dog"))
print(a.wordPattern("abba","dog cat cat fish"))
print(a.wordPattern("abba","dog dog dog dog"))
