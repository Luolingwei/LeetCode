
# 思路: 找到最右边的font满足 <=w && <=h即可, binary search, 注意 mid = (l+r+1)//2
# 如果是 r = mid - 1 则需要 (l+r+1)//2, 因为l可能位置不变, r一定改变, 如果不加1导致l = mid仍在l, 死循环
# 如果是 l = mid + 1 则需要 (l+r)//2, 因为r可能位置不变, l一定改变, 如果加1导致r = mid仍在r, 死循环

class Solution:
    def maxFont(self, text: str, w: int, h: int, fonts, fontInfo):
        l, r = 0, len(fonts)-1
        while l<r:
            mid = (l+r+1)//2
            if self.getTotalWidth(fontInfo, text, fonts[mid])>w or fontInfo.getHeight(fonts[mid])>h:
                r = mid-1
            else:
                l = mid

        if self.getTotalWidth(fontInfo, text, fonts[l])>w or fontInfo.getHeight(fonts[l])>h: return -1
        return fonts[l]

    def getTotalWidth(self, fontInfo, text, font):
        return sum(fontInfo.getWidth(font, c) for c in text)