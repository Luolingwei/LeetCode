
# 思路: 因为XL只能让L往左替换, RX只能让R往右替换, 所以对应的start的L要在target的右边, 对应的start的R要在target的左边
# 同时RL不能相互跨越, 所以start和end的RL的个数和位置要对应

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        start_pairs = [(i,c) for i,c in enumerate(start) if c in ('L','R')]
        end_pairs = [(i,c) for i,c in enumerate(end) if c in ('L','R')]
        if len(start_pairs)!=len(end_pairs): return False
        for j in range(len(start_pairs)):
            li, lc, ri, rc = start_pairs[j][0], start_pairs[j][1], end_pairs[j][0], end_pairs[j][1]
            if lc!=rc: return False
            if lc == 'L' and li<ri: return False
            if lc == 'R' and li>ri: return False
        return True

a=Solution()
print(a.canTransform("LXXLXRLXXL","XLLXRXLXLX"))