class Solution:
    def shortestWordDistance(self, words, word1, word2):
        def find1(s):
            prei,ans=None,float('inf')
            for i,word in enumerate(words):
                if s==word:
                    if prei!=None:
                        ans=min(ans,i-prei)
                    prei=i
            return ans
        def find2(s1,s2):
            pre1,pre2,ans=None,None,float('inf')
            for i,w in enumerate(words):
                if w==word1:
                    if pre2!= None:
                        ans=min(ans,i-pre2)
                    pre1=i
                if w==word2:
                    if pre1!=None:
                        ans=min(ans,i-pre1)
                    pre2=i
            return ans
        if word1==word2: return find1(word1)
        else: return find2(word1,word2)

a=Solution()
print(a.shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"],"makes","coding"))
print(a.shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"],"makes","makes"))