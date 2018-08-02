# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder == []:
            return None
        if len(preorder) == 1:
        	return TreeNode(preorder[0])

        root = TreeNode(preorder.pop(0))
        # print(inorder)
        #find where is the root to seperate the left and right sub-tree
        location = inorder.index(root.val)
        left_inorder = inorder[:location]
        right_inorder = inorder[(location+1):]
        left_preorder = preorder[1:(1+len(left_inorder))]
        right_preorder = preorder[(location+1):]
        # print(left_inorder, right_inorder, left_preorder, right_preorder)
        root.left = self.buildTree(preorder, left_inorder)
        root.right = self.buildTree(preorder, right_inorder)
        return root
        

