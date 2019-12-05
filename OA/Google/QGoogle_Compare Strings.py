class Solution:
    def compare(self,s1,s2):
        wordsA=s1.split()
        wordsB=s2.split()
        freqA=[0]*11
        ans=[]
        for w in wordsA:
            freqA[w.count(min(w))]+=1
        for i in range(1,11):
            freqA[i]+=freqA[i-1]
        for w in wordsB:
            cB=w.count(min(w))
            ans.append(freqA[cB-1])
        return ans

a=Solution()
print(a.compare("abcd aabc bd","aaa aa"))
print(a.compare("abcd aabc bbbbd","vbbbbbbb abaa"))
