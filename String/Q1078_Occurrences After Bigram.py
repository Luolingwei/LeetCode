class Solution:
    def findOcurrences(self, text, first, second):
        words,ans=text.split(),[]
        for i in range(len(words)-2):
            if words[i]==first and words[i+1]==second:
                ans.append(words[i+2])
        return ans

a=Solution()
print(a.findOcurrences("we will we will rock you",'we','will'))
print(a.findOcurrences("alice is a good girl she is a good student",'a','good'))
print(a.findOcurrences("w",'we','will'))