# Input: text = "ghiabcdefhelloadamhelloabcdefghi"
# Output: 7
# Explanation: We can split the string on "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)".
#
# Input: text = "merchant"
# Output: 1
# Explanation: We can split the string on "(merchant)".
#
# Input: text = "antaprezatepzapreanta"
# Output: 11
# Explanation: We can split the string on "(a)(nt)(a)(pre)(za)(tpe)(za)(pre)(a)(nt)(a)".
#
# Input: text = "aaa"
# Output: 3
# Explanation: We can split the string on "(a)(a)(a)".

# 思路: 从左边两边依次check，一旦发现相同字符串即切割下来

class Solution:
    def longestDecomposition(self, S):
        res,l,r=0,0,len(S)-1
        lchar,rchar='',''
        while l<=r:
            lchar,rchar=lchar+S[l],S[r]+rchar
            if lchar==rchar:
                res+=1 if l==r else 2
                lchar,rchar='',''
            l,r=l+1,r-1
        return res+(lchar!='')

a=Solution()
print(a.longestDecomposition("ghiabcdefhelloadamhelloabcdefghi"))
print(a.longestDecomposition("merchant"))
print(a.longestDecomposition("antaprezatepzapreanta"))
print(a.longestDecomposition("aaa"))
print(a.longestDecomposition("elvtoelvto"))