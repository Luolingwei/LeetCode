# Input: [1,1,1,2,2,2]
# Output: [2,1,2,1,2,1]
#
# Input: [1,1,1,1,2,2,3,3]
# Output: [1,3,1,3,2,1,2,1]

# 思路: 利用奇偶index，将数组按频率从小到大排列后叉开.

import collections
class Solution:
    def rearrangeBarcodes(self, barcodes):
        counter=collections.Counter(barcodes)
        barcodes.sort(key=lambda x: (counter[x],x))
        mid=len(barcodes)//2
        barcodes[::2],barcodes[1::2]=barcodes[mid:],barcodes[:mid]
        return barcodes

a=Solution()
print(a.rearrangeBarcodes([1,1,1,1,2,2,2,2]))
print(a.rearrangeBarcodes([1,1,1,1,9,9,9,8,8,8,3,3,3]))
print(a.rearrangeBarcodes([4,3,8,4,4,4,8,3,3,3]))