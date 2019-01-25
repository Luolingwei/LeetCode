class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []
        dic={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        ans=[""]
        for digit in digits:
            ans=[char1+char2 for char1 in ans for char2 in dic[digit]]
        return ans

a=Solution()
print(a.letterCombinations("23"))
print(a.letterCombinations("222"))
print(a.letterCombinations("2"))
print(a.letterCombinations(""))