class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans=[]
        dic={1:'qwertyuiopQWERTYUIOP',2:'asdfghjklASDFGHJKL',3:'zxcvbnmZXCVBNM'}
        for word in words:
            if word[0] in dic[1]:
                tag=1
            elif word[0] in dic[2]:
                tag=2
            else:
                tag=3
            for i in range(1,len(word)):
                if word[i] not in dic[tag]:
                    break
            else:
                ans.append(word)
        return ans

a=Solution()
print(a.findWords(["Hello", "Alaska", "Dad", "Peace"]))
