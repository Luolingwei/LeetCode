class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        ans=['']*numRows
        index,step=0,1
        for char in s:
            if index==0:
                step=1
            elif index==numRows-1:
                step=-1
            ans[index]+=char
            index+=step
        return ''.join(ans)

a=Solution()
print(a.convert("PAYPALISHIRING",3))