
# 思路: 生成以所有可能数字(1-9)开头的序列数
# 一直增加到大于high, 将所有比low大的数添加进res

class Solution:
    def sequentialDigits(self, low: int, high: int):
        res = []
        for i in range(1,10):
            num = digit = i
            while num<=high:
                if num>=low: res.append(num)
                digit+=1
                if digit>9: break
                num = num*10+digit
        return sorted(res)


a=Solution()
print(a.sequentialDigits(100,300))
print(a.sequentialDigits(1000,13000))