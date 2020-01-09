
# 思路: 重新排列，先取余获取Start的位置，然后后面依次分段加入

class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        groups=''.join(S.split('-')).upper()
        L=len(groups)
        start=L%K
        res=groups[:start]
        while start<L:
            res+=('-'+groups[start:start+K])
            start+=K
        return res.lstrip('-')

a=Solution()
print(a.licenseKeyFormatting("5F3Z-2e-9-w",4))
print(a.licenseKeyFormatting("2-5g-3-J",2))