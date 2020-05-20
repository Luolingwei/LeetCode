
# 思路1: binary search, 找到最左边让T>=target的nums[i]
# 如果整个数组的和小于target, 直接返回最大数
# 如果查出来l=0, 说明最小的阈值都让数组大于target, target-preS[l-1], 去掉小的部分
# 剩下的右边数字平分即可, round(target - 0.001)表示 0.5向下取, 0.5表示左右两个数n,n+1都可以

# 思路2: 将数组逆序排列,从尾部开始设置最小值,一直找到大于target为止
# 小值可以直接pop并在target中减掉, 因为他们随着阈值提升不会被改变了
# 如果pop完了还没有找到大于target的, 说明整个数组和小于target, 直接返回最大值

class Solution:
    # def findBestValue(self, arr, target):
    #     N = len(arr)
    #     arr.sort()
    #     preS = arr[:]
    #     for i in range(1, N):
    #         preS[i] += preS[i - 1]
    #     if preS[-1]<=target: return arr[-1]
    #     l, r = 0, N - 1
    #     while l < r:
    #         mid = (l + r + 1) // 2
    #         curT = preS[mid] + (N - mid - 1) * arr[mid]
    #         if curT < target:
    #             l = mid + 1
    #         else:
    #             r = mid
    #     target-=(preS[l-1] if l!=0 else 0)
    #     return round((target - 0.001) / (N - l))

    def findBestValue(self, arr, target):
        arr.sort(reverse=True)
        maxN = arr[0]
        while arr and arr[-1]*len(arr)<=target:
            target-=arr.pop()
        return round((target-0.001)/len(arr)) if arr else maxN


a=Solution()
print(a.findBestValue([4,9,3],10))
print(a.findBestValue([2,3,5],10))
print(a.findBestValue([60864,25176,27249,21296,20204],56803))