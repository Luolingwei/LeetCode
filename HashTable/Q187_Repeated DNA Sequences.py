class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dic = {}
        for index in range(len(s)-9):
            dic[s[index:10+index]]=dic.get(s[index:10+index],0)+1
        return [key for key in dic.keys() if dic[key]>1]

a=Solution()
print(a.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
print(a.findRepeatedDnaSequences("AAAAAAAAAAAA"))
print(a.findRepeatedDnaSequences("AAAAAAAAAAA"))
