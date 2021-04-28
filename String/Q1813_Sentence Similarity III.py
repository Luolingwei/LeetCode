
# 思路: 从小的index 0开始比, 比完之后从长的尾部-(L1-i1)开始比, 看最后s1是否能匹配完

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split()
        s2 = sentence2.split()
        L1, L2 = len(s1), len(s2)
        if len(s2)<len(s1): return self.areSentencesSimilar(sentence2,sentence1)
        i1 = 0
        while i1<L1 and s1[i1]==s2[i1]:
            i1+=1
        while i1<L1 and s1[i1] == s2[L2-L1+i1]:
            i1+=1
        return i1==L1


a=Solution()
print(a.areSentencesSimilar("My name is Haley", "My Haley"))