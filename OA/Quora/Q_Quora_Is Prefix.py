class Solution:
    def prefix(self,A,B):
        memo={""}
        for word1 in A:
            for word2 in list(memo):
                memo.add(word2+word1)
        return all(b in memo for b in B)

a=Solution()
print(a.prefix(["ab","cd","ef","g"],["abef","cdg","abg"]))
print(a.prefix(["ab","cd","ef","g"],["abef","cdg","abg","abc"]))