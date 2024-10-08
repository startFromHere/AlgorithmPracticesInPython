# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def headBetween(l, r):
            if l > r:
                return None
            i = (l+r) // 2
            node = TreeNode(nums[i])
            node.left = headBetween(l, i-1)
            node.right = headBetween(i+1, r)
            return node
        return headBetween(0, len(nums)-1)

        