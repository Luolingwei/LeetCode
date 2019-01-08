class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        prechar='I'
        d = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        for char in s[::-1]:
            ans=ans-d[char] if d[char]<d[prechar] else ans+d[char]
            prechar=char
        return ans

a=Solution()
print(a.romanToInt("III"))
print(a.romanToInt("IV"))
print(a.romanToInt("LVIII"))
print(a.romanToInt("MCMXCIV"))