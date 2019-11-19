class Solution:
    def average(self,S):
        words=S.split()
        return sum(len(word) for word in words)/len(words)

a=Solution()
print(a.average('I am Lingwei Luo'))