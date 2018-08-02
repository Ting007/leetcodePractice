class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #first tranversal the tree node by inorder 
        #because it is the BST, so order of value is left, key, right
        nodes = []
        self.tranversal(root, nodes)
        #because it is BST, you know the value is monotonically increasing from left to right
        return min([abs(a-b) for a, b in zip(nodes, nodes[1:])])
            
    def tranversal(self, root, nodes):
        #inorder tranversal
        if root.left:
            self.tranversal(root.left, nodes)
        if root:
            nodes.append(root.val)
        if root.right:
            self.tranversal(root.right, nodes)