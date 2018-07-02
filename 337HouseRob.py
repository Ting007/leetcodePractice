# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.dfs(root))

    def dfs(self, root):
        if not root:
            return [0, 0]
        #the total[0] store the rob including the root
        #the total[1] store the rob including the leafs only not robing the root
        total = [0, 0]
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        total[0]=root.val + left[1] + right[1]
        total[1]=max(left) + max(right)
        return total





            
