
# 思路: 因为是前k个数的乘积，所以用preSum的时候如果碰到0，直接舍弃前面的数组
# 如果getProduct的时候长度超过了数组说明一定包含了0，直接返回0即可

class ProductOfNumbers:

    def __init__(self):
        self.window=[1]

    def add(self, num: int) -> None:
        if num==0:
            self.window=[1]
        else:
            self.window+=[self.window[-1]*num]

    def getProduct(self, k: int) -> int:
        if k>=len(self.window): return 0
        return self.window[-1]//self.window[-k-1]