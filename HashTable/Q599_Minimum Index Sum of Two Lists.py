# Input:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["KFC", "Shogun", "Burger King"]
# Output: ["Shogun"]
# Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).

# 思路: 将list2做成value:index的字典形式，减少寻找索引次数。

class Solution:
    def findRestaurant(self, list1, list2):
        min_index=float('inf')
        dic2={value:index for index,value in enumerate(list2)}
        for i in range(len(list1)):
            if list1[i] in dic2:
                score=dic2.get(list1[i])+i
                if score<min_index:
                    min_index=score
                    target=[list1[i]]
                elif score==min_index:
                    target.append(list1[i])
        return target

a=Solution()
print(a.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]))
print(a.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],["KFC", "Shogun", "Burger King"]))
print(a.findRestaurant(["vacag","KFC"],["fvo","xrljq","jrl","KFC"]))