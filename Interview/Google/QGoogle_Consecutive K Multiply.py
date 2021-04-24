
class Solution:

    def find(self, nums, k):
        N = len(nums)
        zeros, product, res = 0, 1, float('-inf')
        for i in range(N):
            if i - k >= 0:
                if nums[i - k] == 0:
                    zeros -= 1
                else:
                    product /= nums[i - k]
            if nums[i] == 0:
                zeros += 1
            else:
                product *= nums[i]
            if i>=k-1 and zeros == 0: res = max(res, product)
        return res


    def find2(self, nums, k):
        N = len(nums)
        pre_product = [1]*(N+1)
        zeros = [0]*(N+1)
        res = float('-inf')
        for i in range(1,N+1):
            if nums[i-1]!=0: pre_product[i] = pre_product[i-1]*nums[i-1]
            zeros[i] = zeros[i-1] + (nums[i-1]==0)
            if i>=k and zeros[i] == zeros[i-k]:
                res = max(res, pre_product[i] / pre_product[i-k])
        return res if zeros[-1]==0 else 0


    def find3(self, nums, k):
        N = len(nums)
        pre_product = [1]*(N+1)
        zeros = [0]*(N+1)
        res = float('-inf')
        for i in range(1,N+1):
            if nums[i-1]!=0: pre_product[i] = pre_product[i-1]*nums[i-1]
            zeros[i] = zeros[i-1] + (nums[i-1]==0)
            if i>=k and zeros[i] == zeros[i-k]:
                res = max(res, pre_product[i] / pre_product[i-k])
        return res if zeros[-1]==0 else 0

a=Solution()
print(a.find([1,2,3,4,5],2))
print(a.find([1,0,0,0,5],2))
print(a.find([1,0,0,-4,5],2))
print(a.find([1,0,2,0,-4,5],2))

print(a.find2([1,2,3,4,5],2))
print(a.find2([1,0,0,0,5],2))
print(a.find2([1,0,0,-4,5],2))
print(a.find2([1,0,2,0,-4,5],2))
print(a.find2([1,-1,2,-2,4,-4],2))