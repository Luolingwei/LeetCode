
# 思路1: 生成所有可翻转的数字, 长度达到length时, 判断n和rn是否相等

# 思路2: 递归解决, 利用必须翻转后相等的特性减少搜索的数量
# dfs(curL-2)找到所有翻转后相等的curL-2长度的数字
# 然后在两边加上可以翻转的组合即可, 00,11,69,88,96
# 00在最后一次添加时不可加, 这里根据参数curL!=length判断是否是最后一次添加

class Solution:
    # def findStrobogrammatic(self, length):
    #     valid = [0,1,6,8,9]
    #     flip = {0:0,1:1,6:9,8:8,9:6}
    #     res = []
    #     def dfs(n,fn,L,digit):
    #         if L==length:
    #             if n==fn:
    #                 res.append(str(n))
    #             return
    #         for i in valid:
    #             if n+i==0: continue
    #             dfs(n*10+i,flip[i]*digit+fn,L+1,digit*10)
    #     dfs(0,0,0,1)
    #     return res+["0"] if length==1 else res

    def findStrobogrammatic(self, length):
        def dfs(curL,length):
            if curL==0: return [""]
            if curL==1: return ["0","1","8"]
            res = []
            nums = dfs(curL-2,length)
            for n in nums:
                if curL!=length: res.append("0"+n+"0")
                res.append("1"+n+"1")
                res.append("6"+n+"9")
                res.append("8"+n+"8")
                res.append("9"+n+"6")
            return res
        return dfs(length,length)


a=Solution()
print(a.findStrobogrammatic(1))
print(a.findStrobogrammatic(2))
print(a.findStrobogrammatic(3))