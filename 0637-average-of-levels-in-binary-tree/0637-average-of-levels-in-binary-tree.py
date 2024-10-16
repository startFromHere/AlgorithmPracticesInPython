# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        level = 0
        cnt = 0
        lastNodeOfCurrentLevel = root
        arr = [root]
        tmp = 0
        ans = []
        while arr:
            node = arr.pop(0)
            tmp += node.val
            cnt += 1
            
            if node.left:
                arr.append(node.left)
            if node.right:
                arr.append(node.right)
            if node == lastNodeOfCurrentLevel:
                ans.append(tmp / cnt)
                tmp = 0
                cnt = 0
                if arr:
                    lastNodeOfCurrentLevel = arr[-1]
                    
        return ans


        