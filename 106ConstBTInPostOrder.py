class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not postorder:
            return None
        if len(postorder) == 1:
            return TreeNode(postorder[0])
        root = TreeNode(postorder.pop())
        location = inorder.index(root.val)
        left_inorder = inorder[:location]
        right_inorder = inorder[(location+1):]
        left_postorder = postorder[:len(left_inorder)]
        right_postorder = postorder[len(left_inorder):]
        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)
        return root