class Solution:
    def combinBST(self,t1,t2):
        def inorder(root):
            ans=[]
            if not root: return ans
            ans+=inorder(root.left)
            ans+=[root.val]
            ans+=inorder(root.right)
            return ans
        def merge(nums1,nums2):
            ans=[]
            i,j=0,0
            while i<len(nums1) and j<len(nums2):
                if nums1[i]<nums2[j]:
                    ans.append(nums1[i])
                    i+=1
                else:
                    ans.append(nums2[j])
                    j+=1
            ans+=nums1[i:]
            ans+=nums2[j:]
            return ans
        def construct(nums):
            if not nums: return None
            mid=len(nums)//2
            root=TreeNode(nums[mid])
            root.left=construct(nums[:mid])
            root.right=construct(nums[mid+1:])
            return root

        nums1,nums2=inorder(t1),inorder(t2)
        return construct(merge(nums1,nums2))