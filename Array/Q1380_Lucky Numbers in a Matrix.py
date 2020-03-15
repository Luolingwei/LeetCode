
# 思路: 因为是unique numbers，所以如果min_rols和max_cols有相同的数字，一定是同一个位置出来的

class Solution:
    def luckyNumbers (self, matrix):
        max_cols=set(map(max,list(zip(*matrix))))
        min_rows=set(map(min,matrix))
        res=[]
        for n in max_cols:
            if n in min_rows:
                res.append(n)
        return res

a=Solution()
print(a.luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))