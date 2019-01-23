class Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        #j!=len(words[i]) 或者 j!=0为去重操作
        wordict = {words[i]:i for i in range(len(words))}
        res = []
        for i in range(len(words)):
            for j in range(len(words[i])+1):
                temp1=words[i][:j]
                temp2=words[i][j:]
                if j!=len(words[i]) and temp1[::-1] in wordict and temp2==temp2[::-1] and i!=wordict[temp1[::-1]]:
                    res.append([i,wordict[temp1[::-1]]])
                if temp1[::-1]==temp1 and temp2[::-1] in wordict and i!=wordict[temp2[::-1]]:
                    res.append([wordict[temp2[::-1]],i])
        return res

a=Solution()
print(a.palindromePairs(["abcd","dcba","lls","s","sssll"]))
print(a.palindromePairs(["bat","tab","cat"]))