class Solution:
    def shortestDistance(self, words, word1, word2):
        pre1,pre2,ans=None,None,float('inf')
        for i,w in enumerate(words):
            if w==word1:
                if pre2!=None:
                    ans=min(ans,i-pre2)
                pre1=i
            if w==word2:
                if pre1!=None:
                    ans=min(ans,i-pre1)
                pre2=i
        return ans

a=Solution()
print(a.shortestDistance(["practice", "makes", "perfect", "coding", "makes"],"coding","practice"))