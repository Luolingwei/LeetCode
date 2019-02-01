class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic,res={},''
        for char in s:
            dic[char]=dic.get(char,0)+1
        for tuple in sorted(dic.items(),key=lambda d:d[1],reverse=True):
            res+=tuple[0]*tuple[1]
        return res

a=Solution()
print(a.frequencySort("tree"))
print(a.frequencySort("cccaaa"))
print(a.frequencySort("Aabb"))
