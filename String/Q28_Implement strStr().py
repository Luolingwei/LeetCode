class Solution:
    def strStr(self,haystack,needle):
        left,right=0,len(needle)
        windows=haystack[left:right]
        while right<len(haystack)+1:
            if windows==needle:
                return left
            elif right==len(haystack):
                break
            else:
                windows=windows[1:]
                windows+=haystack[right]
                left,right=left+1,right+1
        return -1

a=Solution()
print(a.strStr("hello","ll"))
print(a.strStr("aaaaa","bba"))
print(a.strStr("aaaaa",""))
print(a.strStr("","aaaaa"))
print(a.strStr("",""))
print(a.strStr("a","a"))
print(a.strStr("mississippi","pi"))