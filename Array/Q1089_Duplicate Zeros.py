class Solution:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        i,L=0,len(arr)
        while i<L:
            if not arr[i]:
                arr.insert(i,0),arr.pop()
                i+=2
            else: i+=1

a=Solution()
print(a.duplicateZeros([1,0,2,3,0,4,5,0]))
print(a.duplicateZeros([1,2,3]))
print(a.duplicateZeros([0,0]))